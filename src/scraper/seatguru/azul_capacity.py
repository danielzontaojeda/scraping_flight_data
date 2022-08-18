import re

from scraping_flight_data.src.scraper.seatguru import seatguru

URL = "https://www.seatguru.com/airlines/Azul_Airlines/information.php"
STRING_TO_DELETE = (
    "'Seats:'",
    "'Economy'",
    "'Economy Xtra'",
    "'Premium Economy'",
    "'Azul Space'",
    "'Business'",
    "','",
    "'['",
    "']'",
)


def get_capacity_for_model(airplane_model, capacity_dict):
    """Searches dict for partial match for airplane_model"""
    pattern = r"^.*?(\d{3}).*$"
    for k, v in capacity_dict.items():
        match = re.search(pattern, airplane_model)
        if match:
            if match.group(1) in k:
                return v
        elif airplane_model in k:
            return v
    return 0


def get_capacity_dict():
    soup = seatguru.get_seatguru_html(URL)
    seats_info = seatguru.parse_soup(soup)
    seats_info = seatguru.clean_soup(seats_info, STRING_TO_DELETE)
    capacity_dict = seatguru.create_dict(seats_info)
    return capacity_dict


if __name__ == "__main__":
    capacity_dict = get_capacity_dict()
    print(get_capacity_for_model("Airbus A320 neo", capacity_dict))
    print(get_capacity_for_model("Embraer 195", capacity_dict))
    print(get_capacity_for_model("ATR", capacity_dict))
