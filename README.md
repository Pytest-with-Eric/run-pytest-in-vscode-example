# Example code for the article **How to Run Pytest in VScode**

## Task

This repo contains the sample code for the article [How To Run Pytest In VS Code (Easy To Follow Step-By-Step Tutorial)](https://pytest-with-eric.com/introduction/how-to-run-pytest-in-vscode/)

## Code
The source code is a simple Python script that calculates the area of various shapes and can be found at `src/calculator.py`. 

Unit Tests can be found at `tests/unit/test_calculator.py`

## Requirements
* Python (3.8+)

Please create a virtual environment and activate it.

Install the dependencies via the `requirements.txt` file using 
```commandline
pip install -r requirements.txt
```
If you don't have Pip installed please follow instructions online on how to do it.

## How To Run the Unit Tests
To run the Unit Tests, from the root of the repo run
```commandline
pytest
```
or for more verbose output
```
pytest -v
```