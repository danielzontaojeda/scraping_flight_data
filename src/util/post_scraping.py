import shutil
from datetime import date, timedelta, datetime
from pathlib import Path

from scraping_flight_data.config import CSV_BACKUP_FOLDER, DAYS_TO_SAVE_BACKUP


def create_csv_backup():
    today = date.today().strftime("%Y-%m-%d")
    shutil.copy("saida.csv", rf"{CSV_BACKUP_FOLDER}\{today}.csv")


def delete_old_backup():
    backups = Path(CSV_BACKUP_FOLDER)
    date_to_delete = date.today() - timedelta(days=DAYS_TO_SAVE_BACKUP)
    for backup in backups.iterdir():
        date_backup = datetime.strptime(backup.name, "%Y-%m-%d.csv").date()
        if date_backup < date_to_delete:
            Path.unlink(backup)


def delete_old_log():
    logs = Path("./logs")
    date_to_delete = date.today() - timedelta(days=DAYS_TO_SAVE_BACKUP)
    for log in logs.iterdir():
        date_log = datetime.strptime(log.name, "%Y-%m-%d.log").date()
        if date_log < date_to_delete:
            Path.unlink(log)
