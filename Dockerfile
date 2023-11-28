FROM python:3.9.18-slim
WORKDIR /app
COPY . .
RUN pip3 install -r requirements.txt
CMD ["streamlit", "run", "1_🏠_Home.py"]
