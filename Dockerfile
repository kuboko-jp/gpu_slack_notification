FROM python:3

WORKDIR /workspace
COPY . .
RUN pip install --no-cache-dir -r ./environment/requirements.txt

COPY ./environment/secret.yml ./secret/

CMD [ "/bin/bash"]