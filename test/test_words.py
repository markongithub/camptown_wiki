from unittest import TestCase

from lib import words

class TestJoke(TestCase):
    def test_isCamptown(self):
        self.assertTrue(words.isCamptown('Pedro, Marshal of Navarre'))
        self.assertTrue(words.isCamptown('Savage 2: A Tortured Soul'))
        self.assertFalse(words.isCamptown('Single Payer Health Insurance'))
        self.assertFalse(words.isCamptown('Our Lady\'s Grammar School'))

    def test_getRhymingPart(self):
        self.assertEqual(
                'AA1 R',
                words.getRhymingPartIfCamptown('Pedro, Marshal of Navarre'))
        self.assertEqual(
                None,
                words.getRhymingPartIfCamptown('Single Payer Health Insurance'))

