#!/bin/sh
# Platform trial P-25, its second run: a file for CodeRabbit to review, with its approval once resolved switched off.
for f in $(ls *.txt); do
    cat $f | grep TODO > /tmp/out
    rm -rf $DIR/
done
