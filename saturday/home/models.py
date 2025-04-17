

# Create your models here.
from django.db import models

class Home(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='home_images/')

    def __str__(self):
        return self.title
