FROM python:3-onbuild
MAINTAINER Aniruth Oblah "aniruth.oblah@gmail.com"
ENV APP_SETTINGS "config.DevelopmentConfig"
ENV DATABASE_URL "postgresql://localhost/rotten_reads"
COPY . /usr/src/app
CMD ["python","rottenreads.py"]
