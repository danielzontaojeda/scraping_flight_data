from scraping_flight_data.src.scraper.seatguru import seatguru

url = "https://www.seatguru.com/airlines/GOL/information.php"
string_to_delete = (
    "'Seats:'",
    "'Economy'",
    "'LATAM+'",
    "'Premium Economy'",
    "','",
    "'['",
    "']'",
)


def get_capacity_for_model(airplane_model, capacity_dict):
    """Searches dict for partial match for airplane_model"""
    # gol website uses different code for the 737-700
    if airplane_model == "73G":
        airplane_model = "737"
    for k, v in capacity_dict.items():
        key = k[k.find("(") + 1 : k.find(")")]
        if str(airplane_model) in key:
            return v
    return 0


def get_capacity_dict():
    soup = seatguru.get_seatguru_html(url)
    seats_info = seatguru.parse_soup(soup)
    seats_info = seatguru.clean_soup(seats_info, string_to_delete)
    capacity_dict = seatguru.create_dict(seats_info)
    return capacity_dict


if __name__ == "__main__":
    capacity_dict = get_capacity_dict()
    print(get_capacity_for_model("7M8", capacity_dict))
    print(get_capacity_for_model("73G", capacity_dict))
    print(get_capacity_for_model("738", capacity_dict))
    print(get_capacity_for_model("737", capacity_dict))
