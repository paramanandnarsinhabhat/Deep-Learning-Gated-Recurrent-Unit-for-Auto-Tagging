

# Deep Learning Gated Recurrent Unit for Auto-Tagging

This project implements a Gated Recurrent Unit (GRU) based neural network for the purpose of automatically tagging text content. It focuses on processing and tagging Stack Overflow questions using a sequence model.

## Project Structure

- `data/`: Contains the dataset and zip files.
    - `archive (2).zip`: Compressed file with the datasets.
    - `unzipped_contents/`: Directory where the datasets are extracted and stored.
- `notebook/`: Jupyter notebooks for interactive development and experimentation.
    - `autotaggingsystemgru.ipynb`: Main notebook for the project.
- `source/`: Python scripts for the project.
    - `autotaggingsystemgru.py`: Main script for the project.
- `weights.best.hdf5`: Saved model weights after training.
- `requirements.txt`: Required libraries for the project.
- `LICENSE`: The license file for the project.
- `README.md`: Documentation and instructions for the project.

## Setup and Installation

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies:

```sh
pip install -r requirements.txt
```

4. Unzip the dataset:

```python
python -c "import zipfile; zipfile.ZipFile('data/archive (2).zip', 'r').extractall('data/unzipped_contents')"
```

## How to Use

You can run the Jupyter notebook for an interactive session:

```sh
jupyter notebook notebook/autotaggingsystemgru.ipynb
```

Or execute the Python script directly:

```sh
python source/autotaggingsystemgru.py
```

## Workflow

The project workflow is as follows:

1. **Load Data and Import Libraries**: Load necessary libraries and the dataset from the `data` directory.
2. **Text Cleaning**: Define and apply a function to clean the text data.
3. **Merge Tags with Questions**: Attach tags to questions for a combined dataset.
4. **Dataset Preparation**: Analyze and prepare the dataset for training.
5. **Text Representation**: Convert text data into a format suitable for training the GRU model.
6. **Model Building**: 
    - Define the GRU model architecture.
    - Train the model with the prepared dataset.
7. **Model Predictions**: Use the trained model to make predictions.
8. **Model Evaluation**: Evaluate the model's performance on the validation set.
9. **Inference**: Define a function to predict tags for new, unseen text data.

## Contributing

Feel free to fork the project, make changes, and submit a pull request if you have improvements to suggest.

## License

This project is open-sourced under the MIT License. See the [LICENSE](LICENSE) file for more details.

---


