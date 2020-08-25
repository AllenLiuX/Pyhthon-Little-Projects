#!/bin/bash

#dir=$1

if test -f $1
then
    file=$1
    if [ ${file##*.} = "mp3" ] # ##*是贪婪匹配字符，匹配到最后一个.
    then
	sox $file -r 16000 -c 1 `echo $file| sed 's/mp3/wav/g'`
    elif [ ${file##*.} = "wav" ]
    then
	 sox $file -r 16000 -c 1 $file
    fi
elif test -d $1
then
    dir=$1
    for file in `ls $dir/*.wav`
    do
	echo "`echo $file | sed 's/^.*\///g'` into `echo $file | sed 's/^.*\///g'`"
	sox $file -r 16000 -c 1 $file
    done
    for file in `ls $dir/*.mp3`
    do
	echo "`echo $file | sed 's/^.*\///g'` into `echo $file| sed 's/mp3/wav/g' | sed 's/^.*\///g'`"
	sox $file -r 16000 -c 1 `echo $file| sed 's/mp3/wav/g'`
	rm $file
    done
fi
