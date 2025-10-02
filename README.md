# product-management-api-146585-146723

Django REST API for managing products.

Quick start:
1. Install dependencies:
   - pip install -r products_backend/requirements.txt
2. Apply migrations:
   - python products_backend/manage.py migrate
3. Run server:
   - python products_backend/manage.py runserver 0.0.0.0:8000
4. API docs:
   - Swagger UI: http://localhost:8000/docs/
   - ReDoc: http://localhost:8000/redoc/
5. Health check:
   - GET http://localhost:8000/api/health/

CRUD Endpoints:
- GET    /api/products/         -> list
- POST   /api/products/         -> create
- GET    /api/products/{id}/    -> retrieve
- PUT    /api/products/{id}/    -> update
- PATCH  /api/products/{id}/    -> partial update
- DELETE /api/products/{id}/    -> delete

Model fields:
- id (auto)
- name (string, required)
- price (decimal, required)
- quantity (integer, required)

Notes:
- Optional list filter: ?search=<text> filters by name.
- Admin: /admin/ (create superuser with `python manage.py createsuperuser`)