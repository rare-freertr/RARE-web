#!/bin/bash


# # **All-in-one page**

#| Test case        | status                     | Description                          |
#| :--------------- | :--------------------------|:----------------------------------- |
# | [`mpls-ldp01.tst`](../mpls/mpls-ldp01.tst.md) | :material-check: |    ldp over ethernet        |

#echo '*** Processing MD files from freeRtr test suite'


RAW_FOLDER=raw
RAW_FILES=$(ls -1 $RAW_FOLDER)
PROGRAM_NAME="$(basename "$(test -L "$0" && readlink "$0" || echo "$0")")"

#echo - $PROGRAM_NAME processing: START

echo -e "# **All features in one page**\n"
echo "| Test case | status | Description |"
echo "| :--- | :--- |:--- |"

START=`date +%s`

for FILE in $RAW_FILES
do
    #echo Processing $FILE: START
    DESCRIPTION=$(head -n 1 $RAW_FOLDER/$FILE | sed 's/# Example: //')
    TST_NAME=$(echo $FILE | sed 's/.tst.md//')

    echo "| [$TST_NAME](md/$FILE) | :material-check: | $DESCRIPTION |"


done

END=`date +%s`

RUNTIME=$((END-START))

#echo "- $PROGRAM_NAME processing: DONE [DURATION: $RUNTIME s]"
