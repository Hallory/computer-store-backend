from django.contrib import admin

from catalog.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "parent")
    search_fields = ("name", "slug")
    list_filter = ("parent",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "brand", "in_stock", "rating", "created_at")
    search_fields = ("name", "slug", "brand", "description")
    list_filter = ("category", "brand", "in_stock")
    prepopulated_fields = {"slug": ("name",)}
    raw_id_fields = ("category",)
    readonly_fields = ("created_at",)
    ordering = ("-created_at",)
