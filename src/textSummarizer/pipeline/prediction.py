from textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class PredictionPipeline:

    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path)

    def predict(self, text: str) -> str:
        inputs = self.tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
        
        summary_ids = self.model.generate(
            inputs["input_ids"],
            num_beams=8,
            max_length=128,
            length_penalty=0.8,
            early_stopping=True
        )
        
        output = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return output