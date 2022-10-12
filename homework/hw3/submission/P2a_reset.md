The file has the exact same content because we did not edit it. Our first git reset (soft) reset the commit corresponding to function -> CommonAncestor. However, we simply recommit this again with no changes. Then, we reset this most recent commit (mixed: default), but again did not make any edits before commmiting again. 

If we check git log after each commit, each of the last 3 commits: 'Change function name again (devA)', 'Changed my mind (devA)', and 'Changed my mind again (devA)' all have the same parent commit: 'Change function name (devA)'. 

Additionally, each blob hash corresponding to func.py is the same for each commit, because the file content does not change. This reinforces the point that the only change made was to the commits.
