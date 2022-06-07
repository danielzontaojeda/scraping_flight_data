class Airplane:
    def __init__(self, airplane_number, company, capacity):
        self.airplane_number = airplane_number
        self.model = ''
        self.company = company
        self.capacity = capacity


#TODO: use this class
class Airport:
    def __init__(self, code, name):
        self.code = code 
        self.name = name


class Flight:
    def __init__(self, flight_string):
        self.date = flight_string[0]
        self.code = flight_string[1].split(' ')
        self.time_departure = flight_string[2]
        self.time_arrival = flight_string[3]
        self.airport_code = flight_string[4]
        self.company_name = flight_string[5]
        self.airport_name = flight_string[6]
        self.airplane = Airplane(get_airplane_number(flight_string[1]),
                                 get_company_code(flight_string[1]), 'capacity')
        self.price1d = 0.0
        self.price15d = 0.0
        self.price30d = 0.0

    def __str__(self):
        return (f"{self.date},{self.airplane.company} {self.airplane.airplane_number},{self.time_departure},"
        f"{self.time_arrival},{self.airport_code},{self.company_name},{self.airport_name},"
        f"{self.price1d},{self.price15d},{self.price30d},{self.airplane.model}")

    def set_price1d(self, price):
        self.price1d = price

    def set_airplane_model(self, model):
        self.airplane.model = model

    def get_list(self) -> list:
        return [
            self.date,
            f"{self.airplane.company} {self.airplane.airplane_number}",
            self.time_departure,
            self.time_arrival,
            self.airport_code,
            self.company_name,
            self.airport_name,
            self.price1d,
            self.price15d,
            self.price30d,
            self.airplane.model
        ]


def get_company_code(string) -> str:
    code = string.split(' ')
    return code[0]


def get_airplane_number(string) -> str:
    code = string.split(' ')
    return code[1]