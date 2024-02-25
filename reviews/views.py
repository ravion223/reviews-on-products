from django.http import HttpResponse
from django.shortcuts import redirect, render
from reviews.models import Product, Review


# Create your views here.


def products_list(request):
    products = Product.objects.all()

    context = {
        "products": products
    }

    return render(request,
                  template_name="products/products-list.html",
                  context=context)


# def add_review(request):
#     if request.method == "POST":
#         author = request.POST.get('author')
#         review_text = request.POST.get('review-text')
#         rating = request.POST.get('rating')

#         review = Review.objects.create(
#             product = product,
#             author = author,
#             text = review_text,
#             rating = rating
#         )
#     else:
#         return render(request,
#                       template_name="products/review-form.html")


def product_detail(request, pk):
    product = Product.objects.get(id=pk)

    context = {
        "product": product,
        "reviews": product.reviews.all(),
    }

    if request.method == "POST":
        author = request.POST.get('author')
        review_text = request.POST.get('review-text')
        rating = request.POST.get('rating')

        review = Review.objects.create(
            product = product,
            author = author,
            text = review_text,
            rating = rating
        )
        return render(request,
                template_name="products/product-detail.html",
                context=context)
    
    return render(request,
                template_name="products/product-detail.html",
                context=context)