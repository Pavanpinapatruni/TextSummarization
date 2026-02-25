from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.model_trainer import ModelTrainer

class ModelTrainerPipeline:
    def __init__(self):
        self.config = ConfigurationManager()

    def main(self):
        try:
            model_trainer_config = self.config.get_model_trainer_config()
            model_trainer = ModelTrainer(model_trainer_config)
            model_trainer.train()
        except Exception as e:
            raise e