#!/bin/sh

if [ "$SPARK_MODE" = "master" ]; then
    /opt/spark/sbin/start-master.sh
elif [ "$SPARK_MODE" = "worker" ]; then
    /opt/spark/sbin/start-slave.sh $SPARK_MASTER
fi

tail -f /dev/null