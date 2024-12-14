import pandas as pd
import os
import sys
from ..config import *

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
PLAYER_DATA_PATH = os.path.join(DATA_DIR, 'male_players_fifa23.csv')
RAW_DATA_PATH = os.path.join(DATA_DIR, 'male_players.csv')

def split_csv_by_year():
    # Read the main CSV file
    df = pd.read_csv(RAW_DATA_PATH)

    # Get unique FIFA versions
    versions = df['fifa_version'].unique()

    # Create separate files for each version
    for version in versions:
        version_df = df[df['fifa_version'] == version]
        output_filename = f'male_players_fifa{version}.csv'
        version_df.to_csv(output_filename, index=False)
        print(f"FIFA {version}: {len(version_df)} players")

def reduce_csv_size():
    # Read the CSV file
    df = pd.read_csv(PLAYER_DATA_PATH)

    # Calculate half the length
    half_length = len(df) // 2

    # Keep only first half of the rows
    df_half = df.iloc[:half_length]

    # Save to new CSV
    df_half.to_csv(os.path.join(DATA_DIR, 'male_players_fifa23_half.csv'), index=False)


if __name__ == '__main__':
    reduce_csv_size()