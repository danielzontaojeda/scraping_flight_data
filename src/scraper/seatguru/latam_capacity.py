from scraping_flight_data.src.scraper.seatguru import seatguru

url = "https://www.seatguru.com/airlines/LATAM_Chile/information.php"
string_to_delete = (
    "'Seats:'",
    "'Economy'",
    "'LATAM+'",
    "'Premium Business'",
    "','",
    "'['",
    "']'",
)


def get_capacity_for_model(airplane_model: str, capacity_dict: dict) -> int:
    """Searches dict for partial match for airplane_model"""
    for k, v in capacity_dict.items():
        if str(airplane_model) in k:
            return v
    return 0


def get_capacity_dict() -> dict:
    """Return dict using latam airplane model as key and capacity as value."""
    soup = seatguru.get_seatguru_html(url)
    seats_info = seatguru.parse_soup(soup)
    seats_info = seatguru.clean_soup(seats_info, string_to_delete)
    capacity_dict = seatguru.create_dict(seats_info)
    return capacity_dict


if __name__ == "__main__":
    capacity_dict = get_capacity_dict()
    print(get_capacity_for_model(320, capacity_dict))
    print(get_capacity_for_model(321, capacity_dict))
    print(get_capacity_for_model(319, capacity_dict))
    print(get_capacity_for_model(767, capacity_dict))
