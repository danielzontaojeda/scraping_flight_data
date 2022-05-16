class Airplane:
    def __init__(self, flight_number, model, company, capacity):
        self.flight_number = flight_number
        self.model = model
        self.company = company
        self.capacity = capacity


class Flight:
    def __init__(self, date, plane_model, time_departure, time_arrival, departure_airport, company):
        self.date = date
        self.plane_model = plane_model.split(' ')
        self.plane = Airplane(self.plane_model[1], 'E195', company, 100) #TODO: model, capacity
        self.time_departure = time_departure
        self.time_arrival = time_arrival
        self.departure_airport = departure_airport
        self.company = company

