# test_mintflux.py
"""
Tests for MintFlux module.
"""

import unittest
from mintflux import MintFlux

class TestMintFlux(unittest.TestCase):
    """Test cases for MintFlux class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MintFlux()
        self.assertIsInstance(instance, MintFlux)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MintFlux()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
