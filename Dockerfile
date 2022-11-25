FROM python
WORKDIR /app
COPY . .
ENTRYPOINT ["python3"]
CMD ["main.py"]
