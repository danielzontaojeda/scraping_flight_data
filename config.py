import json


def read_secrets(filename="secrets.json") -> dict:
    try:
        with open(filename, "r") as f:
            return json.loads(f.read())
    except FileNotFoundError:
        return {}


secrets = read_secrets()
AIRPORT_ORIGIN = "IGU"
FIREFOX_BINARY_LOCATION = r"C:\Program Files\Mozilla Firefox\firefox.exe"
DAYS_TO_SAVE_BACKUP = 30
CSV_BACKUP_FOLDER = secrets["CSV_BACKUP_FOLDER"]
EMAIL_LOGIN = secrets["EMAIL_LOGIN"]
EMAIL_PASSWORD = secrets["EMAIL_PASSWORD"]
