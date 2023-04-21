from django.contrib import admin
from image_upload.models import *
# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass
