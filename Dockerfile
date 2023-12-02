# syntax=docker/dockerfile:1
FROM nvidia/cuda

# RUN apt-key del 7fa2af80
RUN apt-key adv --fetch-keys http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/3bf863cc.pub

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
