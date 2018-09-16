# -*- coding: utf-8 -*-
#Vipro Bot

import everline
from everline.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
from threading import Thread
from googletrans import Translator
from gtts import gTTS
import time,random,sys,json,codecs,threading,glob,urllib,urllib2,urllib3,re,ast,os,subprocess,requests,tempfile

rjbots = everline.LINE()
#rjbots.login(qr=True)
rjbots.login(token='Ewkf0p2ZhZYlrMQNOSK7.tQck1t3+K0hhveBefdLZLW.Cqjj7mdHQrkJgmhjPYDW0DCmorP1+AZJBhTTvt1epYU=') 
rjbots.loginResult() 
print "rjbots-Login Success\n\n=====[Sukses Login]====="

reload(sys)
sys.setdefaultencoding('utf-8')

selfMessage ="""
╔═════════════════════════
║            👿️☆☞ S E L F ☜☆👿️
╠═════════════════════════
╠➩👿️〘Hi〙
╠➩👿️〘Me〙
╠➩👿️〘Mymid〙
╠➩👿️〘Mid @〙
╠➩👿️〘SearchID (ID LINE)〙
╠➩👿️〘Checkdate (DD/MM/YY)〙
╠➩👿️〘Kalender
╠➩👿️〘Steal contact〙
╠➩👿️〘Pp @〙
╠➩👿️〘Cover @〙
╠➩👿️〘Auto like〙
╠➩👿️〘Sbc Text〙
╠➩👿️〘Cbc Text〙
╠➩👿️〘Gbc Text〙
╠➩👿️〘Bio @〙
╠➩👿️〘Info @〙
╠➩👿️〘Name @〙
╠➩👿️〘Profile @〙
╠➩👿️〘Contact @〙
╠➩👿️〘Getvid @〙
╠➩👿️〘Friendlist〙
╠➩👿️〘Micadd @〙
╠➩👿️〘Micdel @〙
╠➩👿️〘Miclist〙
╠═════════════════════════
║             👿 By : REBOTE 👿
╚═════════════════════════
"""

botMessage ="""
╔═════════════════════════
║             👿️☆☞ B O T ☜☆👿️
╠═════════════════════════
╠➩👿️〘Absen〙
╠➩👿️〘Respon〙
╠➩👿️〘Runtime〙
╠➩👿️〘copy @〙
╠➩👿️〘Copycontact〙
╠➩👿️〘Mybackup〙
╠➩👿️〘Mybio (Text)〙
╠➩👿️〘Myname (Text)〙
╠➩👿️〘@bye〙
╠➩👿️〘Bot on/off〙
╠═════════════════════════
║             👿 By : REBOTE 👿
╚═════════════════════════
"""

mediaMessage ="""
╔═════════════════════════
║           👿️☆☞ M E D I A ☜☆👿️
╠═════════════════════════
╠➩👿️〘Gift〙
╠➩👿️〘Giftbycontact〙
╠➩👿️〘Gif gore〙
╠➩👿️〘Google (Text)〙
╠➩👿️〘Playstore NamaApp〙
╠➩👿️〘Fancytext Text〙
╠➩👿️〘musik Judul-Penyanyi〙
╠➩👿️〘lirik Judul-Penyanyi〙
╠➩👿️〘musrik Judul-Penyanyi〙
╠➩👿️〘ig UrsnameInstagram〙
╠➩👿️〘Checkig UrsnameInstagram〙
╠➩👿️〘apakah Text (Kerang Ajaib)〙
╠➩👿️〘kapan Text (Kerang Ajaib)〙
╠➩👿️〘hari Text (Kerang Ajaib)〙
╠➩👿️〘berapa Text (Kerang Ajaib)〙
╠➩👿️〘berapakah Text〙
╠➩👿️〘Youtube Judul Video〙
╠➩👿️〘Youtubevideo Judul Video〙
╠➩👿️〘Youtubesearch:0 Judul Video〙
╠➩👿️〘Image NamaGambar〙
╠➩👿️〘Say Text〙
╠➩👿️〘Say-en Text〙
╠➩👿️〘Say-jp Text〙
╠➩👿️〘Tr-id Text (Translate En Ke ID〙
╠➩👿️〘Tr-en Text (Translate ID Ke En〙
╠➩👿️〘Tr-th Text (Translate ID Ke Th〙
╠➩👿️〘Id@en Text (Translate ID Ke En〙
╠➩👿️〘Id@th Text (Translate ID Ke TH〙
╠➩👿️〘En@id Text (Translate En Ke ID〙
╠═════════════════════════
║             👿 By : REBOTE 👿
╚═════════════════════════
"""

groupMessage ="""
╔═════════════════════════
║           👿️☆☞ G R O U P ☜☆👿️
╠═════════════════════════
╠➩👿️〘Welcome〙
╠➩👿️〘Say welcome〙
╠➩👿️〘Invite creator〙
╠➩👿️〘Setview/Cctv〙
╠➩👿️〘Viewseen/Ciduk〙
╠➩👿️〘Gn: (NamaGroup)〙
╠➩👿️〘Tag all〙
╠➩👿️〘lurk on/off〙
╠➩👿️〘lurkers〙
╠➩👿️〘Recover〙
╠➩👿️〘Cancel〙
╠➩👿️〘Cancelall〙
╠➩👿️〘Gcreator〙
╠➩👿️〘Ginfo〙
╠➩👿️〘Gurl〙
╠➩👿️〘List group〙
╠➩👿️〘Pict group: (NamaGroup)〙
╠➩👿️〘Spam: (Text)〙
╠➩👿️〘Add all〙
╠➩👿️〘Kick: (Mid)〙
╠➩👿️〘Invite: (Mid)〙
╠➩👿️〘Invite〙
╠➩👿️〘Memlist〙
╠➩👿️〘Getgroup image〙
╠➩👿️〘Urlgroup Image〙
╠═════════════════════════
║            👿 By : REBOTE 👿️
╚═════════════════════════
"""
vip="u9022c2960c0aa9c1fec7f21b86838b56"

setMessage ="""
╔═════════════════════════
║              👿️☆☞ S E T ☜☆👿️
╠═════════════════════════
╠➩👿️〘Notif on/off〙
╠➩👿️〘Mimic on/off〙
╠➩👿️〘Url on/off〙
╠➩👿️〘Alwaysread on/off〙
╠➩👿️〘Sider on/off〙
╠➩👿️〘Contact on/off〙
╠➩👿️〘Sticker on〙
╠➩👿️〘Simisimi on/off〙
╠═════════════════════════
║            👿 By : REBOTE 👿️️
╚═════════════════════════
"""

creatorMessage ="""
╔═════════════════════════
║         👿️☆☞ C R E A T O R ☜☆👿️
╠═════════════════════════
╠➩👿️〘Crash〙
╠➩👿️〘Kickall〙
╠➩👿️〘Bc: (Text)〙
╠➩👿️〘Join group: (NamaGroup〙
╠➩👿️〘Leave group: (NamaGroup〙
╠➩👿️〘Leave all group〙
╠➩👿️〘Tag on/off〙
╠➩👿️〘Bot restart〙
╠➩👿️〘Turn off〙
╠═════════════════════════
║            👿 By : REBOTE 👿
╚═════════════════════════
"""

adminMessage ="""
╔═════════════════════════
║            👿️☆☞ A D M I N ☜☆👿️
╠═════════════════════════
╠➩👿️〘Allprotect on/off〙
╠➩👿️〘Ban〙
╠➩👿️〘Unban〙
╠➩👿️〘Ban @〙
╠➩👿️〘Unban @〙
╠➩👿️〘Ban list〙
╠➩👿️〘Clear ban〙
╠➩👿️〘Kill〙
╠➩👿️〘Kick @〙
╠➩👿️〘Set member: (Jumblah)〙
╠➩👿️〘Ban group: (NamaGroup〙
╠➩👿️〘Del ban: (NamaGroup〙
╠➩👿️〘List ban〙
╠➩👿️〘Kill ban〙
╠➩👿️〘Glist〙
╠➩👿️〘Glistmid〙
╠➩👿️〘Details group: (Gid)〙
╠➩👿️〘Cancel invite: (Gid)〙
╠➩👿️〘Invitemeto: (Gid)〙
╠➩👿️〘Acc invite〙
╠➩👿️〘Removechat〙
╠➩👿️〘Qr on/off〙
╠➩👿️〘Autokick on/off〙
╠➩👿️〘Autocancel on/off〙
╠➩👿️〘Invitepro on/off〙
╠➩👿️〘Join on/off〙
╠➩👿️〘Joincancel on/off〙
╠➩👿️〘Respon1 on/off〙
╠➩👿️〘Respon2 on/off〙
╠➩👿️〘Respon3 on/off〙
╠➩👿️〘Responkick on/off〙
╠═════════════════════════
║            👿 By : REBOTE 👿
╚═════════════════════════
"""

helpMessage ="""
╔═════════════════════════
║              👿️☆☞ H E L P ☜☆👿️
╠═════════════════════════
╠➩👿️〘Help self〙
╠➩👿️〘Help bot〙
╠➩👿️〘Help group〙
╠➩👿️〘Help set〙
╠➩👿️〘Help media〙
╠➩👿️〘Help admin〙
╠➩👿️〘Help creator〙
╠➩👿️〘Owner〙
╠➩👿️〘Speed〙
╠➩👿️〘Speed test〙
╠➩👿️〘Status〙
╠═════════════════════════
║            👿 By : REBOTE 👿️
╚═════════════════════════
"""

KAC=[rjbots]
mid = rjbots.getProfile().mid
Bots=[mid]
Creator=["u9022c2960c0aa9c1fec7f21b86838b56","uc03c29a2aae81e699077c554be4941a5","ud1f8811d3fa1f249aa9c72b2f7cf1ac7","u0c03cef42e029d12333f241ff0dc182f","udf828a6bd8b1cdcfb9234288caf61550","ue3d9c213fd973f980bc0cdc73aa764a4","ua22116516aeabdbb414a7e4e16825538"]
admin=["u9022c2960c0aa9c1fec7f21b86838b56","uc03c29a2aae81e699077c554be4941a5","ud1f8811d3fa1f249aa9c72b2f7cf1ac7","u0c03cef42e029d12333f241ff0dc182f","u60c6f1f3fdcbdd3b2e399acf63383cdb","udf828a6bd8b1cdcfb9234288caf61550","u4dd6e73f5ae73f0f40761e2d09ea32ae","ue3d9c213fd973f980bc0cdc73aa764a4","ua22116516aeabdbb414a7e4e16825538"]

contact = rjbots.getProfile()
backup1 = rjbots.getProfile()
backup1.displayName = contact.displayName
backup1.statusMessage = contact.statusMessage                        
backup1.pictureStatus = contact.pictureStatus

responsename = rjbots.getProfile().displayName


wait = {
    "LeaveRoom":True,
    "Bot":True,
    "AutoJoin":False,
    "AutoJoinCancel":False,
    "memberscancel":10,
    "Members":30,
    "AutoCancel":False,
    "AutoKick":False,
    'pap':{},
    'invite':{},
    'steal':{},
    'gift':{},
    'copy':{},    
    'likeOn':{},
    'detectMention':False,
    'detectMention2':True,
    'detectMention3':False,
    'kickMention':False,  
    'sticker':False,  
    'timeline':True,
    "Timeline":True,
    "comment":"Bot Auto Like ©By : RJ`Bõtš\nContact Me : 👉 line.me/ti/p/~iwongtea10",    
    "commentOn":True,
    "commentBlack":{},
    "message":"Thx For Add Me (^_^)\nInvite Me To Your Group ヘ(^_^)ヘ",    
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Qr":False,
    "Contact":False,
    "Sambutan":False,
    "inviteprotect":False,    
    "alwaysRead":False,    
    "Sider":{},
    "Simi":{},    
    "lang":"JP",
    "BlGroup":{}
}

settings = {
    "simiSimi":{}
    }
    
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}    

wait2 = {
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
    }
    
mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }    

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request    
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
            
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content


def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)      
    
def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False    

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image
     
def sendAudio(self, to_, path):
       M = Message()
       M.text = None
       M.to = to_
       M.contentMetadata = None
       M.contentPreview = None
       M.contentType = 3
       M_id = self._client.sendMessage(0,M).id
       files = {
             'file': open(path,  'rb'),
       }
    
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
    
def sendImage(self, to_, path):
      M = Message(to=to_, text=None, contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M2 = self._client.sendMessage(0,M)
      M_id = M2.id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('https://obs-sg.line-apps.com/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True


def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except:
         try:
            self.sendImage(to_, path)
         except Exception as e:
            raise e

def sendAudioWithURL(self, to_, url):
        path = self.downloadFileWithURL(url)
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise Exception(e)

def sendAudioWithUrl(self, to_, url):
        path = '%s/pythonLine-%1.data' % (tempfile.gettempdir(), randint(0, 9))
        r = requests.get(url, stream=True, verify=False)
        if r.status_code == 200:
           with open(path, 'w') as f:
              shutil.copyfileobj(r.raw, f)
        else:
           raise Exception('Download audio failure.')
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise e
            
def downloadFileWithURL(self, fileUrl):
        saveAs = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
        r = self.get_content(fileUrl)
        if r.status_code == 200:
            with open(saveAs, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            return saveAs
        else:
            raise Exception('Download file failure.')

def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] 👋"
    try:
       rjbots.sendMessage(msg)
    except Exception as error:
       print error          
                        
       

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


def bot(op):
    try:

        if op.type == 0:
            return

        if op.type == 5:
           if wait["autoAdd"] == True:
              rjbots.findAndAddContactsByMid(op.param1)
              if(wait["message"]in[""," ","\n",None]):
                pass
              else:
                rjbots.sendText(op.param1,str(wait["message"]))


        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e
	
	    if op.type == 55:
                try:
                     if op.param1 in wait2['readPoint']:     
                         if op.param2 in wait2['readMember'][op.param1]:
                              pass
                         else:
                              wait2['readMember'][op.param1] += op.param2
                         wait2['ROM'][op.param1][op.param2] = op.param2
                         with open('sider.json', 'w') as fp:
                          json.dump(wait2, fp, sort_keys=True, indent=4)
                     else:
                         pass
                except:
                    pass
	      
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = rjbots.getContact(op.param2).displayName
#                            Name = summon(op.param2)
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        rjbots.sendText(op.param1, "╔══════════════╗\n╠❂➣" + Name  + "\n╠❂➣Woww Ada Yang Untiiip. . .\n╠❂➣Chat Kek Idiih (-__-)\n╚══════════════╝")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                    else:
                                        rjbots.sendText(op.param1, "╔══════════════╗\n╠❂➣Dor " + Name  + "\n╠❂➣Dor Kemana Aja. . .\n╠❂➣Chat sini (-__-)\n╚══════════════╝")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                else:
                                    rjbots.sendText(op.param1, "╔══════════════╗\n╠❂➣" + Name + "\n╠❂➣Mau Kemana ???\n╠❂➣Sini Gabung Chat...\n╚══════════════╝")
                                    time.sleep(0.2)
                                    summon(op.param1,[op.param2])
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass 

        if op.type == 22:
            rjbots.leaveRoom(op.param1)

        if op.type == 21:
            rjbots.leaveRoom(op.param1)


        if op.type == 13:
	    print op.param3
            if op.param3 in mid:
		if op.param2 in Creator:
		    rjbots.acceptGroupInvitation(op.param1)

		    
	    if mid in op.param3:	        
                if wait["AutoJoinCancel"] == True:
		    G = vipro.getGroup(op.param1)
                    if len(G.members) <= wait["memberscancel"]:
                        rjbots.acceptGroupInvitation(op.param1)
                        rjbots.sendText(op.param1,"Maaf " + vipro.getContact(op.param2).displayName + "\nMember Kurang Dari 30 Orang\nUntuk Info, Silahkan Chat Owner Kami!")
                        rjbots.leaveGroup(op.param1)                        
		    else:
                        rjbots.acceptGroupInvitation(op.param1)
			rjbots.sendText(op.param1,"☆Ketik ☞Help☜ Untuk Bantuan☆\n☆Harap Gunakan Dengan Bijak ^_^ ☆")
                        		    
 
	    if mid in op.param3:
                if wait["AutoJoin"] == True:
		    G = rjbots.getGroup(op.param1)
                    if len(G.members) <= wait["Members"]:
                        rjbots.rejectGroupInvitation(op.param1)
		    else:
                        rjbots.acceptGroupInvitation(op.param1)
			rjbots.sendText(op.param1,"☆Ketik ☞Help☜ Untuk Bantuan☆\n☆Harap Gunakan Dengan Bijak ^_^ ☆")
	    else:
                if wait["AutoCancel"] == True:
		    if op.param3 in Bots:
			pass
		    else:
                        rjbots.cancelGroupInvitation(op.param1, [op.param3])
		else:
		    if op.param3 in wait["blacklist"]:
			rjbots.cancelGroupInvitation(op.param1, [op.param3])
			rjbots.sendText(op.param1, "Blacklist Detected")
		    else:
			pass
			
        if op.type == 13:
            if op.param2 not in Creator:
             if op.param2 not in admin:
              if op.param2 not in Bots:
                if op.param2 in Creator:
                 if op.param2 in admin:
                  if op.param2 in Bots:
                    pass
                elif wait["inviteprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    rjbots.cancelGroupInvitation(op.param1,[op.param3])
                    rjbots.kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Creator:
                     if op.param2 not in admin:
                      if op.param2 not in Bots:
                        if op.param2 in Creator:
                         if op.param2 in admin:
                          if op.param2 in Bots:
                            pass

        if op.type == 19:
		if wait["AutoKick"] == True:
		    try:
			if op.param3 in Creator:
			 if op.param3 in admin:
			  if op.param3 in Bots:
			      pass
		         if op.param2 in Creator:
		          if op.param2 in admin:
		           if op.param2 in Bots:
		               pass
		           else:
		               rjbots.kickoutFromGroup(op.param1,[op.param2])
		               if op.param2 in wait["blacklist"]:
		                   pass
		        else:
			    vipro.inviteIntoGroup(op.param1,[op.param3])
		    except:
		        try:
			    if op.param2 not in Creator:
			        if op.param2 not in admin:
			            if op.param2 not in Bots:
                                        vipro.kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        rjbots.inviteIntoGroup(op.param1,[op.param3])
		        except:
			    print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Creator:
			        if op.param2 in admin:
			            if op.param2 in Bots:
			              pass
			    else:
                                wait["blacklist"][op.param2] = True
		    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Creator:
		            if op.param2 in admin:
		                if op.param2 in Bots:
			             pass
		        else:
                            wait["blacklist"][op.param2] = True
		else:
		    pass


                if mid in op.param3:
                    if op.param2 in Creator:
                      if op.param2 in Bots:
                        pass
                    try:
                        rjbots.kickoutFromGroup(op.param1,[op.param2])
			rjbots.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    rjbots.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

 
                if Creator in op.param3:
                  if admin in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        rjbots.kickoutFromGroup(op.param1,[op.param2])
			rjbots.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    if op.param2 not in Bots:
                                rjbots.kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        rjbots.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    rjbots.inviteIntoGroup(op.param1,[op.param3])
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True 

        if op.type == 11:
            if wait["Qr"] == True:
		if op.param2 in Creator:
		 if op.param2 in admin:
		  if op.param2 in Bots:
		   pass		
		else:
                    rjbots.kickoutFromGroup(op.param1,[op.param2])
            else:
                pass


        if op.type == 17:
          if wait["Sambutan"] == True:
            if op.param2 in Creator:
                return
            ginfo = rjbots.getGroup(op.param1)
            contact = rjbots.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            rjbots.sendText(op.param1,"╔═══════════════╗\n╠❂➣ Hallo " + vipro.getContact(op.param2).displayName + "\n╠❂➣ Welcome To \n╠❂➣☞ " + str(ginfo.name) + " ☜" + "\n╠❂➣ Budayakan Cek Note\n╠❂➣ Dan Semoga Betah Disini ^_^\n╚═══════════════╝")
            c = Message(to=op.param1, from_=None, text=None, contentType=13)
            c.contentMetadata={'mid':op.param2}
            rjbots.sendMessage(c)  
            rjbots.sendImageWithURL(op.param1,image)
            d = Message(to=op.param1, from_=None, text=None, contentType=7)
            d.contentMetadata={
                                    "STKID": "13269548",
                                    "STKPKGID": "1",
                                    "STKVER": "1329191" }                
            rjbots.sendMessage(d)             
            print "MEMBER JOIN TO GROUP"

        if op.type == 15:
          if wait["Sambutan"] == True:
            if op.param2 in Creator:
                return
            rjbots.sendText(op.param1,"╔═══════════════╗\n╠❂➣Good Bye╠❂➣ " + vipro.getContact(op.param2).displayName +  "\n╠❂➣Sampai Ketemu Lagi . . . (p′︵‵。) 🤗\n╚═══════════════╝")
            d = Message(to=op.param1, from_=None, text=None, contentType=7)
            d.contentMetadata={
                                    "STKID": "13269542",
                                    "STKPKGID": "1",
                                    "STKVER": "1329191" }                
            rjbots.sendMessage(d)                  
            print "MEMBER HAS LEFT THE GROUP"
            
        if op.type == 26:
            msg = op.message      

            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        rjbots.sendText(msg.to,text)             
            
            
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                rjbots.sendText(msg.to,data['result']['response'].encode('utf-8'))

            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = rjbots.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Aku Bilang Jangan Ngetag Lagi " + cName + "\nAku Kick Kamu! Sorry, Byee!!!"]
                     ret_ = random.choice(balas)                     
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  rjbots.sendText(msg.to,ret_)
                                  rjbots.kickoutFromGroup(msg.to,[msg.from_])
                                  break                              
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = rjbots.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Dorr",cName + " Hahahaha?",cName + " Wew Jomblo Tag", cName + " Ciluk Baaa","Lagi Istrhat Bos " + cName, "Ahhaayy Kangen Ya " + cName, "Bagi Tikel Ya " + cName + "?", "Ada Perlu Apa " + cName + "?","Dor " + cName + " Hadir Bos"]
                     ret_ = random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  rjbots.sendText(msg.to,ret_)
                                  break   
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention2"] == True:          
                    contact = rjbots.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["╔═════════════╗\n╠❂➣Dorr\n╠❂➣ " + cName + " \n╠❂➣Jones Tag Hehehe!\n╚═════════════╝"]
                    ret_ = random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  rjbots.sendText(msg.to,ret_)
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": "51626498",
                                                       "STKPKGID": "11538",
                                                       "STKVER": "1" }
                                  rjbots.sendMessage(msg)                                
                                  break
                              
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention3"] == True:          
                    contact = rjbots.getContact(msg.from_)
                    cName = contact.displayName
                    balas = ["╔═════════════╗\n╠❂➣ " + cName + ", \n╠❂➣ Mau Lihat Pp nya\n╚═════════════╝"]
                    balas1 = "╔═════════════╗\n╠❂➣Ini Pp Nya Ciluk Baaa. . .\n╚═════════════╝"
                    ret_ = random.choice(balas)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                           if mention['M'] in Bots:
                                  rjbots.sendText(msg.to,ret_)
                                  rjbots.sendText(msg.to,balas1)
                                  rjbots.sendImageWithURL(msg.to,image)
                                  msg.contentType = 7   
                                  msg.text = None
                                  msg.contentMetadata = {
                                                       "STKID": "51626498",
                                                       "STKPKGID": "11538",
                                                       "STKVER": "1" }
                                  rjbots.sendMessage(msg)                                
                                  break      

        if op.type == 26:
            msg = op.message                                  
                              
            if msg.text in ["Bot on"]:
                wait["Bot"] = True
                rjbots.sendText(msg.to,"Bot Sudah On Kembali.")  

        if op.type == 26:
          if wait["Bot"] == True:    
            msg = op.message
            
            
            if msg.contentType == 7:
              if wait["sticker"] == True:
                msg.cont.entType = 0
                stk_id = msg.contentMetadata['STKID']
                stk_ver = msg.contentMetadata['STKVER']
                pkg_id = msg.contentMetadata['STKPKGID']
                filler = "『 Sticker Check 』\nSTKID : %s\nSTKPKGID : %s\nSTKVER : %s\n『 Link 』\nline://shop/detail/%s" % (stk_id,pkg_id,stk_ver,pkg_id)
                rjbots.sendText(msg.to, filler)
                wait["sticker"] = False
            else:
                pass              

            if wait["alwaysRead"] == True:
                if msg.toType == 0:
                    rjbots.sendChatChecked(msg.from_,msg.id)
                else:
                    rjbots.sendChatChecked(msg.to,msg.id)
                    
                    
            if msg.contentType == 16:
                if wait['likeOn'] == True:
                     url = msg.contentMetadata["postEndUrl"]
                     rjbots.like(url[25:58], url[66:], likeType=1005)
                     rjbots.comment(url[25:58], url[66:], wait["comment"])
                     rjbots.sendText(msg.to,"Like Success")                     
                     wait['likeOn'] = False


            if msg.contentType == 13:
                if wait["wblacklist"] == True:
		    if msg.contentMetadata["mid"] not in admin:
                        if msg.contentMetadata["mid"] in wait["blacklist"]:
                            rjbots.sendText(msg.to,"Sudah")
                            wait["wblacklist"] = False
                        else:
                            wait["blacklist"][msg.contentMetadata["mid"]] = True
                            wait["wblacklist"] = False
                            rjbots.sendText(msg.to,"Ditambahkan")
		    else:
			rjbots.sendText(msg.to,"Admin Detected~")
			

                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        rjbots.sendText(msg.to,"Terhapus")
                        wait["dblacklist"] = False

                    else:
                        wait["dblacklist"] = False
                        rjbots.sendText(msg.to,"Tidak Ada Black List") 
            
                    
 
                elif wait["Contact"] == True:
                     msg.contentType = 0
                     rjbots.sendText(msg.to,msg.contentMetadata["mid"])
                     if 'displayName' in msg.contentMetadata:
                         contact = rjbots.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = rjbots.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         rjbots.sendText(msg.to,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nStatus:\n" + contact.statusMessage + "\n\nPhoto Profile:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nPhoto Cover:\n" + str(cu))
                     else:
                         contact = rjbots.getContact(msg.contentMetadata["mid"])
                         try:
                             cu = rjbots.channel.getCover(msg.contentMetadata["mid"])
                         except:
                             cu = ""
                         rjbots.sendText(msg.to,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nStatus:\n" + contact.statusMessage + "\n\nPhoto Profile:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nPhoto Cover:\n" + str(cu))


 
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = rjbots.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        rjbots.sendText(msg.to,"[Group name]\n" + str(ginfo.name) + "\n\n[Gid]\n" + msg.to + "\n\n[Group creator]\n" + gCreator + "\n\n[Profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "members\nPending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        rjbots.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        rjbots.sendText(msg.to,"Can not be used outside the group")
                    else:
                        rjbots.sendText(msg.to,"Not for use less than group")
                        

 
            elif msg.text is None:
                return
 
            elif msg.text in ["Creator","Owner"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "ue5191af677d7c0c014af4214d5361fd1"}
                rjbots.sendMessage(msg)
		rjbots.sendText(msg.to,"Itu Majikan Kami (^_^)")

 

	    elif msg.text in ["Group creator","Gcreator","gcreator"]:
		ginfo = rjbots.getGroup(msg.to)
		gCreator = ginfo.creator.mid
                msg.contentType = 13
                msg.contentMetadata = {'mid': gCreator}
                rjbots.sendMessage(msg)
		rjbots.sendText(msg.to,"Itu Yang Buat Grup Ini")
 

                
            elif msg.contentType == 16:
                if wait["Timeline"] == True:
                    msg.contentType = 0
                    msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    rjbots.sendText(msg.to,msg.text)

            
            if msg.contentType == 13:
                if wait["steal"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = rjbots.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Stealed"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                rjbots.findAndAddContactsByMid(target)
                                contact = vipro.getContact(target)
                                cu = vipro.channel.getCover(target)
                                path = str(cu)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                rjbots.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nBio :\n" + contact.statusMessage)
                                rjbots.sendText(msg.to,"Profile Picture " + contact.displayName)
                                rjbots.sendImageWithURL(msg.to,image)
                                rjbots.sendText(msg.to,"Cover " + contact.displayName)
                                rjbots.sendImageWithURL(msg.to,path)
                                wait["steal"] = False
                                break
                            except:
                                    pass


            if msg.contentType == 13:
                if wait["gift"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = rjbots.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Gift"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                rjbots.sendText(msg.to,"Gift Sudah Terkirim!")
                                msg.contentType = 9
                                msg.contentMetadata= {'PRDTYPE': 'STICKER',
                                                         'STKVER': '1',
                                                         'MSGTPL': '1',
                                                         'STKPKGID': '1296261'}
                                msg.to = target
                                msg.text = None
                                rjbots.sendMessage(msg)
                                wait['gift'] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     wait["gift"] = False
                                     break   

                      
            if msg.contentType == 13:
                if wait["copy"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = rjbots.getGroup(msg.to)
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Copy"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        rjbots.sendText(msg.to, "Not Found...")
                        pass
                    else:
                        for target in targets:
                            try:
                                rjbots.CloneContactProfile(target)
                                rjbots.sendText(msg.to, "Copied (^_^)")
                                wait['copy'] = False
                                break
                            except:
                                     msg.contentMetadata = {'mid': target}
                                     wait["copy"] = False
                                     break

            if msg.contentType == 13:
                if wait['invite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = rjbots.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             rjbots.sendText(msg.to, _name + " Berada DiGrup Ini")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 rjbots.findAndAddContactsByMid(target)
                                 rjbots.inviteIntoGroup(msg.to,[target])
                                 rjbots.sendText(msg.to,"Invite " + _name)
                                 wait['invite'] = False
                                 break                              
                             except:             
                                      rjbots.sendText(msg.to,"Limit Invite")
                                      wait['invite'] = False
                                      break
                                  
 
            elif msg.text in ["/Key creator","/help creator","/Help creator"]:
                rjbots.sendText(msg.to,creatorMessage)

            elif msg.text in ["/Key group","/help group","/Help group"]:
                rjbots.sendText(msg.to,groupMessage)

            elif msg.text in ["/Key","/help","/Help"]:
                rjbots.sendText(msg.to,helpMessage)

            elif msg.text in ["/Key self","/help self","/Help self"]:
                rjbots.sendText(msg.to,selfMessage)

            elif msg.text in ["/Key bot","/help bot","/Help bot"]:
                rjbots.sendText(msg.to,botMessage)

            elif msg.text in ["/Key set","/help set","/Help set"]:
                rjbots.sendText(msg.to,setMessage)

            elif msg.text in ["/Key media","/help media","/Help media"]:
                rjbots.sendText(msg.to,mediaMessage)
                
            elif msg.text in ["/Key admin","/help admin","/Help admin"]:
                rjbots.sendText(msg.to,adminMessage)               
                

 
            elif msg.text in ["List group"]:
                    gid = rjbots.getGroupIdsJoined()
                    h = ""
		    jml = 0
                    for i in gid:
		        gn = rjbots.getGroup(i).name
                        h += "♦【%s】\n" % (gn)
		        jml += 1
                    rjbots.sendText(msg.to,"=======[List Group]=======\n"+ h +"\nTotal Group: "+str(jml))
 
	    elif "Ban group: " in msg.text:
		grp = msg.text.replace("Ban group: ","")
		gid = rjbots.getGroupIdsJoined()
		if msg.from_ in admin:
		    for i in gid:
		        h = rjbots.getGroup(i).name
			if h == grp:
			    wait["BlGroup"][i]=True
			    rjbots.sendText(msg.to, "Success Ban Group : "+grp)
			else:
			    pass
		else:
		    rjbots.sendText(msg.to, "Khusus Admin")
 
            elif msg.text in ["List ban","List ban group"]:
		if msg.from_ in admin:
                    if wait["BlGroup"] == {}:
                        rjbots.sendText(msg.to,"Tidak Ada")
                    else:
                        mc = ""
                        for gid in wait["BlGroup"]:
                            mc += "-> " +rjbots.getGroup(gid).name + "\n"
                        rjbots.sendText(msg.to,"===[Ban Group]===\n"+mc)
		else:
		    rjbots.sendText(msg.to, "Khusus Admin")
 
	    elif msg.text in ["Del ban: "]:
		if msg.from_ in admin:
		    ng = msg.text.replace("Del ban: ","")
		    for gid in wait["BlGroup"]:
		        if rjbots.getGroup(gid).name == ng:
			    del wait["BlGroup"][gid]
			    rjbots.sendText(msg.to, "Success del ban "+ng)
		        else:
			    pass
		else:
		    rjbots.sendText(msg.to, "Khusus Admin")
 
            elif "Join group: " in msg.text:
		ng = msg.text.replace("Join group: ","")
		gid = rjbots.getGroupIdsJoined()
		try:
		    if msg.from_ in Creator:
                        for i in gid:
                            h = rjbots.getGroup(i).name
		            if h == ng:
		                rjbots.inviteIntoGroup(i,[Creator])
			        rjbots.sendText(msg.to,"Success Join To ["+ h +"] Group")
			    else:
			        pass
		    else:
		        rjbots.sendText(msg.to,"Khusus Admin")
		except Exception as e:
		    rjbots.sendText(msg.to, str(e))
 
	    elif "Leave group: " in msg.text:
		ng = msg.text.replace("Leave group: ","")
		gid = rjbots.getGroupIdsJoined()
		if msg.from_ in Creator:
                    for i in gid:
                        h = rjbots.getGroup(i).name
		        if h == ng:
			    rjbots.sendText(i,"Bot Di Paksa Keluar Oleh Owner!")
		            rjbots.leaveGroup(i)
			    rjbots.sendText(msg.to,"Success Left ["+ h +"] group")
			else:
			    pass
		else:
		    rjbots.sendText(msg.to,"Khusus Admin")

 
	    elif "Ban group: " in msg.text:
		grp = msg.text.replace("Ban group: ","")
		gid = vipro.getGroupIdsJoined()
		if msg.from_ in admin:
		    for i in gid:
		        h = vipro.getGroup(i).name
			if h == grp:
			    wait["BlGroup"][i]=True
			    vipro.sendText(msg.to, "Success Ban Group : "+grp)
			else:
			    pass
		else:
		    vipro.sendText(msg.to, "Khusus Admin")
 
            elif msg.text in ["List ban","List ban group"]:
		if msg.from_ in admin:
                    if wait["BlGroup"] == {}:
                        vipro.sendText(msg.to,"Tidak Ada")
                    else:
                        mc = ""
                        for gid in wait["BlGroup"]:
                            mc += "-> " +vipro.getGroup(gid).name + "\n"
                        vipro.sendText(msg.to,"===[Ban Group]===\n"+mc)
		else:
		    vipro.sendText(msg.to, "Khusus Admin")
 
	    elif msg.text in ["Del ban: "]:
		if msg.from_ in admin:
		    ng = msg.text.replace("Del ban: ","")
		    for gid in wait["BlGroup"]:
		        if vipro.getGroup(gid).name == ng:
			    del wait["BlGroup"][gid]
			    vipro.sendText(msg.to, "Success del ban "+ng)
		        else:
			    pass
		else:
		    vipro.sendText(msg.to, "Khusus Admin")
 
            elif "Join group: " in msg.text:
		ng = msg.text.replace("Join group: ","")
		gid = vipro.getGroupIdsJoined()
		try:
		    if msg.from_ in Creator:
                        for i in gid:
                            h = vipro.getGroup(i).name
		            if h == ng:
		                vipro.inviteIntoGroup(i,[Creator])
			        vipro.sendText(msg.to,"Success Join To ["+ h +"] Group")
			    else:
			        pass
		    else:
		        rjbots.sendText(msg.to,"Khusus Admin")
		except Exception as e:
		    rjbots.sendText(msg.to, str(e))
 
	    elif "Leave group: " in msg.text:
		ng = msg.text.replace("Leave group: ","")
		gid = rjbots.getGroupIdsJoined()
		if msg.from_ in Creator:
                    for i in gid:
                        h = rjbots.getGroup(i).name
		        if h == ng:
			    rjbots.sendText(i,"Bot Di Paksa Keluar Oleh Owner!")
		            rjbots.leaveGroup(i)
			    rjbots.sendText(msg.to,"Success Left ["+ h +"] group")
			else:
			    pass
		else:
		    rjbots.sendText(msg.to,"Khusus Admin")
 
	    elif "Leave all group" == msg.text:
		gid = rjbots.getGroupIdsJoined()
                if msg.from_ in Creator:
		    for i in gid:
			rjbots.sendText(i,"Bot Di Paksa Keluar Oleh Owner!")
		        rjbots.leaveGroup(i)
		    rjbots.sendText(msg.to,"Success Leave All Group")
		else:
		    rjbots.sendText(msg.to,"Khusus Admin")
		   

            elif "Pict group: " in msg.text:
                saya = msg.text.replace('Pict group: ','')
                gid = rjbots.getGroupIdsJoined()
                for i in gid:
                    h = rjbots.getGroup(i).name
                    gna = rjbots.getGroup(i)
                    if h == saya:
                        rjbots.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)		    
		    
 
            elif msg.text in ["cancelall","Cancelall"]:
                if msg.toType == 2:
                    X = rjbots.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        rjbots.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        rjbots.sendText(msg.to,"Tidak Ada Yang Pending")
                else:
                    rjbots.sendText(msg.to,"Tidak Bisa Digunakan Diluar Group")
 
            elif msg.text in ["Ourl","Url on"]:
                if msg.from_ in admin:            	
                 if msg.toType == 2:
                    X = rjbots.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    rjbots.updateGroup(X)
                    rjbots.sendText(msg.to,"Url Sudah Aktif")
                else:
                    rjbots.sendText(msg.to,"Can not be used outside the group")
 
            elif msg.text in ["Curl","Url off"]:
                if msg.from_ in admin:            	
                 if msg.toType == 2:
                    X = rjbots.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    rjbots.updateGroup(X)
                    rjbots.sendText(msg.to,"Url Sudah Di Nonaktifkan")

                else:
                    rjbots.sendText(msg.to,"Can not be used outside the group")
 
            elif msg.text in ["Join on","Autojoin on"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = True
                    wait["AutoJoinCancel"] = False
                    rjbots.sendText(msg.to,"Auto Join Sudah Aktif")
		else:
		    rjbots.sendText(msg.to,"Khusus Admin")

            elif msg.text in ["Join off","Autojoin off"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = False
                    rjbots.sendText(msg.to,"Auto Join Sudah Di Nonaktifkan")
		else:
		    rjbots.sendText(msg.to,"Khusus Admin")
		    
		    
            elif msg.text in ["Joincancel on","Autojoincancel on"]:
		if msg.from_ in admin:
                    wait["AutoJoinCancel"] = True
                    wait["AutoJoin"] = False
                    rjbots.sendText(msg.to,"Auto Join Cancel Sudah Aktif")
		else:
		    rjbots.sendText(msg.to,"Khusus Admin")

            elif msg.text in ["Joincancel off","Autojoincancel off"]:
		if msg.from_ in admin:
                    wait["AutoJoinCancel"] = False
                    rjbots.sendText(msg.to,"Auto Join Cancel Sudah Di Nonaktifkan")
		else:
		    rjbots.sendText(msg.to,"Khusus Admin")
	

            elif msg.text in ["Respon1 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = True
                    wait["detectMention2"] = False
                    wait["detectMention3"] = False
                    wait["kickMention"] = False
                    rjbots.sendText(msg.to,"Auto Respon1 Sudah Aktif")
		else:
		    rjbots.sendText(msg.to,"Khusus Admin")

            elif msg.text in ["Respon1 off"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    rjbots.sendText(msg.to,"Auto Respon1 Sudah Off")
		else:
		    rjbots.sendText(msg.to,"Khusus Admin")	
		    
		    
            elif msg.text in ["Respon2 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    wait["detectMention2"] = True
                    wait["detectMention3"] = False
                    wait["kickMention"] = False
                    rjbots.sendText(msg.to,"Auto Respon2 Sudah Aktif")
		else:
		    rjbots.sendText(msg.to,"Khusus Admin")
            elif msg.text in ["Respon2 off"]:
		if msg.from_ in admin:
                    wait["detectMention2"] = False
                    rjbots.sendText(msg.to,"Auto Respon2 Sudah Off")
		else:
		    vipro.sendText(msg.to,"Khusus Admin")	
		    

            elif msg.text in ["Respon3 on"]:
		if msg.from_ in admin:
                    wait["detectMention"] = False
                    wait["detectMention2"] = False
                    wait["detectMention3"] = True
                    wait["kickMention"] = False
                    rjbots.sendText(msg.to,"Auto Respon3 Sudah Aktif")
		else:
		    rjbots.sendText(msg.to,"Khusus Admin")

            elif msg.text in ["Respon3 off"]:
		if msg.from_ in admin:
                    wait["detectMention3"] = False
                    rjbots.sendText(msg.to,"Auto Respon3 Sudah Off")
		else:
		    rjbots.sendText(msg.to,"Khusus Admin")	
		    
 
            elif msg.text in ["/Responkick on"]:
		if msg.from_ in admin:
                    wait["kickMention"] = True  
                    wait["detectMention"] = False
                    wait["detectMention2"] = False
                    wait["detectMention3"] = False                    
                    rjbots.sendText(msg.to,"Auto Respon Kick Sudah Aktif")
		else:
		    rjbots.sendText(msg.to,"Khusus Admin")

            elif msg.text in ["Responkick off"]:
		if msg.from_ in admin:
                    wait["kickMention"] = False                    
                    rjbots.sendText(msg.to,"Auto Respon Kick Sudah Off")
		else:
		    rjbots.sendText(msg.to,"Khusus Admin")			  
		    
 
	    elif msg.text in ["Autocancel on"]:
	     if msg.from_ in admin:	        
                wait["AutoCancel"] = True
                rjbots.sendText(msg.to,"Auto Cancel Sudah Aktif")
		print wait["AutoCancel"]
	     else:
		    rjbots.sendText(msg.to,"Khusus Admin")		

	    elif msg.text in ["Autocancel off"]:
	     if msg.from_ in admin:	        
                wait["AutoCancel"] = False
                rjbots.sendText(msg.to,"Auto Cancel Sudah Di Nonaktifkan")
		print wait["AutoCancel"]
	     else:
		    rjbots.sendText(msg.to,"Khusus Admin")	
		    

	    elif msg.text in ["Invitepro on"]:
	     if msg.from_ in admin:	        
                wait["inviteprotect"] = True
                rjbots.sendText(msg.to,"Invite Protect Sudah Aktif")
		print wait["inviteprotect"]
	     else:
		    rjbots.sendText(msg.to,"Khusus Admin")		
#=============================
            elif ("Micadd " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        mimic["target"][target] = True
                        rjbots.sendText(msg.to,"Target ditambahkan!")
                        break
                    except:
                        rjbots.sendText(msg.to,"Fail !")
                        break
                    
            elif ("Micdel " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        del mimic["target"][target]
                        rjbots.sendText(msg.to,"Target dihapuskan!")
                        break
                    except:
                        rjbots.sendText(msg.to,"Fail !")
                        break
                    
            elif msg.text in ["Miclist"]:
                        if mimic["target"] == {}:
                            rjbots.sendText(msg.to,"Nothing")
                        else:
                            mc = "Target Mimic User:\n"
                            for mi_d in mimic["target"]:
                                mc += "?? "+rjbots.getContact(mi_d).displayName + "\n"
                            rjbots.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                        if mimic["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                mimic["copy2"] = "me"
                                rjbots.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                mimic["copy2"] = "target"
                                rjbots.sendText(msg.to,"Mimic change to target")
                            else:
                                rjbots.sendText(msg.to,"I dont know")
            
            elif "Mimic " in msg.text:
                cmd = msg.text.replace("Mimic ","")
                if cmd == "on":
                    if mimic["status"] == False:
                        mimic["status"] = True
                        rjbots.sendText(msg.to,"Reply Message on")
                    else:
                        rjbots.sendText(msg.to,"Sudah on")
                elif cmd == "off":
                    if mimic["status"] == True:
                        mimic["status"] = False
                        rjbots.sendText(msg.to,"Reply Message off")
                    else:
                        rjbots.sendText(msg.to,"Sudah off")



        if op.type == 59:
            print op


    except Exception as error:
        print error


while True:
    try:
        Ops = rjbots.fetchOps(rjbots.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(rjbots.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            rjbots.Poll.rev = max(rjbots.Poll.rev, Op.revision)
            bot(Op)

                        