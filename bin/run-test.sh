#!/usr/bin/env bash
docstring='
 ./bin/run-test.sh      # run normal
 ./bin/run-test.sh -n6  # run with 6 parallel threads
'

SH=`cd $(dirname $BASH_SOURCE) && pwd`
AH=`cd $SH/.. && pwd`

[[ -z $pipenvsync ]] || pipenv sync  # skip package install as default, otherwise must set :pipenvsync param

    cd $AH
        PYTHONPATH=`pwd` pipenv run pytest $*
    cd - 1>/dev/null
