#!/bin/sh
# Platform trials P-5 and P-25 (combsmith/software-factory#185): a file for review threads to be opened on, by
# CodeRabbit, the trial-author App and a person, and resolved by the pr-review App. Nothing runs it.
for f in $(ls $1); do
  cat $f | grep TODO
done
