FROM python:3.11-slim
COPY . .
RUN pip install uv
RUN uv sync
CMD uv run ./src/train/train-job.py

