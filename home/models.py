from django.db import models
import uuid

class ImageModel(models.Model):
    uid = models.UUIDField(unique=True,primary_key=True,editable=False,default=uuid.uuid4)
    image = models.ImageField(upload_to="images")
    watermark_text = models.CharField(max_length=100)
