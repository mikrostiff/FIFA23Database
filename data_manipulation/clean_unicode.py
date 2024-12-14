import unicodedata
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import *

def clean_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8-sig') as file:
        content = file.read()
    
    # Normalize and clean unicode characters
    cleaned = unicodedata.normalize('NFKD', content)
    # Remove remaining non-ASCII chars
    cleaned = cleaned.encode('ascii', 'ignore').decode('ascii')
    
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(cleaned)

# Usage
clean_file(PLAYER_DATA_PATH, 'cleaned_file.csv')
