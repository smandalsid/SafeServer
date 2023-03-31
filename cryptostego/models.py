from django.db import models

# Create your models here.

class Image(models.Model):
    image_id=models.CharField(primary_key=True, max_length=5, null=False, blank=False)
    image=models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.image_id
    

class Audio(models.Model):
    audio_id=models.CharField(primary_key=True, max_length=5, null=False, blank=False)
    audio=models.FileField(null=False, blank=False)
    
    def __str__(self):
        return self.audio_id