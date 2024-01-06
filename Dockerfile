FROM python
WORKDIR /app
COPY . .
RUN pip install pipenv
RUN pipenv requirements > requirements.txt
RUN pip install -r requirements.txt
RUN apt update
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt install -y ./google-chrome-stable_current_amd64.deb
EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]