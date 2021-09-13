FROM python:3

WORKDIR /workspace/environment
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /workspace
RUN mkdir -p /secret
COPY secret.yml ./secret/

CMD [ "/bin/bash"]