import requests
import csv

output_file = "output.csv"
file_path = "Task2intern.csv"

def get_status_codes(file_path, output_file):
    try:
        with open(file_path, 'r', newline='', encoding='utf-8-sig') as file, open(output_file, mode='w', newline='', encoding='utf-8') as output_f:
            reader = csv.reader(file)
            writer = csv.writer(output_f)
            writer.writerow(["Status Code", "URL"]) 
            next(reader, None)  # Skip the header row

            for row in reader:
                if row: # Ensure row is not empty
                    url = row[0].strip()  # Extract URL from list
                    try:
                        response = requests.get(url, timeout=5)
                        status_code = response.status_code
                        print(f"({status_code}) {url}")
                    except requests.exceptions.RequestException as e:
                        print(f"(ERROR) {url} - {e}")
                        status_code = "ERROR"

                    writer.writerow([status_code, url]) 
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

get_status_codes(file_path, output_file)
