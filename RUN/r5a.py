#!/usr/bin/env python3

# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "requests",
#     "rich",
# ]
# ///

import logging
import subprocess
from rich import print
from rich.logging import RichHandler

def main() -> None:
    print("R4 Checking CargoVersion!")
    cargz()

def cargz() -> None:
    # Set up logging
    logging.basicConfig(
        level="INFO",
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True)]
    )

    try:
        result = subprocess.run(["cargo", "--version"], capture_output=True, text=True)
        result.check_returncode()  # Raise an exception if the command failed
        logging.info(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        logging.error(f"Error: {e}")
        logging.error(f"Command output: {e.output.strip()}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
