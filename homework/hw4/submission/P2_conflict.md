The child commit (Extending new feature with component A) is based on data that is no longer there, which is causing the merge conflict. It expects the line above its added data to say "This code adds a new feature" but since that commit has been dropped now that line is not there.

You could avoid this merge conflict by reordering the commits first in interactive rebase, which would turn "Adding new feature to code" into the child instead of the parent, preventing the merge conflict when we drop the commit.

If the child contained changes not related to the new feature, a good commit stratey would be to commit them on a different branch until we have tested everything and are certain it is correct. 
