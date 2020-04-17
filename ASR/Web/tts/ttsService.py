# -*- coding: utf-8 -*-
import time
import random
import comtypes.client
from bottle import route, request, run, static_file
import win32serviceutil 
import win32service 
import win32event
import os 
import logging
import inspect 

speaker = comtypes.client.CreateObject("SAPI.SpVoice")
filestream = comtypes.client.CreateObject("SAPI.spFileStream")
filestream.format.type = 6	  
output_dir = 'voice/'

@route('/tts', method='POST')
def do_tts():
#    postValue = request.POST.decode('utf-8')
    text = request.POST.get('text').decode('utf-8')
    if text is None:
      return { 'success' : False}
    print(text)
    # do tts
    filename = time.strftime('%Y%m%d-%H%M%S-',time.localtime(time.time())) + str(random.randint(0,999)).zfill(4) + '.wav'
    speak(filename, text)
    return { 'success' : True, 'path' : '/voice/' + filename }

@route('/voice/<filename>')
def tts(filename):
    return static_file(filename, root='./voice')

def speak(filename, text):
    print('file: ' + output_dir + filename)
    filestream.open(output_dir + filename, 3, False)   
    speaker.AudioOutputStream = filestream
    speaker.Speak(text)
    filestream.close()

# run(host='0.0.0.0', port=8080, debug=True, reloader=True)


class WinService(win32serviceutil.ServiceFramework): 
 
    _svc_name_ = "TTS Service"
    _svc_display_name_ = "TTS Service"
    _svc_description_ = "This is a Windows TTS service"
 
    def __init__(self, args): 
        win32serviceutil.ServiceFramework.__init__(self, args) 
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.logger = self._getLogger()
        self.run = True
        
    def _getLogger(self):
        
        logger = logging.getLogger('[TTSService]')
        
        this_file = inspect.getfile(inspect.currentframe())
        dirpath = os.path.abspath(os.path.dirname(this_file))
        handler = logging.FileHandler(os.path.join(dirpath, "service.log"))
        
        formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)
        
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        
        return logger
 
    def SvcDoRun(self):
        import time
        self.logger.info("service is run....") 
        #while self.run:
        #    self.logger.info("I am runing....")
        #    time.sleep(2)
        run(host='0.0.0.0', port=8080, debug=True, reloader=True)
            
    def SvcStop(self): 
        self.logger.info("service is stop....")
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING) 
        win32event.SetEvent(self.hWaitStop) 
        self.run = False
 
if __name__=='__main__': 
    win32serviceutil.HandleCommandLine(WinService)