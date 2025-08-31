# Panduan Penggunaan Blackie Module

1. Pastikan `payloads.txt` sudah berisi payload SQL Injection yang ingin diuji.
2. Jalankan `main.py` untuk memulai scanning.
3. Hasil scanning akan ditampilkan di terminal.

Contoh:

```bash
python main.py


---

**Blackie/tests/test_scanner.py**

```python
import unittest
from core.scanner import Scanner

class TestScanner(unittest.TestCase):
    def test_load_payloads(self):
        scanner = Scanner()
        self.assertTrue(len(scanner.payloads) > 0)

    def test_run(self):
        scanner = Scanner()
        scanner.run()  # Pastikan tidak error saat run

if __name__ == '__main__':
    unittest.main()
