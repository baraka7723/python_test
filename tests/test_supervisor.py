import unittest
from tests.models import Supervisor


class SupervisorTestCase(unittest.TestCase):

    def test_all_data(self):
        instance = Supervisor.sample()
        self.assertIsInstance(instance, Supervisor, 'this instance is not type of Supervisor')
        self.assertTrue(hasattr(instance, 'username'))
        self.assertTrue(hasattr(instance, 'password'))
        self.assertTrue(hasattr(instance, 'phone_number'))
