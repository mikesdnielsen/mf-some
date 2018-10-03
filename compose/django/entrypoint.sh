#!/bin/bash
set -e
cmd="$@"

# This file can contain settings up of environment variables etc.

# PostgreSQL can be slow to start up - make a function to check if it is up
# and running
function postgresql_is_ready(){
python << END
import sys
import psycopg2
try:
    conn = psycopg2.connect(
        dbname='postgres', user='postgres', host='postgresql')
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

until postgresql_is_ready; do
    >&2 echo "PostgreSQL is unavailable - waiting..."
    sleep 1
done

>&2 echo "PostgreSQL is ready - continuing..."

exec $cmd
