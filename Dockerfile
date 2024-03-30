FROM python:3.11
ENV PYTHONUNBUFFERED=1
WORKDIR /new_blog
COPY requirements.txt /new_blog/
RUN pip install -r requirements.txt
COPY ./new_blog/settings.py /new_blog/new_blog/
COPY . /new_blog/
EXPOSE 8000
ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8000"]