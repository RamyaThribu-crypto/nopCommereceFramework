import logging


class logGen:
    logging.basicConfig(filename=".\\logs\\automation.log", format="%(asctime)s: %(levelname)s: %(message)s",
                        datefmt='%m/%d/%y %I:%M:%S %p')
    