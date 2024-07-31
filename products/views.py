from django.shortcuts import render,redirect
from django.views import View
from products.models import Product
from products.forms import  ProductForm
from django.views.generic import ListView,DetailView
from django.contrib import messages
from django.core.paginator import Paginator
class ProductView(View):
    def get(self,request):
        products=Product.objects.all().order_by('id')
        pagination=Paginator(products,1)
        page = request.GET.get('page', 1)
        pages = pagination.get_page(page)
        context={"pages":pages}
        return render(request,"shop.html",context)
# class ProductListView(ListView):
#     model =Product
#     template_name = "shop.html"
#     context_object_name = "products"

class ProductDetailView(DetailView):
    model =Product
    pk_url_kwarg = "id"
    template_name = "shop-detail.html"
    context_object_name = "product"

class ProductCreateView(View):
    def get(self,request):
        form=ProductForm()
        return render(request,'product_create.html',{'form':form  })
    def post(self,request):
        form=ProductForm(request.POST)
        if form.is_valid():
            product=form.save(commit=False)
            product.slug=product.title+"001"
            product.save()
            return redirect("products-list")
