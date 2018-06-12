from kukibanshee import drone
import elist.elist as elel
import edict.edict as eded
import estring.estring as eses
import tlist.tlist as tltl
import sys
import navegador5.solicitud as nvsoli
import navegador5.file_toolset as nvft
import navegador5.cookie.cookie as nvck
import navegador5.jq as nvjq
import navegador5.body as nvbody
import xxurl.xxurl as xuxu
import random
import xdict.jsfunc as xjs
import math
import base64
import copy
import re
import urllib.parse
from pyquery import PyQuery as pq
import sys
import pexpect
import xdict.ltdict as xlt
from xdict.jprint import convert_token_in_quote
from xdict.jprint import pobj
import html

# 


CFG = {
    '-ip':"http://192.168.1.1",
    '-pw':"",
    '-wanpw':""
}

ACTIONS = {
    "status": {
        "general":"statusPara",
        "lan":"lanPara",
        "wan":"wanParas",
        "wan_stats":"statistLists",
        "wlan":"wlanPara"
    },
    "help" : {
        "auth_reason":"",
        "resp_reason":"",
        "other_reason":""
    },
    "connect":"",
    "disconnect":"",
    "renew":"",
    "release":"",
    "sec_renew":"",
    "sec_release":"",
    "logout":"",
    "login":""
}



def load_config():
    cfg = nvft.read_json(fn="config.cfg",op="r+")
    cfg = eded._extend(cfg,CFG)
    return(cfg)

def get_non_action_params():
    arr = sys.argv[1:]
    d = {}
    i = 0
    while(i<arr.__len__()):
        curr = arr[i]
        cond = (curr in ["-ip","-pw","-wanpw"])
        if(cond):
            i = i+1
            d[curr] = arr[i]
        else:
            i = i + 1
    return(d)

###params priority > config.cfg > CFG

def get_cfg():
    cfg = load_config()
    d = get_non_action_params()
    cfg = eded._extend(d,cfg)
    return(cfg)

def get_base(ip,scheme="http"):
    if("http" in ip):
        base = ip
    else:
        ip = ip.strip("/")
        ip = ip.strip(":")
        ip = ip.strip("/")
        base = scheme+"://" + ip
    return(base)

##python3 mecury.py 
#########################

if(__name__=="__main__"):
    CFG = get_cfg()
else:
    pass

BASE = get_base(CFG['-ip'])
PASSWD = CFG['-pw']


##########################




#######################

URLS = {
    'user_menu':BASE + "/userRpm/MenuRpm.htm",
    'user_index':BASE + "/userRpm/Index.htm",
    'user_wan_cfg':BASE + "/userRpm/WanCfgRpm.htm",
    'user_pppoe_cfg':BASE + "/userRpm/PPPoECfgRpm.htm",
    'frames_logo':BASE + "/frames/logo.htm",
    'frames_banner':BASE + "/frames/banner.htm",
    'wzd_start':BASE + "/userRpm/WzdStartRpm.htm",
    'frames_bottom1':BASE + "/frames/bottom1.htm",
    'frames_bottom2':BASE + "/frames/bottom2.htm",
    'status':BASE + "/userRpm/StatusRpm.htm",
    'css_main':BASE + "/dynaform/css_main.css",
    'common_js':BASE + "/dynaform/common.js",
    'tplink':"http://www.tp-link.com.cn",
    'mecurycom':"http://www.mercurycom.com.cn",
    'wizard1':BASE + "/wizard/wizard1.htm",
    'custom_js':BASE + "/dynaform/custom.js",
    'auth_fail_reason':BASE + "/help/PPPoECfgFailAuthReasonHelpRpm.htm",
    'resp_fail_reason':BASE + "/help/PPPoECfgFailResponseReasonHelpRpm.htm",
    'other_fail_reason':BASE + "/help/PPPoECfgFailOtherReasonHelpRpm.htm"
}


def get_authorization_ckstr(passwd=PASSWD):
    byts = base64.b64encode(("admin:"+passwd).encode('latin1'))
    s = byts.decode("latin-1")
    s = "Basic " + s
    s = urllib.parse.quote(s)
    s = "Authorization=" + s
    return(s)

def get_subtag(ic):
    rslt = nvbody.show_resp_body(ic,"script",coding="gb2312",only_print=False)
    script = rslt[4]['result']
    arr = script.split("\r")
    v = elel.find_all(arr,lambda ele:("document.cookie" in ele))[0]['value']
    v = v.replace('\n',"")
    regex = re.compile('"(.*?);.*"')
    m = regex.search(v)
    subtag = m.group(1)
    return(subtag)

def login(base=BASE,passwd=PASSWD):
    ic,rc = nvsoli.keepalive_init(base)
    ic['url'] = base
    ic = nvsoli.walkon(ic,records_container=rc)
    nvsoli.shutdown(ic)
    ic,rc = nvsoli.keepalive_init(base)
    ckstr = get_authorization_ckstr(passwd)
    ic['url'] = base
    ic['req_head']['Referer'] = base
    ic['req_head']['Cookie'] = ckstr
    ic = nvsoli.walkon(ic,records_container=rc)
    subtag = get_subtag(ic)
    ckstr = drone.append(ckstr,subtag)
    nvsoli.shutdown(ic)
    return(ckstr)


def show_page(ic,coding="gb2312"):
    rslt = nvbody.show_resp_body(ic,coding=coding,only_print=False)
    return(rslt)


def get_page(ckstr,url,base=BASE):
    ic,rc = nvsoli.keepalive_init(base)
    ic['url'] = url
    ic['req_head']['Cookie'] = ckstr
    ic['req_head']['Referer'] = base
    ic = nvsoli.walkon(ic,records_container=rc)
    nvsoli.shutdown(ic)
    return(ic)


def pscp_cmd(fn,un='root',up='root',addr='192.168.75.128'):
    lgcmd = "pscp "
    lgcmd = lgcmd + un + '@' + addr +":"
    lgcmd = lgcmd + '/opt/PY/PY3/MERCURY/'
    lgcmd = lgcmd + fn + " C:\\Users\\DELL\\Desktop\\HOMEWIFI"
    return(lgcmd)

def get_all_pages(ckstr,base=BASE):
    ics = []
    cmds = ""
    for key in URLS:
        fn = key +".html"
        url = URLS[key]
        ic = get_page(ckstr,url,base)
        nvft.write_to_file(fn=fn,op="wb+",content=ic["resp_body_bytes"])
        cmds = cmds + pscp_cmd(fn) + '\nroot\r\n'
        ics.append(ic)
    print(cmds)
    return(ics)



##########################################



################################

statusParaStatusDict = {
   0:"off",
   1:"on"
}


def get_status_para_activeTime(activeTime):
    d = {
        "unDays":0,
        "unHours":0,
        "unMinutes":0,
        "unSeconds":0
    }
    unDays = activeTime//(24*60*60)
    unHours = (activeTime%(24*60*60))//(60*60)
    unMinutes = ((activeTime%(24*60*60))%(60*60))//60
    unSeconds = ((activeTime%(24*60*60))%(60*60))%60
    d["unDays"]=unDays
    d["unHours"]=unHours
    d["unMinutes"]=unMinutes
    d["unSeconds"]=unSeconds
    return(d)

def status_para_l2d(statusPara):
    statusParaDict = {
        "status":statusParaStatusDict[int(statusPara[0])],
        "col":int(statusPara[1]),
        "row":int(statusPara[2]),
        "timeout":int(statusPara[3]),
        "activeTime":get_status_para_activeTime(int(statusPara[4])),
        "fversion":statusPara[5],
        "hversion":statusPara[6]
    }
    return(statusParaDict)



#################################

def get_wan_para_list(wanParas,col,row):
    arr = elel.divide(wanParas,row)
    if(arr[-1].__len__()<row):
        arr.pop(-1)
    else:
        pass
    return(arr)



wanStatusStringArray = [
    " ",
    "disable",
    "timeout",
    "disconnected",
    "normal"
]

wanTypeStringArray = [
    "",
    "DYNAMICIP",
    "STATICIP",
    "PPPoE",
    "802.1X",
    "BPA",
    "L2TP",
    "PPTP",
    "DHCP+"
]

wanLinkModeStringArray = [
    [],
    [None],
    [None,None],
    [
        " ",
        "on_demand",
        "auto",
        "time_based",
        "manually"
    ],
    [None,None,None,None],
    [None,None,None,None,None],
    [
        " ",
        "on_demand",
        "auto",
        "manual"
    ],
    [
        " ",
        "on_demand",
        "auto",
        "manual"
    ],
    [None,None,None,None,None,None,None,None,None]
]

dot1xLoginStringArray  = [ 
    " ",
    "nologin",
    "logging",
    "login"
]

#"dot1xLoginBtn":dot1xLoginButtonStringArray[int(wanPara[5])],
dot1xLoginButtonStringArray = [
    "nodot1x",
    "can-logout-now",
    "can-login-now"
]

DHCPBtnStatusStringArray = [
    "disabled",
    "enabled"
]

DHCPActionStringArray = [
    "disable",
    "release",
    "renew",
    "status"
]

DHCPStringArray = [
    " ",
    "getting",
    "notconnected"
]

linkStatusStringArray = [
    "offline",
    "online",
    "connecting",
    "auth_fail",
    "server_no_resp",
    "unknown",
    "wan_not_connected",
]

# "RenewSecIpBtn":wanPara[18],
# "ReleaseSecIp":wanPara[19],

def wan_para_l2d(wanPara,col,row):
    wanParaDict = {
        "wanStatus":wanStatusStringArray[int(wanPara[0])],
        "mac":wanPara[1],
        "ip":wanPara[2],
        "wanType" :wanTypeStringArray[int(wanPara[3])],
        "wanLinkMode":wanLinkModeStringArray[int(wanPara[3])][int(wanPara[20])],
        "mask":wanPara[4],
        "dot1x":dot1xLoginStringArray[int(wanPara[6])],
        "gateway":wanPara[7],
        "DHCPBtnStatus":DHCPBtnStatusStringArray[int(wanPara[9])],
        "DHCPAction":DHCPActionStringArray[int(wanPara[8])],
        "DHCPStatus":DHCPStringArray[int(wanPara[10])],
        "DNS":wanPara[11],
        "onlineDuration":wanPara[12],
        "linkStatus":linkStatusStringArray[int(wanPara[13])],
        "SecType":wanTypeStringArray[int(wanPara[14])],
        "SecIP":wanPara[15],
        "SecMask":wanPara[16],
        "SecDHCPStat":DHCPStringArray[int(wanPara[17])],
    }
    return(wanParaDict)



####################################


wlanChannelWidthArray = [
    "",
    "20MHz",
    "auto",
    "40MHz"
]

wlanTypeStringArray = [
    " ",
    "11b only",
    "11g only",
    "11n only",
    "11bg mixed",
    "11bgn mixed",
    " "
]

wlanStaDict = {
   0:"off",
   1:"on"
}



wlanWDSStatusDict = {
    0:"off",
    1:"init",
    2:"scan",
    3:"auth",
    4:"asso",
    5:"succ",
    6:"check"
}

def wlan_para_l2d(wlanPara):
    wlanParaDict = {
        "wlanSta":wlanStaDict[int(wlanPara[0])],
        "wlanName":wlanPara[1],
        "wlanChannelManual" : wlanPara[2],
        "wlanMode" :wlanTypeStringArray[int(wlanPara[3])],
        "wlanMac" :wlanPara[4],
        "wlanIp" :wlanPara[5],
        "wlanChannelWidth":wlanChannelWidthArray[int(wlanPara[6])],
        "wlanWDSStatus":wlanWDSStatusDict[int(wlanPara[10])],
        "wlanChannelAuto":int(wlanPara[9]),
        "rateTable":wlanPara[8]
    }
    if(int(wlanPara[2])==0):
        del wlanParaDict["wlanChannelManual"]
    else:
        pass
    if(int(wlanPara[8])==0):
        del wlanParaDict["rateTable"]
    else:
        pass
    return(wlanParaDict)

########
def get_statist_list(statistList,col):
    arr = elel.divide(statistList,4)
    if(arr[-1].__len__()<4):
        arr.pop(-1)
    else:
        pass
    return(arr)

def statist_l2d(statist):
    d = {
        'recv_bytes':int(statist[0]),
        'send_bytes':int(statist[1]),
        'recv_pkts':int(statist[2]),
        'send_pkts':int(statist[3]),
    }
    return(d)

############################

def lan_para_l2d(lanPara):
    d = {
        "lanMac":lanPara[0],
        "lanIP" :lanPara[1],
        "lanMask":lanPara[2]
    }
    return(d)


def get_status(ckstr,url=URLS['status'],coding='gb2312'):
    ic = get_page(ckstr,url)
    rslt = nvbody.show_resp_body(ic,'script',coding=coding,only_print=False)
    arr = xlt.ltdict_to_list(rslt)
    arr = elel.array_map(arr,lambda ele:ele['result'])
    arr = elel.cond_select_all(arr,cond_func=lambda ele:(ele!= None))
    arr = elel.cond_select_all(arr,cond_func=lambda ele:("new Array" in ele))
    arr = elel.array_map(arr,lambda ele:ele.replace('\n','').replace('\r','').replace('\t',''))
    arr = elel.array_map(arr,lambda ele:ele.replace('var','').replace('new Array','').replace('(',"").replace(")","").replace(";",""))
    arr.pop(-1)
    arr = elel.array_map(arr,lambda ele:ele.split("="))
    d = {}
    for each in arr:
        k = each[0].strip("\x20")
        v = each[1].strip("\x20")
        v = convert_token_in_quote(v)
        v = v.split(",")
        v = elel.array_map(v,html.unescape)
        d[k] = v
    spd = status_para_l2d(d['statusPara'])
    wpd = wlan_para_l2d(d['wlanPara'])
    d['statusPara'] = spd
    d['wlanPara'] = wpd
    d['wanParas'] = copy.deepcopy(d['wanPara'])
    del d['wanPara']
    ####
    row = d['statusPara']['row']
    col = d['statusPara']['col']
    wanParas= get_wan_para_list(d['wanParas'],col,row)
    d['wanParas'] = elel.array_map(wanParas,wan_para_l2d,col,row)
    ####
    statistList = copy.deepcopy(d['statistList'])
    del d['statistList']
    statistLists = get_statist_list(statistList,col)
    d['statistLists'] = elel.array_map(statistLists,statist_l2d)
    ###########
    d['lanPara'] = lan_para_l2d(d['lanPara'])
    return(d)

##############################

def load_ckstr():
    try:
        ckstr = nvft.read_file_content(fn="ckstr.record",op="r+")
    except:
        ckstr = login()
        nvft.write_to_file(fn="ckstr.record",op="w+",content=ckstr)
    else:
        pass
    return(ckstr)


def do_actions():
    arr = sys.argv[1:]
    if(arr[0] == '-help'):
        s = '''
            #read from params,-login must be the first
            python3 mercury.py -login -ip "192.168.1.1" -pw "lidapeng" 
            #read from config.cfg
            python3 mercury.py -login
            python3 mercury.py -status
            python3 mercury.py -status wan
            python3 mercury.py -status lan
            python3 mercury.py -status wlan
            python3 mercury.py -status general
            python3 mercury.py -status wan_stats
            python3 mercury.py -status wlan wan lan
        '''
        print(s)
    elif(arr[0] == '-login'):
        ckstr = login()
        nvft.write_to_file(fn="ckstr.record",op="w+",content=ckstr)
    elif(arr[0] == '-status'):
        ckstr = load_ckstr()
        params = arr[1:]
        lngth = params.__len__()
        if(lngth == 0):
            pobj(d)
        else:
            params = elel.array_map(params,lambda ele:ACTIONS['status'][ele])
            d = get_status(ckstr)
            for key in params:
                pobj(d[key])




if(__name__=="__main__"):
    do_actions()
else:
    pass
##@user_menu

##@wizard_start

