# syntax=docker/dockerfile:1
FROM nvidia/cuda:11.0.3-base-ubuntu20.04

COPY requirements.txt requirements.txt
COPY . .
#install dependencies
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
#set work directory
WORKDIR /zephyr-7b-beta
EXPOSE 3330
# Run
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=3330"]
