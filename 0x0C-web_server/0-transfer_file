#!/usr/bin/env bash
# Transfers a file from our client to a server
#
# variables
if [ $# -lt 4 ]
then
  echo "Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY"
else
  scp -o StrictHostKeyChecking=no -i "$4" "$1" "$3@$2":~
fi
