import time
import logging

# Set up basic logging configuration
logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

# Counter for log print
log_counter = 0

def print_hi():
    logging.info(f'This is logging. Log count: {log_counter}')

if __name__ == '__main__':
    while True:
        log_counter += 1
        print_hi()
        if log_counter % 10 == 0:
            time.sleep(1)  # Sleep for 1 second between each print
