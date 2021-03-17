FROM python:3.6-alpine

RUN apk update && \
    apk upgrade && \
    apk add git && \
    apk add build-base && \
    apk add perl
COPY requirements.txt ./

RUN python3.6 -m pip install -r requirements.txt -t .

COPY src/ ./
COPY libs/cloc/cloc-188.pl ./
COPY settings.json ./
# Command can be overwritten by providing a different command in the template directly.
CMD ["python3.6", "cloc.py"]