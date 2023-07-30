# Pytest Technical Interview Task

## Task

This repo contains the sample code for the [Technical Writer Interview Task](https://docs.google.com/document/d/10WtbnP1wnC_iWrqeu4Mitn5u9zljhmwhB7OH_ir4esw/edit?usp=sharing)

## Code
The source code is a simple Python script that calculates the area of various shapes and can be found at `src/area_calculator.py`. 

Unit Tests can be found at `tests/unit/test_area_calculator.py`

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