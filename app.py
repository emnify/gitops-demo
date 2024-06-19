import os
import time
from datetime import datetime
import sys

def main():
    message = os.getenv('MESSAGE', 'No message set via environment variable!')
    while True:
        print(f'[{datetime.now()}] - {message}')
        sys.stdout.flush()
        time.sleep(1)

if __name__ == "__main__":
    main()