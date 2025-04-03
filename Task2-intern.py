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
            
            next(reader, None)

            
            for url in reader:
                try:
                    response = requests.get(url[0].strip(), timeout=5)
                    status_code = response.status_code
                    print(f"({status_code}) {url[0]}")
                except requests.exceptions.RequestException as e:
                    print(f"(ERROR) {url[0]} - {e}")
                    status_code = "ERROR"

                writer.writerow([status_code, url[0]])  
                
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

get_status_codes(file_path, output_file)
