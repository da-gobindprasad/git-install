from django.shortcuts import render, redirect
from .models import Products
from django.http import HttpResponse
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    product_list = Products.objects.all()
    search = request.GET.get('search')

    if search != '' and search is not None:
        product_list = product_list.filter(product_name__icontains=search)

    paginator = Paginator(product_list, 8)
    page = request.GET.get('page')
    product_list = paginator.get_page(page)
    nums = "a" * product_list.paginator.num_pages

    return render(request, 'index.html', {'product_list': product_list, 'nums': nums})


class CreateItem(CreateView):
    model = Products
    fields = ['product_name', 'product_category', 'product_description',
              'product_price', 'product_image']
    template_name = 'item-form.html'

    def form_valid(self, form):
        return super().form_valid(form)


class ProductDetail(DetailView):
    model = Products
    template_name = 'details.html'
    context_product_name = 'product'


def update_item(request, id):
    item = Products.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('product_list')

    return render(request, 'item-form.html', {'form': form, 'item': item})
