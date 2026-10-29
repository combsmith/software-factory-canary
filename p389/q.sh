#!/bin/sh
# Window 3 (issue 389): a file for review threads, which the queue App resolves.
for f in $(ls *.log); do
    grep ERROR $f >> /tmp/errors
done
