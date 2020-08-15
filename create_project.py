
import os
import argparse

# args option
parser = argparse.ArgumentParser()
parser.add_argument('--project_name',type=str,default='My_Project',help='The name of project')
args = parser.parse_args()

# Create Folder

folder_list = ['models','checkpoints','data','datasets','docs','options','result','scripts','test_out','util']
file_list = ['train.py','test.py']

if not os.path.isdir('./'+args.project_name):
	os.mkdir(args.project_name)
os.chdir(args.project_name)
print('Starting create folders....')
for folder_name in folder_list:
	path = './' + folder_name
	if not os.path.isdir(path):
		os.mkdir(path)
print('Successfully creating folders !')
print('Starting create files....')
for file_name in file_list:
	path = './' + file_name
	if not os.path.isfile(path):
		fd = open(path,mode='w',encoding='utf-8')
		fd.close()

print('Successfully creating files !')
