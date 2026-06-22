# test_apexdrop.py
"""
Tests for ApexDrop module.
"""

import unittest
from apexdrop import ApexDrop

class TestApexDrop(unittest.TestCase):
    """Test cases for ApexDrop class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ApexDrop()
        self.assertIsInstance(instance, ApexDrop)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ApexDrop()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
