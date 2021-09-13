FROM python:3

WORKDIR /workspace
COPY . .
RUN pip install --no-cache-dir -r ./environment/requirements.txt && \
    apt-get update && apt-get install -y vim

COPY ./environment/secret.yml ./secret/

CMD [ "/bin/bash"]