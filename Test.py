import unittest
from Main import to_upper

class MytestCase(unittest.TestCase):
    def test_to_upper(self):
        name = "Aks"
        upper_name = to_upper(name)
        self.assertEqual(upper_name, 'aks')
        
if __name__ == "__main__":
    unittest.main()
