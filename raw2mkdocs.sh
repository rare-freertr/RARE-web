#!/bin/bash

echo '*** Processing MD files from freeRtr test suite'

RAW_FOLDER=raw
RAW_FILES=$(ls -1 $RAW_FOLDER)
PROGRAM_NAME="$(basename "$(test -L "$0" && readlink "$0" || echo "$0")")"


#echo - $PROGRAM_NAME processing: START

mkdir -p docs/guides/reference/md
cd docs/guides/reference/md

START=`date +%s`

for FILE in $RAW_FILES
do
    ln -s ../../../../$RAW_FOLDER/$FILE $FILE
done

END=`date +%s`

RUNTIME=$((END-START))

echo "- $PROGRAM_NAME processing: DONE [DURATION: $RUNTIME s]"
