from django.urls import path

from .views import index, contact, about, pricelist, gallery, product_polos, product_hoodie, \
                   product_detail, gallery_category, gallery, how_to_order

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('pricelist/', pricelist, name='pricelist'),

    path('gallery/', gallery_category, name='gallery_category'),
    path('gallery/<slug:slug>/', gallery, name='gallery'),

    path('product/kaos-polos/', product_polos, name='product_polos'),
    path('product/kaos-hoodie/', product_hoodie, name='product_hoodie'),
    path('product/detail/', product_detail, name='product_detail'),

    path('how-to-order/', how_to_order, name='how_to_order'),
]
