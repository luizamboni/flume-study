Flume stody with docker aid
===

Using flume **1.8**

```bash
$ docker build -t flume . && docker run -it flume ag1
```
to send data to source a1.r1 use telnet

```bash
$ telnet localhost 44444
```

to generate a mock data use

```bash
$  ./gen_data.py 100000 2 >> /var/log/profiles.log
```