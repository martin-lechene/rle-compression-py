import unittest
from compression import compress_rle, decompress_rle  # Assurez-vous que les fonctions sont dans compression.py

class TestCompressionRLE(unittest.TestCase):

    def test_basic_compression(self):
        self.assertEqual(compress_rle("AAAABBBCCDAA"), "A4B3C2D1A2")
        self.assertEqual(compress_rle("AAAB"), "A3B1")
        self.assertEqual(compress_rle("AABB"), "A2B2")
    
    def test_empty_string(self):
        self.assertEqual(compress_rle(""), "")
        self.assertEqual(decompress_rle(""), "")

    def test_single_character(self):
        self.assertEqual(compress_rle("A"), "A1")
        self.assertEqual(decompress_rle("A1"), "A")

    def test_no_repetition(self):
        self.assertEqual(compress_rle("ABCD"), "A1B1C1D1")
        self.assertEqual(decompress_rle("A1B1C1D1"), "ABCD")

    def test_decompression(self):
        self.assertEqual(decompress_rle("A4B3C2D1A2"), "AAAABBBCCDAA")
        self.assertEqual(decompress_rle("A3B1"), "AAAB")
        self.assertEqual(decompress_rle("A2B2"), "AABB")

    def test_compression_decompression(self):
        original = "AAABBBCCCCDDDAA"
        compressed = compress_rle(original)
        decompressed = decompress_rle(compressed)
        self.assertEqual(decompressed, original)

if __name__ == '__main__':
    unittest.main()
