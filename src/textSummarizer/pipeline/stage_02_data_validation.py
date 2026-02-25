from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_validation import DataValidation
from textSummarizer.logging import logger

class DataValidationPipeline:
    def __init__(self):
        self.config = ConfigurationManager()

    def main(self):
        try:
            data_validation_config = self.config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            validation_status = data_validation.validate_all_files()
            if validation_status:
                logger.info("All required files are present. Data validation successful.")
            else:
                logger.error("Data validation failed. Some required files are missing.")
        except Exception as e:
            logger.error(f"Error in data validation pipeline: {e}")
            raise e