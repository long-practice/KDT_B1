#import argparse
import os
import subprocess

#parser = argparse.ArgumentParser(description='')

#parser.add_argument('-t', required=True, help='text')
#parser.add_argument('-p', required=True, help='file_dir_path')
#parser.add_argument('--session_id', default="", help='session_id')

#opt = parser.parse_args()

#temp_dir = '/home/workspace/tmp_dir/*.wav'
temp_dir = '/home/workspace/tmp_dir'
#save_dir = '/home/workspace/target/'
save_dir = '/home/workspace/app/KDT_B1_2/b1project/homepage/static/file_audio/' #+ opt.session_id

sysnthesizer_cmd = '/home/workspace/model/KDT_B1/Tacotron2-Wavenet-Korean-TTS/synthesizer.py'
load_path = '--load_path logdir-tacotron2/50000steps'
num_speaker = '--num_speakers 11'
sample_path = '--sample_path ' + temp_dir
fixed_cmd ='python' + ' ' + sysnthesizer_cmd + ' ' +load_path + ' '  + sample_path + ' '+ num_speaker

if not os.path.isdir(save_dir):
    os.mkdir(save_dir)

if not os.path.isdir(temp_dir):
    os.mkdir(temp_dir)


try:
    f = open('/home/workspace/folktale_full_data', 'r')
except:
    print('no such data or dir')    

# row[2] : contents / row[3] : talker_identifier / row[4] : title_id / row[1] : line_index

lines = f.readlines()

for line in lines:
    print(fixed_cmd +' ' + '--speaker_id' + ' ' + line.split('\t')[1] + ' ' + '--text' + ' "' + line.split('\t')[0]  + '."')
    os.system(fixed_cmd +' ' + '--speaker_id' +' ' + line.split('\t')[1] + ' ' + '--text' + ' "' + line.split('\t')[0]  + '."')
wav_file_list = subprocess.check_output(['ls ' + temp_dir + '/*.wav'], shell=True, universal_newlines=True)

#'/home/workspace/tmp_dir'

for wav_file in wav_file_list.split('\n') :
    if wav_file :
        print('mv ' + wav_file + ' '  + save_dir + str(line.split('\t')[2]) + '/' + str(line.split('\t')[3].strip()) + '.wav')
        if not os.path.isdir(save_dir + str(line.split('\t')[2])):
            os.mkdir(save_dir + str(line.split('\t')[2]))
        os.system('mv ' + wav_file + ' '  + save_dir + str(line.split('\t')[2]) + '/'  + str(line.split('\t')[3].strip()) + '.wav')
        
        #'/home/workspace/app/KDT_B1_2/b1project/homepage/static/file_audio/' + opt.id

# if opt.session_id != "":
    
#     try:
#         f = open('input data path', 'r')
#     except:
#         print('no such data or dir')    

#     # row[2] : contents / row[3] : talker_identifier / row[4] : title_id / row[1] : line_index

#     lines = f.readlines()
    
#     for line in lines:
#         print(fixed_cmd +' ' + '--speaker_id' + ' ' + 'user input speaker_id' + ' ' + '--text' + ' "' + line  + '."')
#         os.system(fixed_cmd +' ' + '--speaker_id' +' ' + 'user input speaker_id' + ' ' + '--text' + ' "' + line  + '."')
#     wav_file_list = subprocess.check_output(['ls ' + temp_dir + '/*.wav'], shell=True, universal_newlines=True)
    
#     #'/home/workspace/tmp_dir'
#     cnt = 1
#     for wav_file in wav_file_list.split('\n') :
#         if wav_file :
#             print('mv ' + wav_file + ' '  + save_dir  + '/' + cnt + '.wav')
#             os.system('mv ' + wav_file + ' '  + save_dir + '/'  + cnt + '.wav')
#             cnt+=1
#             #'/home/workspace/app/KDT_B1_2/b1project/homepage/static/file_audio/' + opt.id
            
            
            
# else:
#     try:
#         f = open('/home/workspace/folktale_full_data', 'r')
#     except:
#         print('no such data or dir')    

#     # row[2] : contents / row[3] : talker_identifier / row[4] : title_id / row[1] : line_index

#     lines = f.readlines()

#     for line in lines:
#         print(fixed_cmd +' ' + '--speaker_id' + ' ' + line.split('\t')[1] + ' ' + '--text' + ' "' + line.split('\t')[0]  + '."')
#         os.system(fixed_cmd +' ' + '--speaker_id' +' ' + line.split('\t')[1] + ' ' + '--text' + ' "' + line.split('\t')[0]  + '."')
#     wav_file_list = subprocess.check_output(['ls ' + temp_dir + '/*.wav'], shell=True, universal_newlines=True)
    
#     #'/home/workspace/tmp_dir'

#     for wav_file in wav_file_list.split('\n') :
#         if wav_file :
#             print('mv ' + wav_file + ' '  + save_dir + str(line.split('\t')[2]) + '/' + str(line.split('\t')[3].strip()) + '.wav')
#             if not os.path.isdir(save_dir + str(line.split('\t')[2])):
#                 os.mkdir(save_dir + str(line.split('\t')[2]))
#             os.system('mv ' + wav_file + ' '  + save_dir + str(line.split('\t')[2]) + '/'  + str(line.split('\t')[3].strip()) + '.wav')
            
#             #'/home/workspace/app/KDT_B1_2/b1project/homepage/static/file_audio/' + opt.id