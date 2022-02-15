import pyefun.wxefun as wx
import locale
from coding import *
import os
import configparser

class 窗口1(wx.窗口):
    def __init__(self):
        self.初始化界面()
        self.填充列表()

    def 初始化界面(self):
        #########以下是创建的组件代码#########
        wx.窗口.__init__(self, None, title='Nobihaza Launcher (Pyefun ver.) v1 by 1262917464', size=(576, 640), name='frame', style=wx.窗口边框.普通固定边框& ~(wx.窗口样式.最大化按钮))
        self.容器 = wx.容器(self)
        self.Centre()
        self.窗口1 = self
        
        self.窗口1.背景颜色 = (171, 171, 171, 255)
        self.窗口1.图标 = r'.\resources\新版1262917464.ico'
        self.超级列表框2 = wx.超级列表框(self.容器, size=(544, 480), pos=(8, 8), style=wx.超级列表框样式.报表列表框 | wx.超级列表框样式.图标顶部对齐 | wx.超级列表框样式.显示垂直表格线)
        self.超级列表框2.背景颜色 = (255, 255, 255, 255)
        self.超级列表框2.绑定事件(wx.事件.被双击, self.双击)
        self.按钮1 = wx.按钮(self.容器, size=(136, 40), pos=(8, 496), label='载入列表')
        self.按钮1.绑定事件(wx.事件.被单击, self.按钮1_被单击)
        self.按钮2 = wx.按钮(self.容器, size=(136, 40), pos=(8, 548), label='窗口启动游戏(2K限定)')
        self.按钮2.绑定事件(wx.事件.被单击, self.按钮2_被单击)
        self.按钮3 = wx.按钮(self.容器, size=(136, 40), pos=(152, 496), label='读取本地游戏')
        self.按钮3.绑定事件(wx.事件.被单击, self.按钮3_被单击)
		#########以上是创建的组件代码##########

    #########以下是组件绑定的事件代码#########
    
	
    def 按钮1_被单击(self,event):
        print("按钮1_被单击")
        self.填充列表()
        #print(data[1])
        #self.超级列表框2.插入列(0, "第0列")
        #self.超级列表框2.插入表项(0, "0")
                        
	
    def 按钮3_被单击(self,event):
        print("按钮3_被单击")
        #search(r"X:\2020\Nobita_s_Biohazard(2020)\Game","RPG_RT.exe")
        #print(result)
        self.搜索游戏()

    
    def 按钮2_被单击(self,event):
        print("按钮2_被单击")
        #print(self.超级列表框2.取标题(self.超级列表框2.取现行选中项(),1))
        self.start(self.超级列表框2.取标题(self.超级列表框2.取现行选中项(),2),self.超级列表框2.取标题(self.超级列表框2.取现行选中项(),0))
                        
	
    def 双击(self,event):
        print("超级列表框2_被双击")
        self.start(self.超级列表框2.取标题(self.超级列表框2.取现行选中项(), 2), self.超级列表框2.取标题(self.超级列表框2.取现行选中项(), 0))


	#########以上是组件绑定的事件代码#########
    #def 载入列表:
        #text =
    def 填充列表(self):
        self.超级列表框2.全部删除()
        self.超级列表框2.插入列(0, "路径",2,1)
        self.超级列表框2.插入列(0, "游戏名",2,514)
        self.超级列表框2.插入列(0, "启动参数",2,1)
        #if os.path.isfile("list_utf8.bin") == False and os.path.isfile("list.bin"):
        #    gbk2utf8("list.bin","list_utf8.bin")
        #elif os.path.isfile("list_utf8.bin"):
        #    print("list_utf8.bin存在")
        #else:
        #    return
        if os.path.isfile("list_utf8.bin"):
            with open("list_utf8.bin","r",encoding="utf-8") as f:
                for line in f.readlines():
                    line = line.strip('\n')
                    data = line.split("----")
                    self.超级列表框2.插入表项(0, data[0])
                    self.超级列表框2.置标题(0, 1, data[1])
                    self.超级列表框2.置标题(0, 2, data[2])
        elif os.path.isfile("list.bin"):
            with open("list.bin","r",encoding="gbk") as f:
                for line in f.readlines():
                    line = line.strip('\n')
                    data = line.split("----")
                    self.超级列表框2.插入表项(0, data[0])
                    self.超级列表框2.置标题(0, 1, data[1])
                    self.超级列表框2.置标题(0, 2, data[2])
        else:
            self.搜索游戏()

    def 搜索游戏(self):
        path = os.getcwd() + r"\Game"
        if not os.path.isdir(os.getcwd() + r"\Game"):
            return
        list_bin = "list_utf8.bin"
        with open(list_bin,"w",encoding="utf-8") as list:
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                conf = configparser.RawConfigParser()
                if (os.path.isfile(item_path + "\game.ini")):
                    conf.read(item_path + "\game.ini")
                    if (conf.sections()[0] == "Game"):
                        list.write("0----")
                        if (len(conf.sections()) == 2):
                            list.write(conf['config']['title'])
                        else:
                            list.write(conf['Game']['title'])
                        list.write("----")
                        list.write(item_path + "\Game.exe\n")
                    elif (conf.sections()[0] == "config"):
                        if len(conf['config']) == 3 and conf['config']['maker'] == "mv":
                            list.write("0----")
                            list.write(conf['config']['title'])
                            list.write("----")
                            list.write(item_path + "\game.exe\n")
                        elif len(conf['config']) == 3 and conf['config']['maker'] == "wolf":
                            list.write(conf['config']['applocale'])
                            list.write("----")
                            list.write(conf['config']['title'])
                            list.write("----")
                            list.write(item_path + "\game.exe\n")
                        else:
                            for item in os.listdir(item_path):
                                item_paths = os.path.join(item_path, item)
                                if os.path.isdir(item_paths) and os.path.isfile(item_paths + "\RPG_RT.ini"):
                                    item_path = item_paths
                            list.write(conf['config']['applocale'])
                            list.write("----")
                            list.write(conf['config']['title'])
                            list.write("----")
                            list.write(item_path + "\RPG_RT.exe\n")
                elif (os.path.isfile(item_path + "\RPG_RT.ini")):
                    with open(item_path + "\RPG_RT.ini","r") as f:
                        data = f.read()
                        locale = file_encoding(item_path + "\RPG_RT.ini")
                        if (locale == "GB18030"):
                            list.write("0----")
                        else:
                            list.write("1----")
                        conf.read(item_path + "\RPG_RT.ini", encoding=locale)
                        list.write(conf['RPG_RT']['GameTitle'])
                        list.write("----")
                        list.write(item_path + "\RPG_RT.exe\n")
        self.填充列表()

    def start(self,path,app = "1"):
        cmd = path
        conf = configparser.RawConfigParser()
        if app == "1":
            conf.read("config.ini")
            LE = conf['config']['LE']
            cmd = '"' + LE.replace("%DEFAULT_FOLDER%",os.getcwd()) + '"' + " " + '"' + cmd + '"' + " -" + '"' + "NormalPlay ShowTitle Window" + '"'
        else:
            cmd = '"' + cmd + '"' + r" NormalPlay ShowTitle Window"
        print(cmd)
        os.system("chcp 65001")
        os.system("call " + cmd)


class 应用(wx.App):
    def OnInit(self):
        self.窗口1 = 窗口1()
        self.窗口1.Show(True)
        return True


if __name__ == '__main__':
    app = 应用()
    app.MainLoop()
