from setuptools import find_packages
from setuptools import setup

setup(
    name="{{ cookiecutter.package_name }}",
    version="{{ cookiecutter.version }} ",
    description="{{ cookiecutter.project_short_description }}",
    long_description=open("README.rst").read(),
    long_description_content_type="text/x-rst",
    author="{{ cookiecutter.author }}",
    author_email="{{ cookiecutter.author_email }}",
    keywords="{{ cookiecutter.keywords }}",
    license="Apache License",
    url="{{ cookiecutter.project_git_url }}",
    python_requires="~={{ cookiecutter.python_version }}",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    zip_safe=False,
    include_package_data=True,
    install_requires=["click>=7.0"],
    entry_points={"console_scripts": ["{{ cookiecutter.module_name }} = {{ cookiecutter.module_name }}.cli:cli"]},
    classifiers=[
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
