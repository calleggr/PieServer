#!/bin/bash


declare -a arr=("python src/start_test_server.py" "python src/start_ssl_server.py")

for cmd in "${arr[@]}"; do {
  echo "Process \"$cmd\" started";
  $cmd & pid=$!
  PID_LIST+=" $pid";
} done

trap "kill $PID_LIST" SIGINT

echo "Parallel processes have started";

wait $PID_LIST

echo
echo "All processes have completed";
