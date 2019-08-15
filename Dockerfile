FROM python:alpine3.10

WORKDIR /pychooseu

ADD csvdata/ csvdata/

COPY pychooseu.py .

ENTRYPOINT ["python","pychooseu.py"]
