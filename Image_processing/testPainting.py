#test cases for image processing driver
import unittest
from painting import Painting
import numpy as np

testEmpty3DNumpyArray = np.zeros((1,1,1), dtype=np.int32)

class TestPainting(unittest.TestCase):
    def test_painting_initialization(self):
        painting1 = Painting("test", "../ExamplePaintings/test.jpg")
        self.assertEqual(painting1.getImage(), testEmpty3DNumpyArray)
        self.assertEqual(painting1.getHSVImage(), testEmpty3DNumpyArray)
        self.assertEqual(painting1.getPropertiesList(), [0]*6)

    def test_painting_preprocessing(self):
        painting1 = Painting("test", "../ExamplePaintings/test.jpg")
        painting1.preprocessing()
        self.assertIsNot(painting1.getImage(), testEmpty3DNumpyArray)
        self.assertIsNot(painting1.getHSVImage(), testEmpty3DNumpyArray)
        self.assertEqual(painting1.getPropertiesList(), [0]*6)

    def test_painting_get_properties(self):
        painting1 = Painting("test", "../ExamplePaintings/test.jpg")
        painting1.preprocessing()
        painting1.calculateProperties()
        self.assertNotEqual(painting1.getPropertiesList(), [0]*6)
        print(painting1.getPropertiesList())

if __name__=='__main__':
    unittest.main()