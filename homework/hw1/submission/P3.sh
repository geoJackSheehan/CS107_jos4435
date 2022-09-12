grep [0-9] apollo13.txt | wc -l > out.txt # command for b
grep --help | grep ' count' # command for c
find . -maxdepth 1 -type f -name "*.py" | wc -l # command for d
find . -type f -not -path "*/.*" -not -perm -o=r,o=w # command for e part 1
find . -maxdepth 1 -not -name ".*" -not -perm -o=r,o=w # command for e part 2
