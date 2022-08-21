from datetime import date, timedelta, datetime, time


def date_from_today(days: int) -> date:
    return date.today() + timedelta(days=days)


def get_time_from_isoformat(iso_datetime_str: str) -> time:
    iso_format = datetime.fromisoformat(iso_datetime_str)
    return iso_format.time()


def get_date_from_isoformat(iso_datetime_str: str) -> date:
    # "2022-08-10T06:15:00"
    iso_format = datetime.fromisoformat(iso_datetime_str)
    return iso_format.date()


def get_month_portuguese(month) -> str:
    month_dict = {
        1: "Janeiro",
        2: "Fevereiro",
        3: "Março",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro",
    }
    return month_dict[month]
