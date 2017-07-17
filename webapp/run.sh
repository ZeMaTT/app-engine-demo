#!/usr/bin/env bash

pushd $(dirname $0) > /dev/null

echo "dev_appserver.py /src/default/app.yaml /src/frontend/frontend.yaml /src/dispatch.yaml --host=0.0.0.0 --admin_host=0.0.0.0 --port=8080 --enable_sendmail" "${@}"
dev_appserver.py /src/default/app.yaml /src/frontend/frontend.yaml /src/dispatch.yaml --host=0.0.0.0 --admin_host=0.0.0.0 --port=8080 --enable_sendmail "${@}"
#dev_appserver.py --port 8080 --admin_host=0.0.0.0 --host=0.0.0.0 default/app.yaml frontend/frontend.yaml dispatch.yaml

popd > /dev/null
