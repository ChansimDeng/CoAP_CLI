import os
from cmd import Cmd
from getMotes import getAllMotes
import restCoAP
import logging

class CoAPCLI(Cmd):
  def __init__(self):

    Cmd.__init__(self)
    self.doc_header = 'Commands: \ngetallmotes \npost \npostall \nobserve'
    self.prompt = '>'
    self.intro = '\nCollectCLI, Welcome!'

    self.mote_lists = []

  def do_getallmotes(self, arg):
    if not arg:
      self.stdout.write("Please provide Border router's mac address.\n")
      return
    try:
      mote_lists = getAllMotes(arg) # get motes from border router website.
      self.stdout.write("====== End of List =======\n")
    except:
      self.stdout.write("Error from getallmotes.\n")

  def do_post(self, arg):
    if not arg:
      self.stdout.write("Please provide node's mac address.\n")
      return

    args = arg.split(' ')

    try:
      node = args[0]
      resource = args[1]
      query = args[2]
      restCoAP.postQueryToNode(node, resource, query)
      self.stdout.write("Successful delivery.\n")
      break
    except:
      self.stdout.write("Error from get.\n")
     
  def do_postall(self, arg):
    if not arg:
      self.stdout.write("Please provide arguments\n")
      return
    
    args = arg.split(' ')
    
    try:
      resource = args[0]
      query = args[1]
      restCoAP.postToAllNode(mote_lists, resource, query)
      self.stdout.write("Successful delivery.\n")
      break
    except:
      self.stdout.write("Error from getall.\n")

  def do_observe(self, arg):
    if not arg:
      self.stdout.write("Please provide node's mac address.\n")
      return

    args = arg.split(' ')
    try:
      node = args[0]
      resource = args[1]
      restCoAP.startObserve(node,resource)
      break
    except:
      self.stdout.write("Error from observe.\n")
      
        
if __name__=="__main__":
  collect_cli = CoAPCLI()
  collect_cli.cmdloop()