from django.db import models
from django.contrib.auth.models import User
from io import BytesIO
from django.core.files.storage import default_storage
from PIL import Image

# Create your models here.

class Author(models.Model):

    user = models.OneToOneField(User, verbose_name=("User"), on_delete=models.CASCADE)
    picture = models.ImageField(
        ("Picture"), upload_to="static", default="static/flavio.jpeg", blank=True
    )
    class meta:
        verbose_name= "Author"
        verbose_name_plural="Authors"

    def __str__(self) -> str:
        return self.user.get_full_name()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.picture:
            img = Image.open(default_storage.open(self.picture.name))    
            if img.mode != 'RGB':
                img = img.convert('RGB')
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                buffer = BytesIO()
                img.save(buffer, format="JPEG")
                default_storage.save(self.picture.name, buffer)
