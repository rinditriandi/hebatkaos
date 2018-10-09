from django.contrib import admin

from .models import General, Contact, About, Gallery, GalleryCategory

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

admin.site.register(About, AboutAdmin)

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'created_at', 'updated_at', 'user_created')
    exclude = ['user_created',]

admin.site.register(Gallery, GalleryAdmin)

class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ('category', 'image_category', 'created_at', 'updated_at', 'user_created')
    exclude = ['user_created',]

admin.site.register(GalleryCategory, GalleryCategoryAdmin)

