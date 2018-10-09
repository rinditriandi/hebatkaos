from django.shortcuts import render, get_object_or_404

from .models import General, Gallery, GalleryCategory, About

def index(request):
    qs = General.objects.all()
    context = {
        'qs': qs
    }
    return render(request, 'profile/home.html', context)

def contact(request):
    return render(request, 'profile/contact_us.html', {})

def about(request):
    about = About.objects.all()
    print(about)
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

def gallery(request, pk):
    category = get_object_or_404(GalleryCategory, pk=pk)
    
    context = {
        'category': category
    }
    return render(request, 'profile/gallery.html', context)


def product_polos(request):
    return render(request, 'profile/product/kaos_polos.html', {})

def product_hoodie(request):
    return render(request, 'profile/product/kaos_hoodie.html', {})

def product_detail(request):
    return render(request, 'profile/product/product_detail.html', {})

def how_to_order(request):
    return render(request, 'profile/how_order.html', {})
