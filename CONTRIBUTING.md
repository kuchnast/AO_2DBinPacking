#Contributing guide
### Main information if you would like to help in this project

### 1. Fork
> git clone **<FORK_GIT_REPO_PATH>**

### 2. Preparing local workspace

To start developing first download 'virtualenv' and create new virtual environment.
> pip install virtualenv
> 
> python -m virtualenv venv

Now activate it.
### Linux
> source venv/bin/activate
### Windows
>.\venv\Scripts\activate.bat

Install development packages.
> pip install -r dev-requirements.txt

In order to run tests:
> tox -e black-check,mypy,py3,flake8

Before submitting pull request to automatically format source files:
>tox -e black