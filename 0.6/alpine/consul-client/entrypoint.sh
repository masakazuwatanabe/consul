#!/bin/sh

set -e

if [ $# -ne 0 ]; then
	exec "$@"
fi

exec /entrypoint.py
