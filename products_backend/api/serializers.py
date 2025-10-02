from rest_framework import serializers
from .models import Product


# PUBLIC_INTERFACE
class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for Product model.

    Exposes id, name, price, quantity, created_at, updated_at.
    Includes simple validation for non-negative price and quantity.
    """

    id = serializers.IntegerField(read_only=True, help_text="Auto-generated primary key.")
    name = serializers.CharField(
        max_length=255,
        help_text="Product name.",
        allow_blank=False,
    )
    price = serializers.DecimalField(
        max_digits=12,
        decimal_places=2,
        help_text="Product price as decimal with 2 places.",
    )
    quantity = serializers.IntegerField(
        help_text="Available stock quantity (integer).",
    )
    created_at = serializers.DateTimeField(read_only=True, help_text="Creation timestamp (UTC).")
    updated_at = serializers.DateTimeField(read_only=True, help_text="Last update timestamp (UTC).")

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "price",
            "quantity",
            "created_at",
            "updated_at",
        ]

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price must be non-negative.")
        return value

    def validate_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("Quantity must be non-negative.")
        return value
