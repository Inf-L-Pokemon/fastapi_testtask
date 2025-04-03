from pydantic import BaseModel, HttpUrl


class URLSchema(BaseModel):
    url: HttpUrl
