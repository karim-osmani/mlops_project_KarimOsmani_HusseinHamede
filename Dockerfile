FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Install Poetry and dependencies
RUN pip install --no-cache-dir pipx && \
    pipx install poetry && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Copy dependency files first to leverage Docker caching
COPY poetry.lock pyproject.toml /app/

# Install dependencies with Poetry
RUN poetry install --no-root --no-cache

# Copy the rest of the project files
COPY . /app

# Copy the data file into the container
COPY data/iphone.csv /app/data/iphone.csv

# Expose the FastAPI port
EXPOSE 8000

# Command to run the FastAPI application
CMD ["poetry", "run", "uvicorn", "src.project.main:app", "--host", "0.0.0.0", "--port", "8000"]
