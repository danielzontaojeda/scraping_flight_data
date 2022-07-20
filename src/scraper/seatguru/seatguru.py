from bs4 import BeautifulSoup
import requests


def get_seatguru_html(url):
    """Return soup from seatguru url with airplane capacity data."""
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    aircraft_seats = soup.findAll("div", class_="aircraft_seats")
    soup = BeautifulSoup(aircraft_seats.__str__(), "html.parser")
    return soup


def parse_soup(soup):
    """Transforms soup into a list."""
    return [repr(string) for string in soup.stripped_strings]


def clean_soup(seats_info, string_to_delete):
    """Remove itens from string_to_delete from seats_info."""
    to_delete = [i for i, string in enumerate(seats_info) if string in string_to_delete]
    to_delete.reverse()
    for i in to_delete:
        seats_info.pop(i)
    return seats_info


def create_dict(seats_info):
    """Organizes seats_info data into a dict:

    {plane_model: capacity}
    """
    currentKey = seats_info[0]
    capacity = {currentKey: 0}
    seats_info.pop(0)
    for string in seats_info:
        try:
            num = string.replace("'", "")
            capacity[currentKey] += int(num)
        except ValueError:
            currentKey = string
            capacity[currentKey] = 0
    return capacity
