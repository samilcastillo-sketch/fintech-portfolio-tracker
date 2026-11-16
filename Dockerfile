FROM python:3.13-slim

WORKDIR /app

COPY src/ /app/src/

ENV PORT=5004 \
    HOST=0.0.0.0

EXPOSE 5004

CMD ["python3", "-m", "src.server"]
