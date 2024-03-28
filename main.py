from src.mlProject.logging import *
from src.mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>>>stage {STAGE_NAME} STARTED <<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>stage {STAGE_NAME} completed <<<<<")
except Exception as e:
    logger.exception(e)
    raise e
