FROM java:8



RUN curl -L http://ftp.unicamp.br/pub/apache/flume/1.8.0/apache-flume-1.8.0-bin.tar.gz -s -o - | tar -xzf -

RUN mv ./apache-flume-1.8.0-bin ./flume
# cp ./apache-flume/conf/flume-conf.properties.template ./apache-flume/conf/flume.conf
WORKDIR flume

COPY conf/flume.conf ./conf/flume.conf
COPY entrypoint.sh ./entrypoint.sh
COPY gen_data.py gen_data.py

RUN apt-get update && apt install -y telnet

# RUN find .

ENTRYPOINT [ "./entrypoint.sh" ]
