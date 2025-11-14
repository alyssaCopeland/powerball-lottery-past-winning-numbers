thonfrom datetime import datetime

def parse_date(date_str):
    """
    Parse a date string into a datetime object.
    :param date_str: Date string in 'YYYY-MM-DD' format
    :return: datetime object
    """
    try:
        return datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        print(f"Invalid date format: {date_str}")
        return None