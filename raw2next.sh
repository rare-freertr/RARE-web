#!/bin/bash

#echo '*** Processing MD files from freeRtr test suite'

RAW_FOLDER=raw
RAW_FILES=$(ls -1 $RAW_FOLDER)


START=`date +%s`

echo - $PROGRAM_NAME processing: START

for FILE in $RAW_FILES
do
    sed -ri "/Example|Topology diagram|Configuration|Verification/! s/^/    /" $RAW_FOLDER/$FILE
    sed -i '/## \*\*Topology diagram\*\*/c\=== "Topology"' $RAW_FOLDER/$FILE
    sed -i '/## \*\*Configuration\*\*/c\=== "Configuration"' $RAW_FOLDER/$FILE
    sed -i '/## \*\*Verification\*\*/c\=== "Verification"' $RAW_FOLDER/$FILE
    sed -i '/\[topology\]/c\     <div class="nextWrapper">\n         <iframe src="/guides/reference/snippets/next-diagram.html" style="border:none;"></iframe>\n     </div>\n' $RAW_FOLDER/$FILE
done

END=`date +%s`

RUNTIME=$((END-START))

echo "- $PROGRAM_NAME processing: DONE [DURATION: $RUNTIME s]"
