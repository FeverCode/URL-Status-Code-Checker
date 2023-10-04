import requests

def get_status_codes_from_csv_manual(csv_path):
    # Read the content of the CSV file manually
    with open(csv_path, 'r') as file:
        lines = file.readlines()

    # Extract URLs, skipping the header
    urls = [url.strip() for url in lines[1:]]

    # Fetch and print the status codes for each URL
    for url in urls:
        try:
            response = requests.get(url, timeout=10)  # Added a timeout for better error handling
            print(f"({response.status_code}) {url}")
        except requests.ConnectionError:
            print(f"(ConnectionError) Could not connect to {url}")
        except requests.Timeout:
            print(f"(TimeoutError) Request to {url} timed out")
        except requests.RequestException as e:
            print(f"(Error) {url}: {str(e)}")

if __name__ == "__main__":
    csv_path = "Task 2 - Intern.csv"
    get_status_codes_from_csv_manual(csv_path)
