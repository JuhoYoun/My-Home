from django.db import models
from .validators import validate_image_size


# Create your models here.
class Project(models.Model):
    image = models.ImageField(upload_to='project/', validators=[validate_image_size], null=False)
    title = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=True)

    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'
