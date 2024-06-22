from deepface import DeepFace
from api.models import ImagePair

async def compare_images(image_pair: ImagePair):
    # Download the images from the provided URLs
    image1 = image_pair.image1_url
    image2 = image_pair.image2_url

    is_same_person = DeepFace.verify(img1_path=image1, img2_path=image2)

    return is_same_person