from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.model_evaluation import ModelEvaluation

class ModelEvaluationPipeline:
    def __init__(self):
        self.config = ConfigurationManager()

    def main(self):
        try:
            model_evaluation_config = self.config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(model_evaluation_config)
            model_evaluation.evaluate()
        except Exception as e:
            raise e