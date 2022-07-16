import requests
from bs4 import BeautifulSoup

url = "https://www.seatguru.com/airlines/LATAM_Chile/information.php"
string_to_delete = "'Seats:'", "'Economy'", "'LATAM+'", "'Premium Business'", "','", "'['", "']'"

def get_seatguru_html():
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    aircraft_seats = soup.findAll('div', class_='aircraft_seats')
    soup = BeautifulSoup(aircraft_seats.__str__(), 'html.parser')
    return soup

def parse_soup(soup):
    return [repr(string) for string in soup.stripped_strings]


def clean_soup(seats_info):
    to_delete = [i for i, string in enumerate(seats_info) if string in string_to_delete]
    to_delete.reverse()
    for i in to_delete:
        seats_info.pop(i)
    return seats_info


def create_dict(seats_info):
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


def get_capacity_for_model(airplane_model, capacity_dict):
    for k, v in capacity_dict.items():
        if str(airplane_model) in k:
            return v 
    return 0


def get_capacity_dict():
    soup = get_seatguru_html()
    seats_info = parse_soup(soup)
    seats_info = clean_soup(seats_info)
    capacity_dict = create_dict(seats_info)
    return capacity_dict


if __name__ == "__main__":
    capacity_dict = get_capacity_dict()
    print(get_capacity_for_model(320, capacity_dict))
    print(get_capacity_for_model(321, capacity_dict))
    print(get_capacity_for_model(319, capacity_dict))
    print(get_capacity_for_model(767, capacity_dict))
