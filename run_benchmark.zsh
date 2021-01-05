#!/usr/bin/zsh

# Time and memory benchmark from 
# https://superuser.com/a/767491/740294

if [[ `uname` == Darwin ]]; then
    MAX_MEMORY_UNITS=KB
else
    MAX_MEMORY_UNITS=MB
fi

TIMEFMT='%J   %U  user %S system %P cpu %*E total'$'\n'\
'avg shared (code):         %X KB'$'\n'\
'avg unshared (data/stack): %D KB'$'\n'\
'total (sum):               %K KB'$'\n'\
'max memory:                %M '$MAX_MEMORY_UNITS''$'\n'\
'page faults from disk:     %F'$'\n'\
'other page faults:         %R'

echo "# Running benchmark for squarify"
time ./benchmark.py squarify
echo 
echo
echo "# Running benchmark for sparse_triangular"
time ./benchmark.py sparse_triangular
echo
echo

