FROM python:3.9.18-slim
COPY . .
RUN pip install -r requirements.txt
CMD ["streamlit", "run", "1_🏠_Home.py"]
