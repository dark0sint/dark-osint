import os

def load_payloads():
    payloads_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'payloads.txt')
    try:
        with open(payloads_file, 'r') as f:
            payloads = [line.strip() for line in f if line.strip()]
        return payloads
    except FileNotFoundError:
        print("File payloads.txt tidak ditemukan.")
        return []
