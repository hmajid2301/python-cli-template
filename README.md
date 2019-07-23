# Cookie CutterP Python CLI.

A Cookie Cutter template for creating Python CLI scripts. 

**NOTE**: This project only supports Python3.

## Usage

First you will need to install cookiecutter, then "clone" the project using cookiecutter
Then fill in the form and your project will be ready to use. This project is supposed to be used with GitLab.

```python
pip install cookiecutter
# Via SSH
cookiecutter git@gitlab.com:hmajid2301/python-cli-cookiecutter.git
# Or via HTTPS
cookiecutter https://gitlab.com/hmajid2301/python-cli-cookiecutter.git
```

Then Install `pipenv` (globally) if you don't have it already. Run the pipenv command so that
pipenv will start to build your virtualenv and install your dependencies (including development dependencies).

```python
pip install pipenv
pipenv install --dev
```
