FROM ubuntu:latest
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y git && \
    apt-get install -y mysql-server && \
    apt-get install -y pkg-config && \
    apt install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt install -y python3.8 && \
    apt-get install -y python3-dev && \
    apt-get install -y libmysqlclient-dev && \
    apt-get install -y zlib1g-dev && \
    apt-get install -y pip
RUN rm -r /home/Work && \
    mkdir /home/Work && \
    cd /home/Work && \
    git clone https://github.com/EverGreen1253/hbnb_evolution_02.git
RUN pip install flask && \
    pip install SQLAlchemy && \
    pip install mysqlclient && \
    pip install gunicorn


WORKDIR /home/Work/hbnb_evolution_02

EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]