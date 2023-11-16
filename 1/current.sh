#!/bin/bash

if [ ! -d hello\ current ]
then
        mkdir hello\ current
fi
cd hello\ current
if [ ! -f current.txt ]
then    touch current.txt
fi
echo "hello current!!" > current.txt
cat current.txt
