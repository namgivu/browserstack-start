FROM namgivu/ubuntu-pipenv:18.04-3.7

WORKDIR /app

ARG echo200609x0
COPY  ./Pipfile      ./
COPY  ./Pipfile.lock ./
RUN   pipenv sync

COPY .       .
#    source  workdir

EXPOSE 5000
CMD PYTHONPATH=`pwd`  pipenv run  gunicorn  -b '0.0.0.0:5000'  src.runtest_via_api.api:api  --timeout 6666        --log-level=debug
#   .                 .           .         default port       falcon instance              long lasting request  full debug info in log
