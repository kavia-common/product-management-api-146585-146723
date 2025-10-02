"""
URL configuration for config project.
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.decorators.csrf import csrf_exempt

openapi_tags = [
    {"name": "Health", "description": "Service health check."},
    {"name": "Products", "description": "CRUD operations for products."},
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

schema_view = get_schema_view(
   openapi.Info(
      title="Products API",
      default_version='v1',
      description="A REST API to manage products with CRUD operations.",
      contact=openapi.Contact(name="API Support", email="support@example.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

def get_full_url(request):
    scheme = request.scheme
    host = request.get_host()
    forwarded_port = request.META.get("HTTP_X_FORWARDED_PORT")

    if ':' not in host and forwarded_port:
        host = f"{host}:{forwarded_port}"

    return f"{scheme}://{host}"

@csrf_exempt
def dynamic_schema_view(request, *args, **kwargs):
    url = get_full_url(request)
    view = get_schema_view(
        openapi.Info(
            title="Products API",
            default_version='v1',
            description="Interactive API documentation for Products service.",
            contact=openapi.Contact(name="API Support", email="support@example.com"),
        ),
        public=True,
        url=url,
    )
    # The with_ui view doesn't take tags directly, but tags are picked from view decorators.
    return view.with_ui('swagger', cache_timeout=0)(request)

urlpatterns += [
    re_path(r'^docs/$', dynamic_schema_view, name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'^swagger\.json$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]