from django.urls import path
from reviews import views

urlpatterns = [
    path("", views.products_list, name = "products-list"),
    path("product-detail/<int:pk>", views.product_detail, name = "product-detail"),
    # path("add-review/", views.add_review, name="review-form"),
]