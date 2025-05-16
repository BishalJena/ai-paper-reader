FROM python:3.11-slim AS backend

WORKDIR /app
COPY backend/ ./backend/
COPY notebooks/ ./notebooks/
RUN pip install --upgrade pip && pip install -r backend/requirements.txt

FROM nginx:alpine AS frontend
COPY frontend/static/ /usr/share/nginx/html/

FROM backend AS final
COPY --from=frontend /usr/share/nginx/html /app/static
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
