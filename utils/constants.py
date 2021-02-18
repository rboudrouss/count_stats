from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR/"data"

HISTORY_FILE = DATA_DIR/"history.json"

USERS_FILE = DATA_DIR/"users.json"

COUNT_FILE = DATA_DIR/"count.json"