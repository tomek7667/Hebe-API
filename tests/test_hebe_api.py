# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest
import os

from hebe_api import Hebe


EXAMPLE_HEBE_USERNAME = os.getenv("EXAMPLE_HEBE_USERNAME")
EXAMPLE_HEBE_PASSWORD = os.getenv("EXAMPLE_HEBE_PASSWORD")
print(EXAMPLE_HEBE_USERNAME)

class TestHebeAPI(unittest.TestCase):
    def test_authenticate(self):
        hebe = Hebe()
        hebe.authenticate()


if __name__ == '__main__':
    unittest.main()
