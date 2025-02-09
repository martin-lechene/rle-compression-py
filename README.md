# RLE Compression Library

A simple Python implementation of **Run-Length Encoding (RLE)** for data compression and decompression.

## 📌 Features
- Lossless compression algorithm.
- Efficient for data with repeated characters.
- Simple implementation with Python.
- Includes unit tests for reliability.

## 🚀 Installation
Clone this repository and navigate to the project directory:
```bash
git clone https://github.com/martin-lechene/rle-compression-py.git
cd rle-compression
```

## 🛠 Usage
### Import the functions:
```python
from compression import compress_rle, decompress_rle

data = "AAAABBBCCDAA"
compressed = compress_rle(data)
decompressed = decompress_rle(compressed)

print(f"Original: {data}")
print(f"Compressed: {compressed}")
print(f"Decompressed: {decompressed}")

assert decompressed == data  # Ensures lossless compression
```

### 📝 Example
```python
data = "AAABBBCCCCDDDAA"
compressed = compress_rle(data)  # Output: "A3B3C4D3A2"
decompressed = decompress_rle(compressed)  # Output: "AAABBBCCCCDDDAA"
```

## 🧪 Running Unit Tests
This project includes unit tests using `unittest`. To run them:
```bash
python -m unittest test_compression.py
```

## 📖 How RLE Works
**Run-Length Encoding (RLE)** replaces sequences of repeated characters with a single character followed by the count:
```
Original:   AAAABBBCCDAA
Compressed: A4B3C2D1A2
```
This works well for data with many repeated characters but is inefficient for non-repetitive text.

## 📌 Limitations
- Inefficient for non-repetitive data (e.g., `"ABCD"` → `"A1B1C1D1"` increases size).
- Only works with character-based sequences.

## 📜 License
This project is licensed under the MIT License.

---

Developed by **DOG&DEV** 🚀