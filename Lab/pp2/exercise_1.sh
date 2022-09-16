#!/usr/bin/env bash

# Worked in a group with Annabel Yim, Chiara Chung-Halpern, and Jack Sheehan

read -p "Please enter a file to commit :" new_file

git add $new_file

git status

read -p "Would you like to continue to commit? Y or N:" continue_msg

if [[ "$continue_msg" = "N" ]]; then
	exit 1
else
	read -p "Please enter a commit message:" commit_msg
fi

git commit -m '$commit_msg'

git status

read -p "Would you like to continue to push? Y or N:" push_msg

if [[ "$push_msg" = "N" ]]; then
	exit 1
else
	git push origin main
fi
