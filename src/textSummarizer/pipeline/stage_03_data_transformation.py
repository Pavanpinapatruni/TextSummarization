from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_transformation import DataTransformation

class DataTransformationPipeline:
    def __init__(self):
        self.config = ConfigurationManager()

    def main(self):
        try:
            data_transformation_config = self.config.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.convert()
        except Exception as e:
            raise e