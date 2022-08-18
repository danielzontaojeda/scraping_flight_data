import csv
import os

from scraping_flight_data.src.file_manager import output_excel
from scraping_flight_data.src.flight import flight


def insert_price(list_flights: list[flight.Flight], days: int) -> None:
    with open('saida.csv', newline='') as csvfile, open('saida_tmp.csv', 'a', newline='') as tmp_file:
        reader = csv.reader(csvfile)
        writer = csv.writer(tmp_file)
        writer.writerow(["sep=,"])
        writer.writerow(output_excel.HEADER)
        d = csv.DictReader(csvfile)
        d.fieldnames = 'region', 'state', 'city', 'airport_code', 'date', 'month', \
                       'year', 'airplane_number', 'airplane_model', 'company_name', \
                       'capacity', 'time_departure', 'time_arrival', 'stopover', \
                       'stopover_list', 'distance', 'price_30d', 'price_15d', 'price_1d',\
                       'price_med', 'yield_pax'
        # jumping sep and header lines
        next(d)
        next(d)
        for row in d:
            edit_row(row, list_flights, days)
            writer.writerow(row.values())
    os.remove('saida.csv')
    os.rename('saida_tmp.csv', 'saida.csv')

def edit_row(row: dict, list_flights: list[flight.Flight], days: int) -> None:
    for f in list_flights:
        if (row['date'] == f.date_departure.strftime("%Y-%m-%d") and
                row['airplane_number'] == str(f.airplane.number) and
                row['time_departure'] == f.time_departure.strftime("%H:%M:%S") and
                row['time_arrival'] == f.time_arrival.strftime("%H:%M:%S")):
            row[f'price_{days}d'] = f.price
            price_med = ((float(row['price_30d']) + float(row['price_15d']) + float(row['price_1d']))/3)
            row['price_med'] = f'{price_med:.2f}'