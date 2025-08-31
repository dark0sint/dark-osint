from .utils import load_payloads

class Scanner:
    def __init__(self):
        self.payloads = load_payloads()

    def run(self):
        print("Starting SQL Injection scan...")
        for payload in self.payloads:
            print(f"Testing payload: {payload}")
            # Simulasi scanning, implementasi nyata bisa ditambahkan
        print("Scan selesai.")
