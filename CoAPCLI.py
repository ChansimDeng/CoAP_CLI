import os
from cmd import Cmd
from getMotes import getAllMotes
import restCoAP

class CoAPCLI(Cmd):
  def __init__(self):

    Cmd.__init__(self)
    self.doc_header = 'Commands: \ngetallmotes \nget \ngetall \nobserve \nobserveall'
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
      self.stdout.write("Error from getallmotes.")

  def do_get(self, arg):
    if not arg:
      self.stdout.write("Please provide node's mac address.\n")
      return

    args = arg.split(' ')
    
    if len(args) < 2:
      self.stdout.write("Need to typing resource.\n")
      return
    else:
      node = args[0]
      resource = args[1]
      for index in range(0,len(self.mote_lists)):
        if self.mote_lists[index] == node:
          if len(agrs) == 3:
            try:
              query = args[2]
              restCoAP.getQueryToNode(node,resource,query)
            except:
              self.stdout.write("Error from get.\n")
          else:
            self.stdout.write("Most too arguments, Please check it.\n")
        else:
          self.stdout.write("Please check your typing mac address or query.\n")

  def do_getall(self, arg):
    if not arg:
      self.stdout.write("Please provide node's mac address.\n")
      return
    
    args = arg.split(' ')
    
    if len(args) < 1:
      self.stdout.write("Need to typing resource.\n")
      return
    else:
      try:
        resource = args[0]
        query = args[1]
        restCoAP.getToAllNode(mote_lists, resource, query)
      except:
        self.stdout.write("Error from getall.\n")

  def do_observe(self, arg):
    if not arg:
      self.stdout.write("Please provide node's mac address.\n")
      return

      if len(args) < 2:
        self.stdout.write("Need to typing resource.\n")
        return
      else:
        node = args[0]
        resource = args[1]
        for index in range(0,len(self.mote_lists)):
          if self.mote_lists[index] == node:
            if len(agrs) < 2:
              try:
                restCoAP.startObserve(node,resource)
              except:
                self.stdout.write("Error from observe.\n")
            else:
              self.stdout.write("Most too arguments, Please check it.\n")
          else:
            self.stdout.write("Please check your typing mac address or query.\n")
    
        
if __name__=="__main__":
  collect_cli = CoAPCLI()
  collect_cli.cmdloop()