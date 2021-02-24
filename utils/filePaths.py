from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

UTILS_DIR = BASE_DIR/"utils"

DISBOT_DIR = BASE_DIR/"discord_bot"

TOKEN_PATH = DISBOT_DIR/"token"

FBCONFIG_PATH = UTILS_DIR/"firebase.json"