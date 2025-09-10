"""
log entries we can generate in test case but log file creation and format of log file are need to kept at one place
Type of logs warning logs debug logs info logs
utilities file ar mostly same for all projects
"""

import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(
                            filename=".\\Logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                            force=True

        )
        """ 
            ✅ You are not creating an object yourself.
            ✅ getLogger() gives you a logger instance (existing or newly created internally).
            ✅ logger is just a reference to that object.
        """
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger