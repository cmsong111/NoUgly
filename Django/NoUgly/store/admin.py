from django.contrib import admin
from .models import *
from django.utils.html import format_html


@admin.register(Product_kind)
class ProductkindAdmin(admin.ModelAdmin):
    list_display = ['id', 'kind']
    list_per_page = 10

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['fIDX', 'name', 'grade']
    list_per_page = 12

    fieldsets = (
        ('제품정보', {
            "fields":
                ['name', 'kind']
        }),
        ('제품세부정보', {
            "fields":
                ['grade', 'date', 'weight', 'field', 'price'], 'classes': ['collapse']
        }),
        ('제품이미지', {
            "fields":
                ['image'], 'classes': ['collapse']
        })
    )

    def image_tag(self, obj):
        return format_html('<img src="{}" width="50px;"/>'. format(obj.image.url))
    image_tag.short_description = '이미지'


@ admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'purchase_time', 'uIDX']


admin.site.register(Cart_product)
