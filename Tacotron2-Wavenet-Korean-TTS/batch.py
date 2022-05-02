import argparse
import os
import subprocess
import time

temp_dir = '/home/workspace/younghoon/tmp_dir/*.wav'
#save_dir = '/home/workspace/younghoon/target/'
save_dir = '/home/workspace/app/KDT_B1_2/b1project/homepage/static/file_audio/'


f = open('/home/workspace/folktale_data', 'r')

# row[2] : contents / row[3] : talker_identifier / row[4] : title_id / row[1] : line_index

sysnthesizer_cmd = '/home/workspace/model/KDT_B1/Tacotron2-Wavenet-Korean-TTS/synthesizer.py'
load_path = '--load_path logdir-tacotron2/++++++++++_2022-04-25_05-21-56'
num_speaker = '--num_speakers 11'
sample_path = '--sample_path /home/workspace/younghoon/tmp_dir'
fixed_cmd = 'python' + ' ' + sysnthesizer_cmd + ' ' +load_path + ' '  + sample_path + ' '  + num_speaker

cnt = 0
lines = f.readlines()
for line in lines :
#    if cnt >= 2:
#        break

    #print(fixed_cmd +' ' + '--speaker_id ' + line.split('\t')[1] + ' ' + '--text' + ' "' + line.split('\t')[0]  + '"')
    os.system(fixed_cmd + ' ' + '--speaker_id ' + line.split('\t')[1] + ' ' + '--text' + ' "' + line.split('\t')[0]  + '"')
    time.sleep(3)
    wav_file_list = subprocess.check_output(['ls ' + temp_dir], shell=True, universal_newlines=True)

    for wav_file in wav_file_list.split('\n') :
        if wav_file :
            #print('mv ' + wav_file + ' '  + save_dir + str(line.split('\t')[2]) + '/' + str(line.split('\t')[3].strip()) + '.wav')
            os.system('mv ' + wav_file + ' '  + save_dir + str(line.split('\t')[2]) + '/'  + str(line.split('\t')[3].strip()) + '.wav')
            print('mv ' + wav_file + ' '  + save_dir + str(line.split('\t')[2]) + '/' + str(line.split('\t')[3].strip()) + '.wav')
    cnt += 1

