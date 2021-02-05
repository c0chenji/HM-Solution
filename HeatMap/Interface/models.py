from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from PIL import Image
from django.contrib.auth.hashers import make_password
# Create your models here.+


# Camera table
class Camera(models.Model):

    # rtsp_url = models.CharField(max_length=100)
    camera_model = models.CharField(max_length=40,unique=True)
    rtsp_url = models.ImageField(default='default.jpg', upload_to='images')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def channel(self):
        return Channel.objects.filter(camera=self)

    def __unicode__(self):
        return self.name


# Channel Table
class Channel(models.Model):
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
 #   IP = models.GenericIPAddressField(unique=True)
    IP = models.CharField(max_length=15, unique=True)
    portNum = models.CharField(max_length=5)
    cameraNum = models.CharField(max_length=3)
    description = models.CharField(max_length=255, unique=True)
    enabled = models.BooleanField(default=True)
  #  camera = models.ForeignKey(Camera, on_delete=models.CASCADE,related_name="cameras")
    camera = models.ForeignKey(
    Camera, related_name='channel_camera', on_delete=models.CASCADE)
    coordinates = models.CharField(max_length=1200, default='')
    names = models.CharField(max_length=600, default='')
    directions = models.CharField(max_length=600, default='')

    def save(self, *args, **kwargs):
        self.validate_unique()
        super(Channel, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('Interface-channel', kwargs={'pk': self.pk})


# Frame table
class Frame(models.Model):
    img_name = models.CharField(max_length=40)
    captureTime = models.DateTimeField()
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)

# HeatMap table
class Heatmap(models.Model):
    topColor = models.CharField(max_length=255, default='')
    bottomColor = models.CharField(max_length=255, default='')
    topLeftX = models.IntegerField(default=0)
    topLeftY = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    dwellingTime = models.IntegerField(default=-1)
    zoneArea = models.IntegerField(default=-1)
    frame = models.ForeignKey(Frame, on_delete=models.CASCADE)

# Direction table
class Direction(models.Model):
    topColor = models.CharField(max_length=255, default='')
    bottomColor = models.CharField(max_length=255, default='')
    topLeftX = models.IntegerField(default=0)
    topLeftY = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    direction = models.CharField(max_length=648)
    frame = models.ForeignKey(Frame, on_delete=models.CASCADE)
