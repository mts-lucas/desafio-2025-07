from tests.base_test_case import BaseTestCase



class WrapFormatterTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.url = "/api/v1/formatters/wrap/"

    def test_valid_input(self):
        response = self.post_request(self.text)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("formatted_text", data)
        self.assertTrue(all(len(line) <= self.width for line in data["formatted_text"].split("\n")))

    def test_missing_text(self):
        response = self.post_request("")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["detail"], "Text é um campo obrigatório")

    def test_with_paragraph_breaks(self):
        response = self.post_request(self.text_with_breaks)
        self.assertEqual(response.status_code, 200)
        self.assertIn("formatted_text", response.json())
