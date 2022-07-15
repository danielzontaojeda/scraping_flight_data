from datetime import date, timedelta, datetime


def date_from_today(days: int):
	return date.today()+timedelta(days=days)

def get_time_from_isoformat(iso_datetime_str):
	iso_format = datetime.fromisoformat(iso_datetime_str)
	return iso_format.time()

def get_date_from_isoformat(iso_datetime_str):
	# "2022-08-10T06:15:00"
	iso_format = datetime.fromisoformat(iso_datetime_str)
	return iso_format.date()


