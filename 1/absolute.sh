#!/bin/bash

cd /
if [ ! -d tmp ]
then
	mkdir tmp
fi
cd tmp
if [ ! -d hello\ world ]
then
	mkdir hello\ world
fi
cd hello\ world
if [ ! -f absolute.txt ]
then
	touch absolute.txt
fi
echo "hello world!!" > absolute.txt
cat absolute.txt
