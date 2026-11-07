
import requests
import pandas as pd
import plotly.express as px
import streamlit as st

API_BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="API Monitor",
    page_icon="📡",
    layout="wide"
)


def api_request(method, path, **kwargs):
    try:
        response = requests.request(
            method,
            f"{API_BASE_URL}{path}",
            timeout=15,
            **kwargs
        )
        response.raise_for_status()

        if response.status_code == 204:
            return None

        return response.json()

    except requests.RequestException as error:
        st.error(f"API request failed: {error}")
        return None


# Header
st.title("📡 API Monitoring Dashboard")
st.caption("Monitor your endpoints, track availability and analyze response times.")

# Check backend connection
health = api_request("GET", "/")

if health is None:
    st.warning("Start your FastAPI backend before using the dashboard.")
    st.stop()

st.sidebar.success("Backend connected")
st.sidebar.caption("FastAPI · PostgreSQL")

page = st.sidebar.radio(
    "Navigation",
    ["Overview", "Endpoints", "Monitoring History"]
)

# Fetch endpoints
endpoints = api_request("GET", "/endpoints/")

if endpoints is None:
    st.stop()


# ---------------- OVERVIEW ----------------

if page == "Overview":
    st.subheader("Overview")

    all_checks = []

    for endpoint in endpoints:
        checks = api_request(
            "GET",
            f"/endpoints/{endpoint['id']}/checks"
        )

        if checks:
            all_checks.extend(checks)

    total_endpoints = len(endpoints)
    total_checks = len(all_checks)

    successful_checks = sum(
        1 for check in all_checks if check["success"]
    )

    success_rate = (
        successful_checks / total_checks * 100
        if total_checks else 0
    )

    response_times = [
        float(check["response_time_ms"])
        for check in all_checks
        if check["response_time_ms"] is not None
    ]

    avg_response = (
        sum(response_times) / len(response_times)
        if response_times else 0
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Endpoints", total_endpoints)
    col2.metric("Total Checks", total_checks)
    col3.metric("Success Rate", f"{success_rate:.1f}%")
    col4.metric("Avg Response Time", f"{avg_response:.2f} ms")

    st.divider()
    st.subheader("Your Monitored Endpoints")

    if not endpoints:
        st.info("No endpoints added yet. Go to Endpoints to add one.")

    for endpoint in endpoints:
        col1, col2 = st.columns([4, 1])

        with col1:
            st.markdown(f"**{endpoint['name']}**")
            st.caption(endpoint["url"])

        with col2:
            if st.button(
                "Check Now",
                key=f"check_{endpoint['id']}"
            ):
                result = api_request(
                    "POST",
                    f"/endpoints/{endpoint['id']}/checks"
                )

                if result is not None:
                    st.success(
                        f"Check completed! Status: "
                        f"{result['status_code']}"
                    )
                    st.rerun()

        st.divider()


# ---------------- ENDPOINTS ----------------

elif page == "Endpoints":
    st.subheader("Manage Endpoints")

    with st.form("add_endpoint"):
        name = st.text_input("Endpoint Name")
        url = st.text_input(
            "Endpoint URL",
            placeholder="https://example.com"
        )

        submitted = st.form_submit_button("Add Endpoint")

        if submitted:
            if not name.strip() or not url.strip():
                st.warning("Please enter both name and URL.")
            else:
                result = api_request(
                    "POST",
                    "/endpoints/",
                    json={
                        "name": name.strip(),
                        "url": url.strip()
                    }
                )

                if result is not None:
                    st.success("Endpoint added successfully!")
                    st.rerun()

    st.divider()
    st.subheader("Registered Endpoints")

    if not endpoints:
        st.info("No endpoints registered yet.")

    for endpoint in endpoints:
        col1, col2 = st.columns([5, 1])

        with col1:
            st.markdown(f"**{endpoint['name']}**")
            st.caption(endpoint["url"])
            st.caption(f"Endpoint ID: {endpoint['id']}")

        with col2:
            if st.button(
                "Delete",
                key=f"delete_{endpoint['id']}"
            ):
                result = api_request(
                    "DELETE",
                    f"/endpoints/{endpoint['id']}"
                )

                if result is None:
                    st.success("Endpoint deleted!")
                    st.rerun()

        st.divider()


# ---------------- MONITORING HISTORY ----------------

elif page == "Monitoring History":
    st.subheader("Monitoring History")

    if not endpoints:
        st.info("Add an endpoint before viewing its history.")
    else:
        endpoint_options = {
            f"{endpoint['name']} (ID: {endpoint['id']})":
            endpoint["id"]
            for endpoint in endpoints
        }

        selected_name = st.selectbox(
            "Select Endpoint",
            list(endpoint_options.keys())
        )

        selected_id = endpoint_options[selected_name]

        checks = api_request(
            "GET",
            f"/endpoints/{selected_id}/checks"
        )

        if checks:
            df = pd.DataFrame(checks)

            df["response_time_ms"] = pd.to_numeric(
                df["response_time_ms"],
                errors="coerce"
            )

            df["checked_at"] = pd.to_datetime(df["checked_at"])

            st.subheader("Response Time Trend")

            chart_df = df.dropna(subset=["response_time_ms"])

            if not chart_df.empty:
                fig = px.line(
                    chart_df.sort_values("checked_at"),
                    x="checked_at",
                    y="response_time_ms",
                    markers=True,
                    labels={
                        "checked_at": "Time",
                        "response_time_ms": "Response Time (ms)"
                    }
                )

                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("No response-time data available.")

            st.subheader("Check Records")

            st.dataframe(
                df.sort_values("checked_at", ascending=False),
                use_container_width=True,
                hide_index=True
            )

        else:
            st.info("No monitoring history available for this endpoint yet.")
