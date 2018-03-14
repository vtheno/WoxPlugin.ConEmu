#coding=utf-8
from wox import Wox,WoxAPI
#import Parsing as P
import os
import config
class Main(Wox):
    def query(self,key):
        if key.startswith(">>"):
            consequence = key[2:]
        if consequence.startswith(" "):
            consequence = consequence[1:] #P.Parse(key)
        results = []
        item = {
            "Title":"MyWox",
            "SubTitle":"result: {cmd}".format(cmd=consequence),
            "IcoPath":"Image/app.ico",
            "JsonRPCAction":{
                "method":'exec_cmd',
                'parameters':[consequence],#pwd,
            }
        }
        results.append (item)
        return results
    def exec_cmd(self,cmd):
        Exec = 'ConEmuC -GuiMacro:0 '
        Input = 'print("{}\n");'.format(cmd)
        Enter = 'Keys("{Enter}");' # autohotkey keydefine
        #temp = 'ConEmuC -c "{}"'.format(cmd)
        cmd = config.Path + Exec + Input
        run = config.Path + Exec + Enter
        os.system(cmd)
        os.system(run)
        #f = os.popen(run).readlines()
        #WoxAPI.showMsg(f[0],f[0])
if __name__ == "__main__":
    #P.test()
    #print( P.Parse(">>  hello") )
    Main()
