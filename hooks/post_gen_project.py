import distutils.spawn
import subprocess
import sys


def create_virtualenv():
    subprocess.check_call(["pip3", "install", "tox"])
    subprocess.check_call(["make", "install-venv"])


def git_init():
    git = distutils.spawn.find_executable("git")
    subprocess.check_call([str(git), "init"])
    subprocess.check_call([str(git), "add", "--all"])
    subprocess.check_call([str(git), "commit", "-m", "initial commit"])
    subprocess.check_call(
        ["git", "remote", "add", "origin", "{{cookiecutter.project_git_url}}.git"]
    )


if __name__ == "__main__":
    create_virtualenv()
    git_init()
