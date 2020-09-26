FROM python:3.7-alpine
LABEL maintainer="Abu Darda"

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

# Set work directory
WORKDIR /app

# Copy project
COPY ./app /app

# Create user
RUN adduser -D user
RUN chown user:user -R /app/
USER user