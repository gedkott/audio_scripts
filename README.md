# pyenv - manage multiple versions of python on one machine

Install from [pyenv](https://github.com/pyenv/pyenv)

try in your termminal: `pyenv install 3.9.0`

# venv - virtual environments for each project

Comes built in with python3

try in your terminal in the root directory of your project: `python3 -m venv env`

then execute: `source env/bin/activate`

# pip - managing dependencies within a specific project

try in yoour terminal: `python3 -m pip install numpy`

update the requirement.txt with each change: `python3 -m pip freeze > requirements.txt`
