thonimport json
from fetcher.powerball_client import fetch_powerball_data
from processors.result_parser import parse_results

def main():
    # Define date range for fetching Powerball data (this can be modified as needed)
    start_date = "2024-01-01"
    end_date = "2024-12-31"

    # Fetch the data
    data = fetch_powerball_data(start_date, end_date)
    
    # Parse the fetched data
    parsed_data = parse_results(data)

    # Output the parsed data
    with open('data/sample_output.json', 'w') as f:
        json.dump(parsed_data, f, indent=4)
    
    print("Powerball data saved to 'data/sample_output.json'")

if __name__ == "__main__":
    main()