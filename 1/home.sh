#!/bin/bash

cd $HOME
if [ ! -d hello\ home ]
then
        mkdir hello\ home
fi
cd hello\ home
if [ ! -f home.txt ]
then    touch home.txt
fi
echo "hello home!!" > home.txt
cat home.txt
