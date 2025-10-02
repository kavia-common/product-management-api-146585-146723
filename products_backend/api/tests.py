from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Product

class HealthTests(APITestCase):
    def test_health(self):
        url = reverse('Health')  # Make sure the URL is named
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"message": "Server is up!"})

class ProductCrudTests(APITestCase):
    def setUp(self):
        self.list_url = "/api/products/"
        self.health_url = reverse('Health')

    def test_product_crud_flow(self):
        # Create
        payload = {"name": "Widget", "price": "19.99", "quantity": 10}
        create_res = self.client.post(self.list_url, data=payload, format="json")
        self.assertEqual(create_res.status_code, 201)
        product_id = create_res.data["id"]

        # Retrieve
        detail_url = f"{self.list_url}{product_id}/"
        get_res = self.client.get(detail_url)
        self.assertEqual(get_res.status_code, 200)
        self.assertEqual(get_res.data["name"], "Widget")

        # Update (PUT)
        put_payload = {"name": "Widget Pro", "price": "24.99", "quantity": 8}
        put_res = self.client.put(detail_url, data=put_payload, format="json")
        self.assertEqual(put_res.status_code, 200)
        self.assertEqual(put_res.data["name"], "Widget Pro")

        # Partial Update (PATCH)
        patch_payload = {"quantity": 5}
        patch_res = self.client.patch(detail_url, data=patch_payload, format="json")
        self.assertEqual(patch_res.status_code, 200)
        self.assertEqual(patch_res.data["quantity"], 5)

        # List with search
        list_res = self.client.get(self.list_url + "?search=Widget")
        self.assertEqual(list_res.status_code, 200)
        self.assertTrue(len(list_res.data["results"]) >= 1 if isinstance(list_res.data, dict) and "results" in list_res.data else len(list_res.data) >= 1)

        # Delete
        del_res = self.client.delete(detail_url)
        self.assertEqual(del_res.status_code, 204)
        self.assertFalse(Product.objects.filter(id=product_id).exists())
