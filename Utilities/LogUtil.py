import os
import logging

class Logger:
    def __init__(self, name, level):
        self.LogFileName = os.path.join(os.getcwd(), "Logs", f"log{time.strftime('%Y-%m-%d')}.txt")
        os.makedirs(os.path.dirname(self.LogFileName), exist_ok=True)  # Ensure the Logs directory exists
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        fh = logging.FileHandler(self.LogFileName, mode="a")
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
