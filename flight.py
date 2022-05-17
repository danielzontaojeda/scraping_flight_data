class Airplane:
    def __init__(self, airplane_number, model, company, capacity):
        self.airplane_number = airplane_number
        self.model = model
        self.company = company
        self.capacity = capacity


def get_company_code(string):
    code = string.split(' ')
    return code[0]


def get_airplane_number(string):
    code = string.split(' ')
    return code[1]


class Flight:
    def __init__(self, flight_string):
        self.date = flight_string[0]
        self.code = flight_string[1].split(' ')
        self.time_departure = flight_string[2]
        self.time_arrival = flight_string[3]
        self.airport_code = flight_string[4]
        self.company_name = flight_string[5]
        self.airport_name = flight_string[6]
        self.airplane = Airplane(get_airplane_number(flight_string[1]), 'model',
                                 get_company_code(flight_string[1]), 'capacity')

