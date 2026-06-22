from django.urls import path

from product.views import ProductView, SingleProductView, SaleView

urlpatterns = [
    path("", ProductView.as_view(),),
    path("sell/", SaleView.as_view(),),
    path("<product_id>/", SingleProductView.as_view(),),
]