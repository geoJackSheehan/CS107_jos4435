#!/usr/bin/env bash
for f in $(find -maxdepth 1 -type f -not -name ".*"); do
	variable=$(cat $f | sed '/^\s*#/d;/^\s*$/d' | wc -l)
                echo -n `basename $f` ; echo " $variable"
done
