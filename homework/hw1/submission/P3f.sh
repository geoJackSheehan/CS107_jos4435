#!/usr/bin/env bash
for f in $(find -maxdepth 1 -type f -not -name ".*"); do
	cat $f | sed '/^\s*#/d;/^\s*$/d' | wc -l > numberfile.txt
	for g in $(cat numberfile.txt); do
		echo -n `basename $f` ; echo " $g"
	done
done
rm numberfile.txt
