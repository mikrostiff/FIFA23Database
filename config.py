import os
import sys

# Get application directory
if getattr(sys, 'frozen', False):
    APP_DIR = os.path.dirname(sys.executable)
else:
    APP_DIR = os.path.dirname(os.path.abspath(__file__))

# Set data directory in program folder
DATA_DIR = os.path.join(APP_DIR, 'data')
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Global file paths
PLAYER_DATA_PATH = os.path.join(DATA_DIR, 'male_players.csv')
RAW_DATA_PATH = os.path.join(DATA_DIR, 'male_players.csv')
