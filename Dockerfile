FROM python:3.9-slim
RUN pip install flask requests
COPY app.py .
COPY templates templates
ENV FLASK_APP=app.py
EXPOSE 80
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]