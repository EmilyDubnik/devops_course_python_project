FROM python:3-alpine
ADD rest_app.py /
CMD ["python3", "./rest_app.py"]