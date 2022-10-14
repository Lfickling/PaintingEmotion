#test cases for image processing driver
import unittest
from painting import Painting

class TestPainting(unittest.TestCase):
    def test_painting_initialization(self):
        painting1 = Painting("test", "PaintingEmotion/ExamplePaintings/test.jpg")
        self.assertEqual(painting1.getImage(), [[[]]])
        self.assertEqual(painting1.getHSVImage(), [[[]]])
        self.assertEqual(painting1.getPropertiesList(), [0]*6)

    def test_painting_preprocessing(self):
        painting1 = Painting("test", "PaintingEmotion/ExamplePaintings/test.jpg")
        painting1.preprocessing()
        self.assertIsNot(painting1.getImage(), [[[]]])
        self.assertIsNot(painting1.getHSVImage(), [[[]]])
        self.assertEqual(painting1.getPropertiesList(), [0]*6)

    def test_painting_get_properties(self):
        painting1 = Painting("test", "PaintingEmotion/ExamplePaintings/test.jpg")
        painting1.preprocessing()
        painting1.calculateProperties()
        self.assertNotEqual(painting1.getPropertiesList(), [0]*6)

if __name__=='__main__':
    unittest.main()