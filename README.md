Flume stody with docker aid
===

Using flume **1.8**

```bash
$ docker build -t flume . && docker run -it flume entrypoint.sh agent_foo
```
to send data to source a1.r1 use telnet

```bash
$ telnet localhost 44444
```