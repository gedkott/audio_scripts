## Use (pyenv)[https://github.com/pyenv/pyenv]
pyenv install 3.9.0

python3 -m venv env
source env/bin/activate

python3 -m pip install numpy

python3 -m pip freeze > requirements.txt