
import logging
import mylib

def main():
    logger = logging.getLogger(__name__)
    logging.basicConfig(filename='myapp.log',
                        format="%(levelname)s:%(name)s:%(asctime)s - %(message)s",
                        level=logging.INFO, datefmt='%m/%d/%Y %I:%M:%S %p')

    logging.info('Started')
    mylib.do_something()
    logging.info('Finished')


if __name__ == "__main__":
    main()