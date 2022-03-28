FROM ubuntu
  
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN apt install -y python3-dev python3-pip  python3-opencv vim-tiny  libopencv-dev
RUN pip3 install Cython
RUN pip3 install numpy
RUN pip3 install paho-mqtt
RUN pip3 install boto3

WORKDIR /app

COPY save_images_on_s3.py ./

CMD ["python3","save_images_on_s3.py"]