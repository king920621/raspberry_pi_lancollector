FROM python:3.11-alpine
RUN apk add --no-cache iputils   # 提供 ping 命令
WORKDIR /app
COPY collect.py .
CMD ["python", "collect.py"]