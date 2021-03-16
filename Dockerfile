FROM public.ecr.aws/lambda/python:3.7
COPY requirements.txt ./

RUN python3.7 -m pip install -r requirements.txt -t .

COPY src/ ./
COPY config.json ./
# Command can be overwritten by providing a different command in the template directly.
CMD ["bash"]