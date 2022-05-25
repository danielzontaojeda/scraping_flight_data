from scraping_flight_data.util import data_util


def main():
    if data_util.is_time(" CWB"):
        print("y")
        print(data_util.is_time(("04:00 cwb")))
    else:
        print("n")


if __name__ == "__main__":
    main()
