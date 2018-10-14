from django.shortcuts import render, get_object_or_404

from .models import General, Gallery, GalleryCategory, About, ProductCategory, Quality

def index(request):
    qs = General.objects.all()
    products = ProductCategory.objects.all()
    context = {
        'qs': qs,
        'products': products
    }
    return render(request, 'profile/home.html', context)

def contact(request):
    return render(request, 'profile/contact_us.html', {})

def about(request):
    about = About.objects.all()
    context = {
        'about': about
    }
    return render(request, 'profile/about.html', context)

def pricelist(request):
    return render(request, 'profile/pricelist.html', {})

def gallery_category(request):
    categories = GalleryCategory.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'profile/gallery_category.html', context)

def gallery(request, slug):
    category = get_object_or_404(GalleryCategory, slug=slug)
    
    context = {
        'category': category
    }
    return render(request, 'profile/gallery.html', context)

def product(request, slug):
    product = get_object_or_404(ProductCategory, slug=slug)
    context = {
        'product': product
    }
    return render(request, 'profile/product/product.html', context)


# def product_polos(request):
#     return render(request, 'profile/product/kaos_polos.html', {})

def product_hoodie(request):
    return render(request, 'profile/product/kaos_hoodie.html', {})

def product_detail(request):
    # products = get_object_or_404(ProductCategory)
    # print(products)

    # context = {
    #     'products': products
    # }
    return render(request, 'profile/product/product_detail.html', {})

def how_to_order(request):
    return render(request, 'profile/how_order.html', {})

def quality(request):
    quality = Quality.objects.all()
    print(quality)
    context = {
        'qualities': quality
    }
    return render(request, 'profile/quality.html', context)