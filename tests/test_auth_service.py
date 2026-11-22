from src.services.auth_service import hash_password, verify_password

password = "mySecurePassword123"

hashed = hash_password(password)

print("Hashed:", hashed)
print("Correct password:", verify_password(password, hashed))
print("Wrong password:", verify_password("wrongPassword", hashed))