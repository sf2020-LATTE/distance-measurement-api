FROM python:3.7

# ローカルの/appを、Dockerコンテナ内の/appへコピー
COPY ./src /app

RUN pip install fastapi uvicorn
RUN pip install pytest
RUN pip install httpx

EXPOSE 80

CMD ["uvicorn", "--reload", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
