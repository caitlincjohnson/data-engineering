# Data Engineering
This is my catch-all repository for code snippets, projects, and all things relating to data engineering.

Main concepts included in this repository include side projects for the following:
- Apache Airflow
- Apache Spark
- Intermediate to Advanced Python exercises

## Installation/Usage

This repository leverages pre-commit as an attempt to improve readabilty of the code. To get started with this, after cloning the respository, execute the following command:

`pip install pre-commit`

Run the following to set up the git hook scripts:

`run pre-commit install`

Now you have the option to run pre-commit on all files, which can be done as such:

`pre-commit run --all-files`

Or you can select a file to run it against:

`pre-commit run path/to/file.py`
