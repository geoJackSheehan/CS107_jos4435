#!/usr/bin/env bash

# Worked in a group with Chiara Chung-Halpern, Annabel Yim, and Jack Sheehan

for f in $(ls); do
	if [ -x "$f" ]; then
		echo "'$f' is executable"
	fi
done

