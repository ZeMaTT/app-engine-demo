#!/usr/bin/env bash
docker rm `docker ps -q -a --filter 'status=exited'`
