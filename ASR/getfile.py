import urllib.request
import sys
import os
file = sys.argv[1]
if file[:4]=="http":
    url = file
    if not os.path.exists('audio'):
        os.makedirs('audio')
    file = 'audio/' + url.split('/')[-1]
    if not os.path.exists(file):
        try:
            urllib.request.urlretrieve(url, filename=file)
        except Exception as e:
            print("Error occurred when downloading file, error message:")
            print(e)