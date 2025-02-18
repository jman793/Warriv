FROM python:3

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

# CMD ["sleep", "infinity"]
CMD ["python", "/src/app/bot_runner.py"]
