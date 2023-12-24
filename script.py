# IMPORTS
import json
import os
import shutil
import sys

# CONSTANTS
with open('my_secrets.json') as f:
    my_secrets = json.load(f)
src_dir = my_secrets['src_dir']
dst_dir = my_secrets['dst_dir']

# OTHER VARIABLES
files = os.listdir(src_dir)
courses = os.listdir(dst_dir)
ref = {}

# CODE BODY
if len(courses) == 0:
    sys.exit(0)
else:
    for i in range(len(courses)):
        course = courses[i]
        course_code = course[1:5] + '-' + course[6:10] + '_'
        ref[course_code] = course

for file in files:
    for key in ref.keys():
        if file.startswith(key):
            shutil.move(src_dir + '/' + file, dst_dir + '/' + ref[key])