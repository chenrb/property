from django.test import TestCase


class IndexViewTests(TestCase):
    def test_root_url_renders_index_template(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
