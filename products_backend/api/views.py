from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Product
from .serializers import ProductSerializer


@api_view(['GET'])
def health(request):
    """
    Health check endpoint.

    Returns:
        200 OK with a simple JSON payload indicating the server is up.
    """
    return Response({"message": "Server is up!"})


# PUBLIC_INTERFACE
class ProductViewSet(viewsets.ModelViewSet):
    """
    A viewset providing the standard actions for Product CRUD.

    Endpoints:
        - GET    /api/products/           -> list products
        - POST   /api/products/           -> create product
        - GET    /api/products/{id}/      -> retrieve product
        - PUT    /api/products/{id}/      -> update product (full)
        - PATCH  /api/products/{id}/      -> partial update product
        - DELETE /api/products/{id}/      -> delete product

    Query Params (list):
        - search (optional): case-insensitive substring filter on name.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.query_params.get("search")
        if search:
            qs = qs.filter(name__icontains=search)
        return qs

    @swagger_auto_schema(
        operation_id="product_list",
        operation_summary="List products",
        operation_description="Retrieve a paginated list of products. Optional search by name using `?search=`.",
        manual_parameters=[
            openapi.Parameter(
                name="search",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                required=False,
                description="Case-insensitive substring filter applied to product name.",
            )
        ],
        responses={200: ProductSerializer(many=True)},
        tags=["Products"],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="product_create",
        operation_summary="Create a product",
        operation_description="Create a new product with name, price, and quantity.",
        request_body=ProductSerializer,
        responses={201: ProductSerializer, 400: "Bad Request"},
        tags=["Products"],
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="product_retrieve",
        operation_summary="Retrieve a product",
        operation_description="Retrieve a product by its ID.",
        responses={200: ProductSerializer, 404: "Not Found"},
        tags=["Products"],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="product_update",
        operation_summary="Update a product",
        operation_description="Update all fields of a product by its ID.",
        request_body=ProductSerializer,
        responses={200: ProductSerializer, 400: "Bad Request", 404: "Not Found"},
        tags=["Products"],
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="product_partial_update",
        operation_summary="Partially update a product",
        operation_description="Update one or more fields of a product by its ID.",
        request_body=ProductSerializer,
        responses={200: ProductSerializer, 400: "Bad Request", 404: "Not Found"},
        tags=["Products"],
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_id="product_delete",
        operation_summary="Delete a product",
        operation_description="Delete a product by its ID.",
        responses={204: "No Content", 404: "Not Found"},
        tags=["Products"],
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
