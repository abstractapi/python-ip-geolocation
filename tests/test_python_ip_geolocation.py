import unittest
import os, sys

from python_ip_geolocation import AbstractIpGeolocation
from dotenv import load_dotenv

load_dotenv()

IP_GEOLOCATION_API_KEY = os.getenv('IP_GEOLOCATION_API_KEY')

class TestAbstractIpGeolocation(unittest.TestCase):
    def __init__(self, *args, **kwargs):

        super(TestAbstractIpGeolocation, self).__init__(*args, **kwargs)

    def test_no_config(self):

        with self.assertRaises(Exception):
            # tests aren't always run in order, so make sure to
            # clear api_key
            AbstractIpGeolocation.api_key = None
            AbstractIpGeolocation.look_up("108.177.16.0")

    def test_config(self):

        AbstractIpGeolocation.configure(IP_GEOLOCATION_API_KEY)
        AbstractIpGeolocation.look_up("108.177.16.0")


if __name__ == '__main__':
    unittest.main()