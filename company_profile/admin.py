from django.contrib import admin
from django.db import models

from pagedown.widgets import AdminPagedownWidget

from .models import General, Contact, About, Gallery, GalleryCategory, ProductCategory, Product, \
                    Quality

class GeneralAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'carousel_image', 'created_at', 'updated_at', 'user_created')
    exclude = ['user_created',]

admin.site.register(General, GeneralAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'updated_at', 'user_created')
    exclude = ['user_created',]

admin.site.register(Contact, ContactAdmin)

class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'background_img', 'created_at', 'updated_at', 'user_created')
    exclude = ['user_created',]
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }

admin.site.register(About, AboutAdmin)

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'created_at', 'updated_at', 'user_created')
    exclude = ['user_created',]

admin.site.register(Gallery, GalleryAdmin)

class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'image_category', 'created_at', 'updated_at', 'user_created')
    exclude = ['user_created',]

admin.site.register(GalleryCategory, GalleryCategoryAdmin)

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'image', 'created_at', 'updated_at', 'user_created')
    exclude = ['user_created', 'slug']

admin.site.register(ProductCategory, ProductCategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'product_name', 'model', 'image1', 'image2', 'created_at', 'updated_at', 'user_created')
    exclude = ['user_created', 'slug']

admin.site.register(Product, ProductAdmin)

class QualityAdmin(admin.ModelAdmin):
    list_display = ('title', 'quality_image', 'description', 'created_at', 'updated_at', 'user_created')
    exclude = ['user_created',]
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }

admin.site.register(Quality, QualityAdmin)