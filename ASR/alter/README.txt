操作方法
1. 进入内部服务器192.168.2.103, User: gpu, password: gpu001
2. 进入文件夹位置：/home/gpu/kaldi-master/egs/aidatatang_asr
3. 把双声道的mp3或wav的一个或多个文件放入一个文件夹下，并运行sudo ./asr.sh <文件夹名>/  (注意文件夹末尾必须加'/')
4. 脚本将会执行sox.sh，run2.sh, get_ctm_fast.sh, 和ctm_to_xml.sh。./run2.sh将会持续一段时间，大概是录音文件总时长的1/10。
5. 若执行成功，转译文本结果将会在exp/chain/tdnn_1a_sp/decode_offline_test_<time>/rec_<time>.txt. <time>为翻译时的中国时间。同理，时间戳文件ctm和标准格式xml文件将在文件夹./CTMs和./XMLs下的对应时间文件夹。

关键脚本
1. asr.sh: 依次执行转译的步骤，sox.sh做音频各式处理，run.sh做转译，get_ctm_fast做时间戳提取，ctm_to_xml做xml结果生成。
2. sox.sh: 输入一个放着mp3或wav的文件夹，将每个文件的两个声道剥离并分别变为16000Hz的wav单声道文件，存于此文件夹的sox_res文件夹下。并生成一个sounds_info文件，储存每个录音的时长和位置供生成xml使用。
3. run2.sh: 输入一个放着16000HZ单声道录音的文件夹，输出decode转译结果并生成Lat.*.gz过程文件。可修改并发数量nj，默认为10。
4. get_ctm_fast.sh: 提取lat.1.gz里的时间戳部分，放入ctm文件中。
5. ctm_to_xml.py: 将所有录音根据录音名和左右声道两两匹配，根据每个词的时间顺序和间隔自动分句，计算语速和静音片段，把所有ctm文件转换成一个个左右声道合并的xml文件结果。

6. alter.py: Two modes:
    a) Forceful translation of certain pinyin to certain words. Use -p or --pinyin=wordbank, where wordbank is the file storing target words.
    b) Substitute certain words into other words. Use -s or --sub=change, where change stores the paired two words '[ori] [sub]'
7. xml_cleaner.py: 把xml里的'[_-][0-9]+'去掉，此为修改词表graph/words.txt的过程参数(unique id)。