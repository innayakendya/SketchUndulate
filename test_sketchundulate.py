# test_sketchundulate.py
"""
Tests for SketchUndulate module.
"""

import unittest
from sketchundulate import SketchUndulate

class TestSketchUndulate(unittest.TestCase):
    """Test cases for SketchUndulate class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SketchUndulate()
        self.assertIsInstance(instance, SketchUndulate)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SketchUndulate()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
