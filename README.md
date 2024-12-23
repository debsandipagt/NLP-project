## 2. Open VS Code in the folder `sensor-fault-detection`.

## 3. In VS Code, go to Settings -> Path -> Python: Conda Path and add `C:\Users\debsa\anaconda3\`.

## 4. In VS Code, go to Settings -> Path -> Python: Default Interpreter Path and add `C:\Users\debsa\anaconda3\python.exe`.

## 5. Open the with CMD terminal and write the command `git init` to initialize Git (Git is a version control system).

## 6. Create an environment with the command `conda create -p myenv python=3.8.16 -y`.

## 7. Activate the environment with `conda activate ./myenv/`.

## 8. Create a file named `requirements.txt`.

## 9. Run `pip install -r requirements.txt` to install all required libraries.

## 10. Create a `README.md` file to document all steps.

# Setup and Installation

- Create a `setup.py` file and use the command `python setup.py install` to install the package.
- Check installed packages using `pip list`.

## 11. Create a `src` folder, and within it, create an `__init__.py` file (this folder acts as a package since it contains `__init__.py`).

## 13. Create `constant` Folder in `src` and Initialize with `__init__.py`

- Set up a `constant` folder within the `src` directory.
- Inside the `constant` folder, create an `__init__.py` file to store project constants.

## 14. Component Creation

- **`components` Folder**: Structure the project into modular components.
  - **`__init__.py`**: Initialize the folder as a Python package for streamlined imports.
  - **`data_ingestion.py`**: Manage data loading and preprocessing tasks.
  - **`data_transformation.py`**: Oversee feature engineering and data transformation.
  - **`model_trainer.py`**: Include the logic for training the model.

## 25. Training Pipeline

- Create a `pipeline` folder within the `src` directory.
- In the `pipeline` folder, add a `train_pipeline.py` & `predict_pipeline.py` file.
- Implement the training and prediction pipeline code in `train_pipeline.py` & `predict_pipeline.py`

## 16. Exception Handling

- **Create an `exception.py` file**: 
  - **Location**: `src/exception.py`
  - **Purpose**: Manage custom exceptions for your project. Define classes to handle specific error cases and improve error reporting.

## 17. Logger File

- **Create a `logger.py` file**:
  - **Location**: `src/logger.py`
  - **Purpose**: Set up logging configurations for your project. Include functions to initialize and configure a logger to capture and record log messages.

## 18. Utilities Folder

- **Create a `utils` folder**: This folder will contain utility files and classes.
- **Inside the `utils` folder, create an `__init__.py` file**: Initialize the `utils` package by creating an empty `__init__.py` file.
- **Create a `main_utils.py` file**:
  - **Location**: `utils/main_utils.py`
  - **Purpose**: Define a utility class with methods for:
    - Reading YAML files.
    - Saving/loading objects using `pickle`.
    - Handling schema configurations.
    - Providing robust error handling with custom exceptions.