from django.core.exceptions import ValidationError
from django.conf import settings


def validate_image_size(value):
    file_size = value.size
    if file_size > settings.MAX_IMAGE_SIZE:
        raise ValidationError(f"The maximum file size that can be uploaded is {settings.MAX_IMAGE_SIZE_MB}MB")