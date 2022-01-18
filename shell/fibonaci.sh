#!/bin/bash

number=10
a=0
b=1

echo "Fibonaci series upto $number is:"
echo "$a"
echo "$b"

i=2
while [ $i -lt $number ]
do
	fib=$((a+b))
	echo $fib
	a=$b
	b=$fib
	i=`expr $i + 1`
done
