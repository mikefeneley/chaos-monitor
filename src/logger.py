import logging

class Logger:

    def __init__(self):
        logging.basicConfig(filename="test.log", level=logging.DEBUG)
        self.logger = logging.getLogger(__name__)
        pass

    def report_checksum_mismatch(self):
        self.logger.debug("Checksum mismatch")

    def report_checksum_match(self):
        self.logger.debug("Checksum match")

if __name__ == '__main__':
    log = Logger()
    log.report_checksum_mismatch()
