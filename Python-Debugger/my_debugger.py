from ctypes import *
from my_debugger_defines import *

kernel32 = windll.kernel32

class debugger():

    def __init__(self):
        self.h_process = None
        self.pid = None
        self.debugger_active = False

    def load(self,path_to_exe):
        print "[+] We have successfully launched the process!"
        print "[+] PID: %d" % process_information.dwProcessId

        #Obtain handle and store for future access
        self.h_process = self.open_process(process_information.dwProcessId)
        