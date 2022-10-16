from stegano import exifHeader
from faker import Faker
from project.backend.constants import UPLOAD_FOLDER


def image_encode(img, message: str) -> str:
    img_name = img.filename
    path = UPLOAD_FOLDER + img_name
    img.save(path)
    fake = Faker()
    shifred_img = UPLOAD_FOLDER + f"{fake.unique.password(special_chars=False)}.jpg"
    exifHeader.hide(UPLOAD_FOLDER + img_name, shifred_img, message)
    return UPLOAD_FOLDER + img_name


def image_decode(shifred_img):
    return exifHeader.reveal(shifred_img).decode()
