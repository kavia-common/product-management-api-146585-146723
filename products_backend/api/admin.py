from django.contrib import admin
from django.utils.html import format_html
from .models import Product

# Apply subtle branding using Ocean Professional palette:
# primary: #2563EB, secondary/success: #F59E0B, error: #EF4444

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin configuration for Product."""
    list_display = ("id", "name", "price", "quantity", "stock_status", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name",)
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        ("Basic Info", {"fields": ("name", "price", "quantity")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )

    def stock_status(self, obj):
        color = "#F59E0B" if obj.quantity > 0 else "#EF4444"
        label = "In Stock" if obj.quantity > 0 else "Out of Stock"
        return format_html('<span style="color:{}; font-weight:600;">{}</span>', color, label)

    stock_status.short_description = "Status"
