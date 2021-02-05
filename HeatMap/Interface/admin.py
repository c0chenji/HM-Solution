from django.contrib import admin
from .models import Camera,Channel,Direction

# Register your models here.
#admin.site.register(Channel)
admin.site.register(Camera)
admin.site.register(Channel)

admin.site.register(Direction)