#!/usr/bin/env bash

DEFAULT_COMMAND="/bin/bash /src/run.sh"

if [ "$#" -gt 1 ]
then
    command="$@"
else
    command="${DEFAULT_COMMAND}"
fi

pushd $(dirname $0) > /dev/null

echo "${command}"

docker run -ti -p 8080:8080 -p 8000:8000 -v "$(pwd)/webapp":/src google/cloud-sdk ${command}
popd > /dev/null
