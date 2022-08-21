from scraping_flight_data.src.scraper.seatguru import seatguru

URL = "https://www.seatguru.com/airlines/GOL/information.php"
STRING_TO_DELETE = (
    "'Seats:'",
    "'Economy'",
    "'LATAM+'",
    "'Premium Economy'",
    "','",
    "'['",
    "']'",
)


def get_capacity_for_model(airplane_model: str, capacity_dict: dict) -> int:
    """Searches dict for partial match for airplane_model"""
    # gol website uses different code for the 737-700
    if airplane_model == "73G":
        airplane_model = "737"
    for k, v in capacity_dict.items():
        key = k[k.find("(") + 1 : k.find(")")]
        if str(airplane_model) in key:
            return v
    return 0


def get_capacity_dict() -> dict:
    """Return dict using gol airplane model as key and capacity as value."""
    soup = seatguru.get_seatguru_html(URL)
    seats_info = seatguru.parse_soup(soup)
    seats_info = seatguru.clean_soup(seats_info, STRING_TO_DELETE)
    capacity_dict = seatguru.create_dict(seats_info)
    return capacity_dict


if __name__ == "__main__":
    capacity_dict = get_capacity_dict()
    print(get_capacity_for_model("7M8", capacity_dict))
    print(get_capacity_for_model("73G", capacity_dict))
    print(get_capacity_for_model("738", capacity_dict))
    print(get_capacity_for_model("737", capacity_dict))
