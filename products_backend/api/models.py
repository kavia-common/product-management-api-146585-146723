from django.db import models


class Product(models.Model):
    """
    Stores a single product entry.

    Fields:
        name: The name of the product.
        price: The price of the product as a decimal value with 2 places.
        quantity: The available stock quantity of the product.
        created_at: Auto timestamp when the product was created.
        updated_at: Auto timestamp when the product was last updated.
    """
    name = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when last updated.")

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self) -> str:
        return f"{self.name} (${self.price})"
