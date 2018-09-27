from django.conf import settings
from django.db import models

class General(models.Model):
    title           = models.CharField(max_length=120)
    description     = models.CharField(max_length=256)
    carousel_image  = models.ImageField(upload_to='carousel/', max_length=255)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    user_created    = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
    
    def save_model(self, request, obj, form, change):
        obj.user_created = request.user
        super().save_model(request, obj, form, change)

class Contact(models.Model):
    name            = models.CharField(max_length=120)
    email           = models.EmailField()
    subject         = models.CharField(max_length=256)
    message         = models.TextField()
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    user_created    = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

class About(models.Model):
    title           = models.CharField(max_length=120)
    description     = models.TextField()
    background_img  = models.ImageField(upload_to='about', max_length=255)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    user_created    = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title