from fastapi import APIRouter, Body
from api.models import ImagePair
from api.services import compare_images
import logging

api_router = APIRouter(prefix="/api/v1")

@api_router.get("/")
async def main():
    return {"message": "Hi!"}

@api_router.post("/compare_images")
async def compare_images_endpoint(image_pair: ImagePair = Body(...)):
    logging.info("POST: /api/v1/compare_images")
    return await compare_images(image_pair)