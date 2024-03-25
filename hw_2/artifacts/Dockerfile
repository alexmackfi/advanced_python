FROM python:3.8-slim

WORKDIR /app

COPY ./src ./src

RUN apt-get update && apt-get install -y \
    texlive-latex-base \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -i https://test.pypi.org/simple/ latex-package-alexmackfi

