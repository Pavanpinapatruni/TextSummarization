from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_ingestion import DataIngestion
from textSummarizer.logging import logger

class DataIngestionPipeline:
    def __init__(self):
        self.config = ConfigurationManager()

    def main(self):
        try:
            data_ingestion_config = self.config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip()
        except Exception as e:
            logger.error(f"Error in data ingestion pipeline: {e}")
            raise e