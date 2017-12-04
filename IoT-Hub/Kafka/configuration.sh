#!/bin/bash

#echo "192.168.0.137 ubuntu" | sudo tee -a /etc/hosts
#echo "192.168.0.139 black-pearl" | sudo tee -a /etc/hosts

if [ $1 = "zookeeper" ]
then
	/kafka/bin/zookeeper-server-start.sh config/zookeeper.properties
elif [ $1 = "broker" ]
then
	sed -i 's/broker.id=0/broker.id='$2'/g' config/server.properties
        sed -i 's/port=9092/port='$3'/g' config/server.properties
	/kafka/bin/kafka-server-start.sh config/server.properties
else
	exit
fi
