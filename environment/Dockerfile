FROM python:3

WORKDIR /workspace/environment
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /workspace
CMD [ "/bin/bash", "cp ./environment/secret.yml ./secret/secret.yml"]