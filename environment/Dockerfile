FROM python:3

WORKDIR /workspace/environment
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /workspace/secret
COPY secret.yml ./

WORKDIR /workspace
CMD [ "/bin/bash" ]