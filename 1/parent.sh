#!/bin/bash

cd ..
if [ ! -d hello\ parent ]
then
        mkdir hello\ parent
fi
cd hello\ parent
if [ ! -f parent.txt ]
then    touch parent.txt
fi
echo "hello parent!!" > parent.txt
cat parent.txt
