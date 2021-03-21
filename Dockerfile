
# pull official base image
FROM python:3.8

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install dependencies
RUN pip install --upgrade cython
RUN pip install --upgrade pip
COPY Pipfile Pipfile.lock /usr/src/app/
COPY ./requirements.txt .
RUN pip install -r requirements.txt


# copy project
COPY . .
