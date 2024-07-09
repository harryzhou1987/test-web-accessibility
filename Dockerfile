FROM python:alpine3.19

RUN pip install requests==2.31.0

COPY executable.py /executable.py

ENTRYPOINT ["python","/executable.py"]
