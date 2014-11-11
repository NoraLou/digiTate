import os
# import pprint
import json


def load_json(file_name):
    file = open(file_name)
    json_text = file.read()
    file.close()

    data = json.loads(json_text)
    print(data)


def loop_Dir (file_path):
	for directr in os.walk(file_path).next()[1]:
		print directr
		new_dir = file_path + "/" + directr
		print new_dir
		print os.listdir(new_dir)
		file_names = os.listdir(new_dir)
		for i in file_names:
			print i
			load_json(new_dir + "/" + i)


		# for i in os.walk(new_dir).next()[1]:
		# 	print new_dir






		# print(files)
		# for f in files:
		# 	directory = f[0]  

		# 	load_json(directory + "/"+f)




		 # for files in directory:
			# print "*****************"
			# print files
			# for f in files:
			# 	print"**************"
			# 	print f
			# 	# load_json(f)

			




loop_Dir("./collection-master/artists")