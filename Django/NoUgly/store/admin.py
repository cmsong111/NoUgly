from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Product_kind)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Destination)
admin.site.register(Cart_product)
