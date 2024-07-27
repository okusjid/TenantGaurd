from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        arbitrary_types_allowed = True

class TokenData(BaseModel):
    username: str | None = None

    class Config:
        arbitrary_types_allowed = True
