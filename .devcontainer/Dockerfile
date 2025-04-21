FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

# Copy requirements.txt to a temp location to update the requirements.
COPY requirements.txt /tmp/pip-tmp/
RUN pip --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tm/

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>
