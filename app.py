import time
import logging

# Set up basic logging configuration
logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

# Counter for log print
log_counter = 0

def print_hi():
    global log_counter
    log_counter += 1
    logging.info(f'This is logging. Log count: {log_counter}')
    print(f'This is print. Log count: {log_counter}')

if __name__ == '__main__':
    while True:
        print_hi()
        time.sleep(2)
