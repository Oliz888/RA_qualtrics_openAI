### Project Structure

The following is an overview of the project's structure:


### Description of Key Files and Directories:

- **`.env`**: This file contains sensitive environment variables such as API keys.
- **`README.md`**: The documentation for the project, including instructions on how to set up and use the project.
- **`data/`**: Stores input and output data files.
  - `misinformation_comments.csv`: The input CSV file with comments to evaluate.
  - `output_file.csv`: The output CSV file after evaluation.
- **`notebooks/`**: Jupyter notebooks for running and testing API calls or any other experimental code.
  - `api_call_func.ipynb`: Notebook with the API call logic.
- **`logs/`**: Contains log files for tracking evaluation processes.
  - `evaluation_debug.log`: The log file to debug evaluations.
- **`src/`**: The source code for the project.
  - `__pycache__/`: Directory for Python cache files.
  - `imports.py`: Handles all imports for the project.
  - `main_execution.py`: Script that orchestrates the main logic execution.
  - `main_functions.py`: Contains core functions like `get_evaluation`, `plot_radar`, etc.
  - `main.py`: The main entry point that imports and runs the core functions.
- **`tests/`**: Directory reserved for unit and integration tests (optional or future use).

