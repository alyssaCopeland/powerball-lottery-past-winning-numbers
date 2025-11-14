thonimport requests
from datetime import datetime

BASE_URL = "https://api.powerball.com"

def fetch_powerball_data(start_date, end_date):
    """
    Fetch historical Powerball data between the provided date range.
    :param start_date: Starting date in 'YYYY-MM-DD' format
    :param end_date: Ending date in 'YYYY-MM-DD' format
    :return: A list of Powerball draw data
    """
    try:
        # Construct the URL with the date range
        url = f"{BASE_URL}/draws?startDate={start_date}&endDate={end_date}"
        
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes

        # Return the fetched data as a JSON object
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []