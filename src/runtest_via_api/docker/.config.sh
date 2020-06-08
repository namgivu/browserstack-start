#!/usr/bin/env bash
cSH=`cd $(dirname $BASH_SOURCE) && pwd`

    IMAGE_NAME='namgivu/aqa_brs_runtestviaapi'
CONTAINER_NAME='namgivu__aqa_brs_runtestviaapi'
          PORT=20609
  NETWORK_NAME="${CONTAINER_NAME}__dockernetwork"
