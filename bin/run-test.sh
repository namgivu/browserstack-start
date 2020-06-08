#!/usr/bin/env bash
docstring='
./bin/run-test.sh      # run normal
./bin/run-test.sh -n6  # run with 6 parallel threads

./bin/run-test.sh -n8 --reruns 2  # run parallel as 8 and retry-max-2-times/each-test-if-fail
'

SH=`cd $(dirname $BASH_SOURCE) && pwd`
AH=`cd $SH/.. && pwd`

[[ -z $pipenvsync ]] || pipenv sync  # skip package install as default, otherwise must set :pipenvsync param

    cd $AH
        PYTHONPATH=`pwd` pipenv run pytest $*
    cd - 1>/dev/null
