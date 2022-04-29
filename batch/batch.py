import argparse
import os

parser = argparse.ArgumentParser(description='file mv match dir and rename')

#parser.add_argument('-t', required=True, help='text')
parser.add_argument('-p', required=True, help='file_dir_path')
parser.add_argument('-n', required=True, help='title_id')

opt = parser.parse_args()

save_dir = '/home/app/KDT_B1_2/b1project/homepage/static/file_audio/' + opt.n
print('title_id : ' + opt.n)

if not os.path.isdir(save_dir):
    os.mkdir(save_dir)
    
get_files = os.listdir(opt.p)

num =1
for g in get_files:
    if g.split('.')[1] == 'wav':  
        print('move and rename' + g)
        os.rename(opt.p + '/' + g, save_dir +'/' + str(num) +'.wav')
        num += 1