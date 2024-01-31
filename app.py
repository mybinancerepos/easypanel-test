import time, requests, logging

logging.basicConfig(level=logging.DEBUG, format='%(name)s - %(levelname)s - %(message)s')

def print_hi():
    logging.info('This is Log')
    print('This is Log')

if __name__ == '__main__':
    while True:
        print_hi()
        time.sleep(2)
        logging.info("*********************************************")
