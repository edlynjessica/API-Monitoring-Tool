from pydantic import BaseModel, ConfigDict


class EndpointCreate(BaseModel):
    name:str
    url:str

# to create a endpoint, the user must send name, and url in the post request...

class EndpointResponse(BaseModel):
    id:int
    user_id:int
    name:str
    url:str
    model_config = ConfigDict(from_attributes=True)

# when we return the endpoint, we need to return the id, user_id, name, and url. The model_config is used to tell pydantic to read the data from SQLAlchemy model object...