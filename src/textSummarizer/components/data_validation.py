
import os
from textSummarizer.entity import DataValidationConfig
from textSummarizer.logging import logger


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_files(self) -> bool:
        try:
            validation_status = True
            all_files = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))
            print(all_files)

            for file in self.config.ALL_REQUIRED_FILES:
                
                logger.info(f"Checking for file: {file}")
                if file not in all_files:
                    validation_status = False
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"File: {file} is not present.")
                else:
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"File: {file} is present.")
            return validation_status
        except Exception as e:
            return e