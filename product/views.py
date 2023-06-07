from django.shortcuts import render, get_object_or_404

from product.models import Product
from .forms import ProductForm
# Create your views here.
def products(request):
    q = request.GET.get('q', None)
    products = ''
    if q is None or q is "":
        products = Product.objects.all()
    elif q is not None:
        products = Product.objects.filter(title__contains=q)
    return render(request, 'product/product.html', {'products': products })


def detail(request, id=None):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product/detail.html', locals())

def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('product/')
    else:
        form = ProductForm()
        return render(request, 'product/edit.html', {'form': form})