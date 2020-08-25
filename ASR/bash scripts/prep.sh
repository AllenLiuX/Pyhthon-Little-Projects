#!/bin/bash

dir=$1
path="/home/gpu/kaldi-master/egs/cvte/s5"
cd $path

if test -f $dir
then
    echo "Error. Input should be a directory"
    exit 1
elif test -d $dir
then
    ncdir=$(basename $dir)    #$dir 最后不要有/
    rm -r data/test_`echo $ncdir`
    mkdir data/test_`echo $ncdir`
    echo "generating utt2spk, text, wav.scp, spk2utt"
    for file in `ls $dir`
    do
        ncfile=$(basename $file)
        suffix=".*"
        pfile=${ncfile%$suffix}
        if [ ${file: 0-3} == "wav" ]
        then
            echo "$pfile $pfile" >> data/test_`echo $ncdir`/utt2spk
            echo -e "$pfile\tA" >> data/test_`echo $ncdir`/text
            echo -e "$pfile\t$dir$ncfile" >> data/test_`echo $ncdir`/wav.scp
        fi
    done
    cp data/test_`echo $ncdir`/utt2spk data/test_`echo $ncdir`/spk2utt

    echo "copying frame_shift, conf"
    cp frame_shift data/test_`echo $ncdir`
    cp -r conf data/test_`echo $ncdir`
fi