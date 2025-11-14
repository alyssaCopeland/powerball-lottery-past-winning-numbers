thonfrom fetcher.utils_date import parse_date

def parse_results(data):
    """
    Parse the raw Powerball data into a structured format.
    :param data: Raw Powerball data
    :return: List of parsed draw results
    """
    parsed_results = []

    for draw in data:
        draw_date = parse_date(draw.get("drawDate"))
        winning_numbers = draw.get("winningNumbers", "").split()
        power_play_multiplier = draw.get("powerPlayMultiplier", "1")
        
        parsed_results.append({
            "drawDate": draw_date.isoformat() if draw_date else None,
            "winningNumbers": winning_numbers,
            "powerPlayMultiplier": power_play_multiplier
        })
    
    return parsed_results