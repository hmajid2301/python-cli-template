# Cookie Cutter Python CLI.

A Cookie Cutter template for creating Python CLI scripts. 

**NOTE**: This project only supports Python3.

## Usage

First you will need to install cookiecutter, then "clone" the project using cookiecutter
Then fill in the form and your project will be ready to use. This project is supposed to be used with GitLab.

```bash
pip install cookiecutter
# Via SSH
cookiecutter git@gitlab.com:hmajid2301/python-cli-cookiecutter.git
# Or via HTTPS
cookiecutter https://gitlab.com/hmajid2301/python-cli-cookiecutter.git
```

Then install virtualenv (globally) if you need to, so we can create a virtualenv and install all of our python dependencies.
Then install the package locally

```bash
pip install virtualenv # Install virtualenv
virtualenv .venv # Create virtualenv
pip install -r requirements.txt # Install dependencies
pip install -e . # Install package locally
```

## Libraries

This template comes with the following libraries/packages ready to use.

- GitLab CI
- Black
- Flake8
- Docker
- Pytest
- Sphinx

## Changelog

You can find the [changelog here](https://gitlab.com/hmajid2301/python-cli-cookiecutter/blob/master/CHANGELOG.md).