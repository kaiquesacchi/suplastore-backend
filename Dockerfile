FROM alpine
WORKDIR /app
COPY . .

RUN apk add python3
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
CMD [ "python3", "run.py" ]
# Run with:
# docker run -it -p 5000:5000 -rm suplastorebackend:latest