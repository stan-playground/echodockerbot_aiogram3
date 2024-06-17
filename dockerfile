FROM python:3.10-slim
ENV TOKEN='7412105233:AAEpjHUyIGMN7c6Tw5Zj8ejEcpuYsx7YSQo'
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "bot.py" ]

