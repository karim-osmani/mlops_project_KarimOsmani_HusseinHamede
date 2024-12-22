# tasks.py
from invoke import task
@task
def test(c):
 """Run all tests with pytest."""
 c.run("poetry run pytest tests/")
@task
def lint(c):
 """Run ruff to lint and format the code."""
 c.run("poetry run ruff check src/ tasks.py tests/")
@task
def format(c):
 """Run ruff to lint and format the code."""
 c.run("poetry run ruff format src/ tasks.py tests/")
@task
def type(c):
 """Run ruff to lint and format the code."""
 c.run("poetry run mypy src/ tasks.py tests/")
@task
def docs(c):
 """Generate HTML documentation with pdoc."""
 c.run("poetry run pdoc src/ml_data_pipeline --output-dir docs --html")
@task
def run(c, config="config/config_dev.yaml"):
 """Run the data pipeline with the specified configuration file."""
 c.run(f"poetry run ml-data-pipeline --config {config}")