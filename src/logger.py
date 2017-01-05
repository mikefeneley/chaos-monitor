import logging

class Logger:

    def __init__(self, name=__name__):
        logging.basicConfig(filename="ChaosMonitor.log", level=logging.DEBUG)
        self.logger = logging.getLogger(name)

    def log_generic_message(self, message=""):
        self.logger.debug(message)
        self.logger.debug(__name__)
    def log_checksum_mismatch(self, filename="", old_checksum="", new_checksum=""):
        log_string = "Checksum mismatch: Filename: %s Old Checksum: %s  New Checksum: %s" %  (filename, old_checksum, new_checksum)
        self.logger.debug(log_string)

    def log_checksum_match(self, filename="", old_checksum="", new_checksum=""):
        log_string = "Checksum mismatch: Filename: %s Old Checksum: %s  New Checksum: %s" %  (filename, old_checksum, new_checksum)
        self.logger.debug(log_string)

if __name__ == '__main__':
    log = Logger()
    log.log_checksum_mismatch()
