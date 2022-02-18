

from rest_framework.pagination import PageNumberPagination


class ProductPageNumberPagination(PageNumberPagination):
    page_size = 4


class CartProuductNumberPagination(PageNumberPagination):
    page_size = 5
