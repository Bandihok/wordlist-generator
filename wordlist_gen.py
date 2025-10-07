#!/usr/bin/env python3
"""
Wordlist Generator with Configurable Suffixes and Logging

Generates a wordlist by combining base words (in multiple cases)
with provided suffixes, respecting a maximum password length.
"""

from pathlib import Path
import configparser
import argparse
import logging

# Load configuration
config = configparser.ConfigParser()
config.read('config.ini')

# Paths from config
LOG_DIR = config["Paths"]["logs_dir"]
WORDLIST_DIR = config["Paths"]["Wordlist_dir"]

# Ensure log directory exists
Path(LOG_DIR).mkdir(exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(Path(LOG_DIR) / "word_logs.log"),
        logging.StreamHandler()
    ]
)

def word_list_cong_gen(base, suffix, outputfile):
    """Generate wordlist from base words and suffixes."""
    logging.info("Beginning wordlist generation...")
    password = []
    base_word = []

    # Generate case variations
    for word in base:
        base_word.extend([word.upper(), word.lower(), word.capitalize()])

    max_len = int(config["Settings"]["len_password"])
    
    # Combine with suffixes
    for word in base_word:
        for suf in suffix:
            candidate = word + suf
            if len(candidate) <= max_len:
                password.append(candidate)
                logging.debug(f"Add password: {candidate}")

    # Remove duplicates
    password = list(set(password))
    logging.info(f"Was generated {len(password)} passwords~!")

    # Write to file
    try:
        output_path = Path(WORDLIST_DIR) / outputfile
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w") as f:
            for pwd in password:
                f.write(pwd + '\n')
        logging.info(f"File {output_path} was created!")
    except Exception as e:
        logging.error(f"Error writing file: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="--- Wordlist Generator with Config & Logging ---")
    parser.add_argument("--base", required=True, help="Comma-separated base words (e.g., 'admin,user')")
    parser.add_argument("--suffix", default=config["Settings"]["default_suffix"],
                        help="Comma-separated suffixes (default from config.ini)")
    parser.add_argument("--output", default="generated_wordlist.txt",
                        help="Output filename (saved in Wordlist_dir)")

    args = parser.parse_args()
    base = [w.strip() for w in args.base.split(",") if w.strip()]
    suffix = [w.strip() for w in args.suffix.split(",") if w.strip()]

    word_list_cong_gen(base, suffix, args.output)
