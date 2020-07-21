FROM python:3.8

WORKDIR /tmp/app

# Copy the project files to the WORKDIR
COPY rest_api_tests_hw/requirements.txt requirements.txt

# Setup the venv and install pyinstaller
RUN python -m venv /tmp/venv && \
    . /tmp/venv/bin/activate && \
    pip install -r requirements.txt
