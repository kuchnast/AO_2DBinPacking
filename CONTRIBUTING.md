#Contributing guide
### Main information if you would like to help in this project

### 1. Fork
> git clone **<FORK_GIT_REPO_PATH>**

### 2. Preparing local workspace
Make sure you have instaled python in version 3.10 or higher by typing:
> python --version


To start developing first download 'virtualenv' and create new virtual environment.
> pip install virtualenv
> 
> python -m virtualenv venv

Now activate it.
### Linux
> source venv/bin/activate
### Windows
>.\venv\Scripts\activate.bat

### Tips
Especially for Windows I recommend using PyCharm to be able easily run tests. Also, linux subsystem is a bit tricky so cmd is better option imo. In this case, you need to install python and git for windows to be able to build package. 

In PyCharm on Windows by default PowerShell is started as local terminal. I don't recommend using it. 

### What next
Install development packages.
> pip install -r dev-requirements.txt

In order to run pytest tests:
> pytest

In order to run formatting and syntax tests **(not necessary)**:
> tox -e black-check,mypy,flake8

To run script just type command:
> bin_packing_2d -i [input file or directory]

By default, all algorithms are launched. To run only specific algorithm type:
> bin_packing_2d -i [input file or directory] -a [algorithm_name]

Algorithm names can be found by typing ***bin_packing_2d -h***

To generate random input data run:
> generate_input_data
> 
 or
> 
> generate_plotting_data

Files will be saved to data/in or data/plot.

Before submitting automatically format source files:
>tox -e black

### 3. Adding new algorithm
1. Create new file in ***src/algorithms*** and new class inheriting from **OnlineAlgorithm** or **OfflineAlgorithm**
for example like in ***first_fit_algorithm.py***.

2. Override *\__init\__()*, *\_pack()* and run() methods.

3. Write a test in ***tests\algorithms*** to be able to check if it is working fine (look at first_fit_algorithm_test.py).
Remember to add ***test*** at file name and import pytest inside it.
To run only your test use pytest [test_path] or from IDE like PyCharm. 
Remember that you have to be in main project directory (e.g. for PyCharm you need to change it in run config).
4. Add your algorithm to dictionary at top of file ***src/main.py***.

From now, you should be able to run it from ***bin_packing_2d*** command.
