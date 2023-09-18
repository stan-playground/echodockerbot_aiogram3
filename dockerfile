FROM python:3.11-slim
ENV TOKEN='your_token'
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "bot.py" ]