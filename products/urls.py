from django.urls import path
from .views import ProductView,ProductCreateView,ProductDetailView

urlpatterns = [
    path('product/', ProductView.as_view(), name='products-list'),
    path('product/create/', ProductCreateView.as_view(), name='products-create'),
    path('product/<int:id>/', ProductDetailView.as_view(), name='products-detail'),
]