# Installation Guide
To get started with the Gender Classifier project, please follow the steps below:

## Prerequisites
- Python 3.7 or higher
- pip package manager

## Step 1: Clone the Repository
```
git clone https://github.com/your-username/gender-classifier.git
```

## Step 2: Navigate to the Project Directory
```
cd gender-classifier
```

## Step 3: Create a Virtual Environment (optional)
It is recommended to create a virtual environment to isolate the project dependencies. You can use tools like `venv` or `conda` for this purpose.

### Using venv (built-in in Python 3):
```
python -m venv venv
```

### Activating the Virtual Environment
- For Windows:
```
venv\Scripts\activate
```
- For macOS/Linux:
```
source venv/bin/activate
```

## Step 4: Install Dependencies
```
pip install -r requirements.txt
```

## Step 5: Explore the Project
You're all set! You can now explore the Gender Classifier project. Here are a few files and directories you may find useful:

- `dataset/`: Directory to store the dataset of portrait images. Once you run the jupyter notebook the dataset directory will be formed.
- `notebooks/`: Jupyter notebooks for data exploration and model training. Run the notebook to train model and save it.
- `interface.py`: Run this script to launch the user interface for making gender predictions.

## Step 6: Run the User Interface
To use the Gender Classifier and make gender predictions on new images, run the following command:
```
python interface.py
```

Follow the instructions provided in the user interface to capture an image and obtain the predicted gender.

That's it! You have successfully installed the Gender Classifier project and are ready to start classifying genders in portrait images. Enjoy!
