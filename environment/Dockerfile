FROM python:3

WORKDIR /workspace/environment
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /workspace/secret
COPY secret.yml /workspace/secret/

WORKDIR /workspace
CMD [ "/bin/bash" ]