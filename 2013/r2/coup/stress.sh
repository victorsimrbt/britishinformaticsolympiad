#!/bin/bash

# solution.cpp          solution you want to stress test
# brute.cpp/brute.py    brute force solution for the problem
# gen.py                generates a new random test case for the problem

# compile all programs first
# g++ solution.cpp
# g++ brute.cpp -o brute
# g++ gen.cpp -o gen

for ((i=1; i<=16; i++)) do
    # ./a.out < "testdata/1-$i.in" > out
    python3 ans.py < "testdata/1-$i.in" > out
    if ! cmp -s out "testdata/1-$i.out"
    then
        echo 'Found failing test!'
        exit
    fi
    echo "OK 1-$i"
done

while true
do
  # generate a new test case in the file named "in"
  # note that we pass i as a random seed to the generator
  python3 gen.py > in
  # redirect the solution output to the "out" file
#   ./a.out < in > out
    python3 ans.py < in > out
  # redirect the brute force solution output to the "out-correct" file
  python3 brute.py < in > out-correct
  # ./brute < in > out-correct

  # compare both outputs.
  # if outputs are different, echo the 
  # corresponding message and break the loop.
  # failing test will be in the "in" file.
  if ! cmp -s out out-correct
  then
    echo 'Found failing test!'
    break
  fi

  # if outputs are the same, we echo "OK".
  # this is optional, but helps to see the progress of stress testing.
  echo 'OK'
done