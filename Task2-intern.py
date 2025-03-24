import requests
import csv

def get_status_codes(file_path):
    try:
        with open(file_path, 'r', newline='', encoding='utf-8-sig') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    url = row[0].strip()
                    if url.lower() == "urls":  
                        continue
                    try:
                        response = requests.get(url, timeout=5)
                        print(f"({response.status_code}) {url}")
                    except requests.exceptions.RequestException as e:
                        print(f"(ERROR) {url} - {e}")
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")


file_path = "Task2intern.csv"  
get_status_codes(file_path)
