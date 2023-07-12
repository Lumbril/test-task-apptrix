import sys

from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile

from APPTRIX.settings import BASE_DIR


def watermark_photo(avatar):
    base_image = Image.open(avatar)
    watermark = Image.open(str(BASE_DIR) + '/api/packs/watermark.png')

    base_image.paste(watermark, (0, 0))

    return base_image
