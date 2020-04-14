from django.db import models

# Create your models here.


class dim(models.Model):
    image = models.ImageField(
        upload_to='documents/',
        width_field='image_width',
        height_field='image_height')
    image_width = models.IntegerField(default=0)
    image_height = models.IntegerField(default=0)

    def __str__(self):
        return self.image
