#!/bin/bash

echo $1

bin/flume-ng agent --conf conf \
   --conf-file conf/flume.conf \
    --name $1 \
    -Dflume.root.logger=INFO,console