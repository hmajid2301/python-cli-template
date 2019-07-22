FROM python:alpine{{ cookiecutter.python_version }}
LABEL MAINTAINER="{{ cookiecutter.author }} {{ cookiecutter.author_email }}"

COPY dist ./dist/
RUN pip install dist/*
