#!/bin/sh
# P-5 with the queue App, CodeRabbit's case (issue 389): a file for CodeRabbit to review.
for f in $(ls *.log); do
    cat $f | grep ERROR > /tmp/errors.txt
    rm -rf $DIR/
done
