#!/bin/bash

#dir=$1

if test -f $1
then
    file=$1
    ncfile=$(basename $file)  #获取文件名本身
    suffix=".*"
    pfile=${ncfile%$suffix} #没有后缀
    #echo $pfile
    if [ ${file##*.} = "mp3" ] # ##*是贪婪匹配字符，匹配到最后一个.
    then
    echo $file into `echo $pfile`_L.wav and `echo $pfile`_R.wav
    # sox $file -r 16000 `echo "L_$ncfile" | sed 's/mp3/wav/g'` remix 1
    sox $file -r 16000 `echo $pfile`_L.wav remix 1
    sox $file -r 16000 `echo $pfile`_R.wav remix 2
    elif [ ${file##*.} = "wav" ]
    then
    echo "$file into $pfile_L.wav and $pfile_R.wav"
    sox $file -r 16000 `echo $pfile`_L.wav remix 1
    sox $file -r 16000 `echo $pfile`_R.wav remix 2
    fi
elif test -d $1
then
    dir=$1
    if [ ! -d "$dir/sox_res" ]
    then
    mkdir "$dir/sox_res"
    fi
    rm $dir/sounds_info 2> /dev/null
    for file in `ls $dir/*.wav 2> /dev/null`
    do
    ncfile=$(basename $file)
    suffix=".*"
    pfile=${ncfile%$suffix} #没有后缀
    echo "`echo $ncfile` into `echo $dir`sox_res/`echo $pfile`_L.wav"
    sox $file -r 16000 `echo $dir`sox_res/`echo $pfile`_L.wav remix 1
    echo "`echo $ncfile` into `echo $dir`sox_res/`echo $pfile`_R.wav"
    sox $file -r 16000 `echo $dir`sox_res/`echo $pfile`_R.wav remix 2
    echo "$pfile `soxi -D $file` $dir$ncfile\n" >> $dir/sounds_info
    done
    for file in `ls $dir/*.mp3 2> /dev/null`
    do
    ncfile=$(basename $file)
    suffix=".*"
    pfile=${ncfile%$suffix} #没有后缀
    echo "`echo $ncfile` into `echo $dir`sox_res/`echo $pfile`_L.wav"
    sox $file -r 16000 `echo $dir`sox_res/`echo $pfile`_L.wav remix 1
    echo "`echo $ncfile` into `echo $dir`sox_res/`echo $pfile`_R.wav"
    sox $file -r 16000 `echo $dir`sox_res/`echo $pfile`_R.wav remix 2
    echo "$pfile `soxi -D $file` $dir$ncfile\n" >> $dir/sounds_info
    # rm $file
    done
fi