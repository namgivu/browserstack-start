#!/usr/bin/env bash
SH=`cd $(dirname $BASH_SOURCE) && pwd`
AH=`cd $SH/../../.. && pwd`

source "$SH/.config.sh"
    docker stop -t1 $CONTAINER_NAME; docker rm -f $CONTAINER_NAME
    docker network create  --driver bridge  $NETWORK_NAME || true
        docker run  --name $CONTAINER_NAME  -p $PORT:5000  -d      --restart unless-stopped  --net $NETWORK_NAME  $IMAGE_NAME
        #           container name          port mapping   daemon  auto-restart if crashed   docker network       .
            sleep 2
            docker logs $CONTAINER_NAME
                echo
                http -h :$PORT/health | head -n1
                echo "
# view log
docker logs $CONTAINER_NAME
"
