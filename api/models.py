from pydantic import BaseModel

class ImagePair(BaseModel):
    image1_url: str
    image2_url: str