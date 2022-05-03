import argparse
import os
import subprocess

parser = argparse.ArgumentParser(description='')

#parser.add_argument('-t', required=True, help='text')
#parser.add_argument('-p', required=True, help='file_dir_path')
parser.add_argument('--session_id', default="", help='session_id')

opt = parser.parse_args()

#temp_dir = '/home/workspace/tmp_dir/*.wav'
temp_dir = '/home/workspace/tmp_dir'
#save_dir = '/home/workspace/target/'
save_dir = '/home/workspace/app/KDT_B1_2/b1project/homepage/static/file_audio/' + opt.id

try:
    f = open('/home/workspace/folktale_full_data', 'r')
except:
    print('no such data or dir')    

# row[2] : contents / row[3] : talker_identifier / row[4] : title_id / row[1] : line_index

sysnthesizer_cmd = '/home/workspace/model/KDT_B1/Tacotron2-Wavenet-Korean-TTS/synthesizer.py'
load_path = '--load_path logdir-tacotron2/++++++++++_2022-04-25_05-21-56'
num_speaker = '--num_speakers 11'
sample_path = '--sample_path ' + temp_dir
fixed_cmd ='python' + ' ' + sysnthesizer_cmd + ' ' +load_path + ' '  + sample_path + ' '+ num_speaker

if not os.path.isdir(save_dir[:-2]):
    os.mkdir(save_dir[:-2])

if not os.path.isdir(sample_path.split()[1]):
    os.mkdir(sample_path.split()[1])

cnt = 0
lines = f.readlines()
for line in lines :
    #if cnt >= 3:
        #break
    for i in range(11):
        print(fixed_cmd +' ' + '--speaker_id' + ' ' + str(i) + ' ' + '--text' + ' "' + line.split('\t')[0]  + '."')
        os.system(fixed_cmd +' ' + '--speaker_id' +' ' + str(i) + ' ' + '--text' + ' "' + line.split('\t')[0]  + '."')
    wav_file_list = subprocess.check_output(['ls ' + temp_dir + '/*.wav'], shell=True, universal_newlines=True)

    for wav_file in wav_file_list.split('\n') :
        if wav_file :
            print('mv ' + wav_file + ' '  + save_dir + str(line.split('\t')[2]) + '/' + str(line.split('\t')[3].strip()) + '.wav')
            if not os.path.isdir(save_dir + str(line.split('\t')[2])):
                os.mkdir(save_dir + str(line.split('\t')[2]))
            os.system('mv ' + wav_file + ' '  + save_dir + str(line.split('\t')[2]) + '/'  + str(line.split('\t')[3].strip()) + '.wav')
    cnt += 1

#get_files = os.listdir(opt.p)

#num =1
#for g in get_files:
#    if g.split('.')[1] == 'wav':  
#        print('move and rename' + g)
#        os.rename(opt.p + '/' + g, save_dir +'/' + str(num) +'.wav')
#        num += 1
