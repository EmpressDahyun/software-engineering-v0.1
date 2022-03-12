from django.contrib import admin

from stellaris.models import Category
from .models import Category, Gallery, PartyTraysCategory, PartyTraysProduct, Product
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Gallery)
admin.site.register(PartyTraysCategory)
admin.site.register(PartyTraysProduct)