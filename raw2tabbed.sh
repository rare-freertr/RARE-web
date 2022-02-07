#!/bin/bash


# # **All-in-one page**

#| Test case        | status                     | Description                          |
#| :--------------- | :--------------------------|:----------------------------------- |
# | [`mpls-ldp01.tst`](../mpls/mpls-ldp01.tst.md) | :material-check: |    ldp over ethernet        |

#echo '*** Processing MD files from freeRtr test suite'

basic=0
conn=0
crypt=0
demo01=0
demo02=0
intop1=0
intop2=0
intop8=0
intop9=0
mpls=0
opnflw=0
p4lang=0
qos=0
rout=0
serv=0

RAW_FOLDER=raw
RAW_FILES=$(ls -1 $RAW_FOLDER)
PROGRAM_NAME="$(basename "$(test -L "$0" && readlink "$0" || echo "$0")")"

#echo - $PROGRAM_NAME processing: START

function tab_header {
    echo "    | Test case | status | Description |"
    echo "    | :--- | :--- |:--- |"
}


START=`date +%s`

echo "# **Features by category**"

for FILE in $RAW_FILES
do
    #echo Processing $FILE: START
    DESCRIPTION=$(head -n 1 $RAW_FOLDER/$FILE | sed 's/# Example: //')
    TST_NAME=$(echo $FILE | sed 's/.tst.md//')
    TST_TYPE=$(echo $FILE | sed -r 's/-.*.tst.md|.tst.md//')

    if [ "$TST_TYPE" = "conn" ]; then
        if [ $conn = 0 ]; then
            echo -e '\n=== "Connection"\n'
            echo -e "    ## **Connection test cases**\n"
            tab_header
            conn=1
        fi
        echo "    | [$TST_NAME](md/$FILE) | :material-check: | $DESCRIPTION |"
    fi

    if [ "$TST_TYPE" = "crypt" ]; then
        if [ $crypt = 0 ]; then
            echo -e '\n=== "Cryptograhy"\n'
            echo -e "    ## **Cryptograhy test cases**\n"
            tab_header
            crypt=1
        fi
        echo "    | [$TST_NAME](md/$FILE) | :material-check: | $DESCRIPTION |"
    fi

    if [ "$TST_TYPE" = "mpls" ]; then
        if [ $mpls = 0 ]; then
            echo -e '\n=== "MPLS"\n'
            echo -e "    ## **Multi-Protocol-Label-Switching test cases**\n"
            tab_header
            mpls=1
        fi
        echo "    | [$TST_NAME](md/$FILE) | :material-check: | $DESCRIPTION |"
    fi

    if [ "$TST_TYPE" = "qos" ]; then
        if [ $qos = 0 ]; then
            echo -e '\n=== "QoS"\n'
            echo -e "    ## **Quality of Service test cases**\n"
            tab_header
            qos=1
        fi
        echo "    | [$TST_NAME](md/$FILE) | :material-check: | $DESCRIPTION |"
    fi

    if [ "$TST_TYPE" = "rout" ]; then
        if [ $rout = 0 ]; then
            echo -e '\n=== "Routing protocol"\n'
            echo -e "    ## ** Routing protocol test cases**\n"
            tab_header
            rout=1
        fi
        echo "    | [$TST_NAME](md/$FILE) | :material-check: | $DESCRIPTION |"
    fi

    if [ "$TST_TYPE" = "serv" ]; then
        if [ $serv = 0 ]; then
            echo -e '\n=== "Server"\n'
            echo -e "    ## **Server test cases**\n"
            tab_header
            serv=1
        fi
        echo "    | [$TST_NAME](md/$FILE) | :material-check: | $DESCRIPTION |"
    fi

#    echo $TST_TYPE

done

END=`date +%s`

RUNTIME=$((END-START))

#echo "- $PROGRAM_NAME processing: DONE [DURATION: $RUNTIME s]"
