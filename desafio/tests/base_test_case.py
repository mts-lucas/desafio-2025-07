import unittest
from fastapi.testclient import TestClient
from main import start_application


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(start_application())
        self.text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque vestibulum lorem quam, vel euismod est dapibus vel. Sed et placerat erat. Nunc nec aliquam sapien. Praesent massa odio, tincidunt nec tincidunt non, vulputate sed est. Curabitur dignissim elit a ex facilisis pellentesque. Curabitur scelerisque mi quis placerat iaculis. Proin commodo, nisi ac placerat tristique, enim ipsum volutpat arcu, quis fermentum nisi arcu ut leo. Aliquam malesuada suscipit tellus eu elementum. In in massa consectetur, lacinia diam eget, eleifend neque. Vivamus dignissim eget lectus eu tincidunt. Proin condimentum est sit amet tincidunt imperdiet. Phasellus malesuada lacus nec maximus pellentesque. Morbi tincidunt nec urna id vehicula. In posuere nibh metus, consequat sodales eros ultricies id. Nam vitae ipsum massa. Aliquam auctor, sapien eget vulputate euismod, purus tellus vehicula lorem, in porttitor justo erat et sapien. Cras pharetra urna id tellus pharetra aliquam. Nullam eu dignissim libero. In imperdiet arcu augue, vitae vestibulum velit hendrerit ut. Maecenas felis orci, mattis in pharetra ac, interdum vel risus. Proin vel fringilla arcu, sed rutrum augue."

        self.text_with_breaks = " Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque vestibulum lorem quam, vel euismod est dapibus vel. Sed et placerat erat. Nunc nec aliquam sapien. Praesent massa odio, tincidunt nec tincidunt non, vulputate sed est. Curabitur dignissim elit a ex facilisis pellentesque. Curabitur scelerisque mi quis placerat iaculis. Proin commodo, nisi ac placerat tristique, enim ipsum volutpat arcu, quis fermentum nisi arcu ut leo.\n\nAliquam malesuada suscipit tellus eu elementum. In in massa consectetur, lacinia diam eget, eleifend neque. Vivamus dignissim eget lectus eu tincidunt. Proin condimentum est sit amet tincidunt imperdiet. Phasellus malesuada lacus nec maximus pellentesque. Morbi tincidunt nec urna id vehicula. In posuere nibh metus, consequat sodales eros ultricies id. Nam vitae ipsum massa. Aliquam auctor, sapien eget vulputate euismod, purus tellus vehicula lorem, in porttitor justo erat et sapien. Cras pharetra urna id tellus pharetra aliquam. Nullam eu dignissim libero. In imperdiet arcu augue, vitae vestibulum velit hendrerit ut. Maecenas felis orci, mattis in pharetra ac, interdum vel risus. Proin vel fringilla arcu, sed rutrum augue. "
        self.width = 50

    def post_request(self, text):
        return self.client.post(self.url, json={
            "text": text,
            "width": self.width
        })
