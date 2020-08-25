#!/bin/bash

#path="/root/kaldi/egs/aidatatang_asr/"
path="/home/gpu/kaldi-master/egs/aidatatang_asr"
cd $path

dir=$1
if [ ! -d $dir ]
then
    exit 1
fi

start=$(date +%s)

echo "running sox.sh"
./sox.sh $dir
sounds="$dir/sox_res"

echo "running run2.sh"
./run2.sh $sounds > temp_output
decode_dir=`cat temp_output | grep 'decode result in ' | sed 's/decode\ result\ in\ //g' | sed 's/\ //g'`

end=$(date +%s)
take=$(( end - start ))
echo Time taken for run.sh is ${take} seconds.

echo "running get_ctm_fast.sh"
./get_ctm_fast.sh r graph $decode_dir CTMs/ctm_${decode_dir##*_}
rm temp_output

echo "running ctm_to_xml.py"
mkdir XMLs/xml_${decode_dir##*_}/
python3 ctm_to_xml.py $dir/sounds_info CTMs/ctm_${decode_dir##*_}/ctm XMLs/xml_${decode_dir##*_}/

end2=$(date +%s)
take2=$(( end2 - start ))
echo Time taken for ctm is ${take2} seconds.