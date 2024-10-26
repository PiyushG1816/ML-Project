import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name = 'Project1'

list_of_files=[
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitoring.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    'setup.py',
]

for paths in list_of_files:
    paths = Path(paths)
    filedir , filename = os.path.split(paths)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating {filedir} for {filename}")

    if(not os.path.exists(paths)) or (os.path.getsize(paths) == 0):
        with open(paths,'w') as f:
            pass
            logging.info(f"Creating empty file: {paths}")

    else:
        logging.info(f"{filename} already exists")