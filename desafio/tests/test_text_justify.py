from tests.base_test_case import BaseTestCase


class JustifyFormatterTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.url = "/api/v1/formatters/justify/"

    def test_valid_input(self):
        response = self.post_request(self.text)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("justified_text", data)
        lines = data["justified_text"].split("\n")
        self.assertTrue(all(len(line) == self.width for line in lines[:-1]))

    def test_missing_text(self):
        response = self.post_request("")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["detail"], "Text é um campo obrigatório")

    def test_with_paragraph_breaks(self):
        response = self.post_request(self.text_with_breaks)
        self.assertEqual(response.status_code, 200)
        self.assertIn("justified_text", response.json())
