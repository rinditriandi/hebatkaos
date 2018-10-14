from django.conf import settings
from django.template.defaultfilters import slugify


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

    class Meta:
        verbose_name = 'Hubungi Kami'
        verbose_name_plural = 'Hubungi Kami'

    def __str__(self):
        return self.title

class About(models.Model):
    title           = models.CharField(max_length=120)
    description     = models.TextField()
    background_img  = models.ImageField(upload_to='about', max_length=255)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    user_created    = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Tentang Kami'
        verbose_name_plural = 'Tentang Kami'
        

    def __str__(self):
        return self.title

class GalleryCategory(models.Model):
    category        = models.CharField(max_length=128)
    slug            = models.SlugField(max_length=128, blank=True, null=True, unique=True)
    image_category  = models.ImageField(upload_to='gallery')
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    user_created    = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Galeri Kategori'
        verbose_name_plural = 'Galeri Kategori'

    def __str__(self):
        return self.category
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.category)
        super(GalleryCategory, self).save(*args, **kwargs)

class Gallery(models.Model):
    category        = models.ForeignKey(GalleryCategory, null=True, blank=True, related_name='galleries', on_delete=models.CASCADE)
    title           = models.CharField(max_length=120)
    slug            = models.SlugField(max_length=120, blank=True, null=True, unique=True)
    image           = models.ImageField(upload_to='gallery')
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    user_created    = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Galeri'
        verbose_name_plural = 'Galeri'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Gallery, self).save(*args, **kwargs)

class HowToOrder(models.Model):
    title           = models.CharField(max_length=120)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    user_created    = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

class ProductCategory(models.Model):
    category        = models.CharField(max_length=120)
    slug            = models.SlugField(max_length=120,blank=True, null=True, unique=True)
    image           = models.ImageField(upload_to='product', blank=True, null=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    user_created    = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Produk Kategori'
        verbose_name_plural = 'Produk Kategori'

    def __str__(self):
        return self.category
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.category)
        super(ProductCategory, self).save(*args, **kwargs)

class Product(models.Model):
    category        = models.ForeignKey(ProductCategory, null=True, blank=True, related_name='products', on_delete=models.CASCADE)
    product_name    = models.CharField(max_length=255)
    slug            = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    image1          = models.ImageField(upload_to='product', blank=True, null=True)
    image2          = models.ImageField(upload_to='product', blank=True, null=True)
    model           = models.CharField(max_length=120)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    user_created    = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Produk'
        verbose_name_plural = 'Produk'

    def __str__(self):
        return self.product_name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super(Product, self).save(*args, **kwargs)

class Quality(models.Model):
    title           = models.CharField(max_length=120)
    quality_image   = models.ImageField(upload_to='quaility')
    description     = models.TextField()
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    user_created    = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Kualitas Kaos'
        verbose_name_plural = 'Kualitas Kaos'

    def __str__(self):
        return self.title