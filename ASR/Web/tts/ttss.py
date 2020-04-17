# -*- coding: utf-8 -*-
import time
import random
import comtypes.client
from bottle import route, request, run, static_file

@route('/tts', method='POST')
def do_tts():
#    postValue = request.POST.decode('utf-8')
    text = request.POST.get('text')
    if text is None:
      return { 'success' : False}
    text = text.decode('utf-8')
    # print(text)
    filename = time.strftime('%Y%m%d-%H%M%S-',time.localtime(time.time())) + str(random.randint(0,999)).zfill(4) + '.wav'
    speak(filename, text)
    return { 'success' : True, 'path' : '/voice/' + filename }

@route('/voice/<filename>')
def get_voicefile(filename):
    return static_file(filename, root='./voice')

def speak(filename, text):
    print('file: ' + output_dir + filename)
    filestream.open(output_dir + filename, 3, False)   
    speaker.AudioOutputStream = filestream
    speaker.Speak(text)
    filestream.close()

if __name__=='__main__': 
    output_dir = 'voice/'
    speaker = comtypes.client.CreateObject("SAPI.SpVoice")
    filestream = comtypes.client.CreateObject("SAPI.spFileStream")
    filestream.format.type = 6	
    run(host='0.0.0.0', port=8080, debug=True)   #  , reloader=True)
