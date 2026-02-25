import os
from textSummarizer.logging import logger
from textSummarizer.entity import DataTransformationConfig
from transformers import AutoTokenizer
from datasets import load_from_disk

class DataTransformation:
    
    def __init__(self, config : DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_name)

    def convert_examples_to_features(self, example_batch):

        inputs = self.tokenizer(example_batch["dialogue"], max_length=1024, truncation=True)

        labels = self.tokenizer(example_batch["summary"], max_length=128, truncation=True)

        return {
            "input_ids": inputs["input_ids"],
            "attention_mask": inputs["attention_mask"],
            "labels": labels["input_ids"],
        }
    
    def convert(self):
        logger.info("Loading dataset from disk.")
        dataset = load_from_disk(self.config.data_path)

        logger.info("Converting examples to features.")
        dataset_pt = dataset.map(self.convert_examples_to_features, batched=True)

        logger.info("Saving transformed dataset to disk.")
        dataset_pt.save_to_disk(os.path.join(self.config.root_dir, "transformed_dataset"))