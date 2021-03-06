from django.urls import path

from .views import index, contact, about, pricelist, gallery, product_hoodie, \
                   product_detail, gallery_category, gallery, how_to_order, product, \
                   quality

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('pricelist/', pricelist, name='pricelist'),

    path('gallery/', gallery_category, name='gallery_category'),
    path('gallery/<slug:slug>/', gallery, name='gallery'),

    path('product/<slug:slug>/', product, name='product'),
    path('sell/detail/', product_detail, name='product_detail'),

    # path('product/kaos-polos/', product_polos, name='product_polos'),
    path('product/kaos-hoodie/', product_hoodie, name='product_hoodie'),
    
    path('quality/', quality, name='quality'),
    path('how-to-order/', how_to_order, name='how_to_order'),
]
