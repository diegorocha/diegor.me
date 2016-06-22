# coding: utf-8

import app
import unittest


class TestAp(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_home(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status_code, 302)

    def test_404(self):
        rv = self.app.get('/foo')
        self.assertIn(rv.status_code, [302, 404])

if __name__ == '__main__':
    unittest.main()
