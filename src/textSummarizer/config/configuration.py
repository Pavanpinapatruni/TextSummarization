from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_directories
from textSummarizer.entity import (DataIngestionConfig,
                                   DataTransformationConfig,
                                   DataValidationConfig,
                                   ModelTrainerConfig)


class ConfigurationManager:
    def __init__(
        self,
        config_file_path: Path = CONFIG_FILE_PATH,
        params_file_path: Path = PARAMS_FILE_PATH,
    ):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        # since it is configbox output, we can call it as 
        # config.artifacts_root instead of self.config["artifacts_root"]
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_URL=config.source_URL,
            local_data_file=Path(config.local_data_file),
            unzip_dir=Path(config.unzip_dir),
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES
        )

        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        data_transformation_config = self.config.data_transformation

        create_directories([data_transformation_config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir = data_transformation_config.root_dir,
            data_path = data_transformation_config.data_path,
            tokenizer_name = data_transformation_config.tokenizer_name
        )
        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        model_trainer_config = self.config.model_trainer

        create_directories([model_trainer_config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir = Path(model_trainer_config.root_dir),
            data_path = Path(model_trainer_config.data_path),
            model_ckpt = model_trainer_config.model_ckpt,
            num_train_epochs = self.params.TrainingArguments.num_train_epochs,
            warmup_steps = self.params.TrainingArguments.warmup_steps,
            per_device_train_batch_size = self.params.TrainingArguments.per_device_train_batch_size,
            weight_decay = self.params.TrainingArguments.weight_decay,
            logging_steps = self.params.TrainingArguments.logging_steps,
            evaluation_strategy = self.params.TrainingArguments.evaluation_strategy,
            eval_steps = self.params.TrainingArguments.eval_steps,
            save_steps = self.params.TrainingArguments.save_steps,
            gradient_accumulation_steps = self.params.TrainingArguments.gradient_accumulation_steps
        )

        return model_trainer_config