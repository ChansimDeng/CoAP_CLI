import subprocess, sys
import threading

class StartObserve(threading.Thread):
  def __init__(self, node, resource, coapProcess=None):
    threading.Thread.__init__(self, coapProcess=coapProcess)
    self.node = node
    self.resource = resource
    self.coapProcess = coapProcess
    return

  def run(self):
    get_cmd = 'coap -o \"coap://['+self.node+']:5683/g/'+self.resource+'\"'
    try:
      self.coapProcess = subprocess.call(get_cmd, shell=True)
      # retcode = subprocess.call(get_cmd)
      # log.debug(retcode)
      return
    except:
      print "Not success for send out.\n"
      pass

  def stop(self):
    self.coapProcess.terminate()
    self._is_running = False

  def printName(self):
    print self.node

  def getName(self):
    return self.node
    