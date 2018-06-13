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
import time

# 


CFG = {
    '-ip':"http://192.168.1.1",
    '-pw':"",
    '-wanuser':"",
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
    "fail_help" : {
        "auth_reason":"/help/PPPoECfgFailAuthReasonHelpRpm.htm",
        "resp_reason":"/help/PPPoECfgFailResponseReasonHelpRpm.htm",
        "other_reason":"/help/PPPoECfgFailOtherReasonHelpRpm.htm"
    },
    "connect":"/userRpm/StatusRpm.htm?Connect=%C1%AC%20%BD%D3&wan=",
    "disconnect":"/userRpm/StatusRpm.htm?Disconnect=%B6%CF%20%CF%DF&wan=",
    "renew":"/userRpm/StatusRpm.htm?RenewIp=%B8%FC%20%D0%C2&wan=",
    "release":"/userRpm/StatusRpm.htm?ReleaseIp=%CA%CD%20%B7%C5&wan=",
    "sec_renew":"/userRpm/StatusRpm.htm?RenewSecIp=1&wan=",
    "sec_release":"/userRpm/StatusRpm.htm?ReleaseSecIp=1&wan=",
    "dot1x_logout":"/userRpm/StatusRpm.htm?Login=%B5%C7%20%C2%BC&wan=",
    "dot1x_login":"/userRpm/StatusRpm.htm?Logout=%CD%CB%20%B3%F6&wan=",
    "wan_cfg" : {
<<<<<<< HEAD
        "types":"wantypeinfo",
        "pppoe":"pppoeInf",
        "detect":"wanTypeDetectInfo"
=======
>>>>>>> 2cb2df3c608618267872c390e5b0195ae2420ada
    }
}


def quote_chinese(s,codec='gb2312'):
    bytstrm = s.encode(codec)
    s = eses.bytstrm2hex(bytstrm)
    s = s.replace("\\x","%")
    s = s.upper()
    return(s)



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
<<<<<<< HEAD
    'user_dynamic_cfg':BASE + "/userRpm/WanDynamicIpCfgRpm.htm",
    'user_static_cfg':BASE + "/userRpm/WanStaticIpCfgRpm.htm",
    'user_pppoe_cfg':BASE + "/userRpm/PPPoECfgRpm.htm",
    'user_pppoe_cfg_adv':BASE + "/userRpm/PPPoECfgAdvRpm.htm?Advanced=%B8%DF%BC%B6%C9%E8%D6%C3&wan=",
=======
    'user_pppoe_cfg':BASE + "/userRpm/PPPoECfgRpm.htm",
>>>>>>> 2cb2df3c608618267872c390e5b0195ae2420ada
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
<<<<<<< HEAD
    'other_fail_reason':BASE + "/help/PPPoECfgFailOtherReasonHelpRpm.htm",
    "pppoe_cfg_auth_fail_reason":BASE + "/help/PPPoECfgFailAuthReasonHelpRpm.htm",
    "pppoe_cfg_resp_fail_reason":BASE + "/help/PPPoECfgFailResponseReasonHelpRpm.htm",
    "pppoe_cfg_other_fail_reason":BASE + "/help/PPPoECfgFailOtherReasonHelpRpm.htm"
=======
    'other_fail_reason':BASE + "/help/PPPoECfgFailOtherReasonHelpRpm.htm"
>>>>>>> 2cb2df3c608618267872c390e5b0195ae2420ada
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
    lgcmd = lgcmd + '/opt/PY/PY3/mw316r/'
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

def get_raw_script_dict(ic,coding='gb2312'):
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
    return(d)

def get_status(ckstr,url=URLS['status'],coding='gb2312',**kwargs):
    if('ic' in kwargs):
        ic = kwargs['ic']
    else:
        ic = get_page(ckstr,url)
    d = get_raw_script_dict(ic,coding=coding)
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
    
####################################

<<<<<<< HEAD
 


wanTypeDetectStatDict = {
    0:"HAVE_NOT_DETECTED",
    1:"DETECTIING",
    2:"HAVE_DETECTED",
    3:"DISCONNECTED"
}

wanTypeStringArray2 = [
 'DYNAMICIP',
 'STATICIP',
 'PPPoE',
 '802.1X',
 'BPA',
 'L2TP',
 'PPTP',
 'DHCP+',
 ''
]



def wan_type_detect_l2d(wanTypeDetectInfoArray):
    d = {
        "detected_wan_type":wanTypeStringArray2[int(wanTypeDetectInfoArray[0])],
        "wan_type_detect_stat":wanTypeDetectStatDict[int(wanTypeDetectInfoArray[1])],
        "wait_time":int(wanTypeDetectInfoArray[2]),
    }
    return(d)

def wan_type_info_l2d(wantypeinfo):
    count = int(wantypeinfo[0])
    arr = wantypeinfo[1:]
    arr = elel.divide(arr,2)
    arr = arr[:count]
    tl = elel.array_map(arr,tuple)
    d = tltl.tlist2dict(tl)
    return(d)

linkTypeStringDict2 = {
    1:"on_demand",
    2:"auto",
    3:"on_certain_time",
    4:"manual"
}

specialDialDict = {
    "0":"normal",
    "100":"auto",
    "1":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7
}

def pppoe_if_l2d(pppoeInf,detected_wan_type):
    d = {
    }
    if(int(pppoeInf[0]) != 1):
        d['detected_wan_type'] = wanTypeStringArray2[int(pppoeInf[6])]
    else:
        d['detected_wan_type'] = detected_wan_type
    d['wanuser'] = pppoeInf[7]
    d['wanpw'] = pppoeInf[8]
    d['link_type'] = linkTypeStringDict2[int(pppoeInf[20])]
    d['auto_disconnect_waittime'] = pppoeInf[21]+"minutes"
    d['on_certain_time_from'] = pppoeInf[22]+":" + pppoeInf[23]
    d['on_certain_time_to'] = pppoeInf[24]+":" + pppoeInf[25]
    d['SecType'] = wanTypeStringArray[int(pppoeInf[29])]
    d["sta_ip"] = pppoeInf[30]
    d["sta_mask"] = pppoeInf[31]
    d["dyn_ip"] = pppoeInf[32]
    d["dyn_mask"] = pppoeInf[33]
    d['PPPoELinkStat'] = linkStatusStringArray[int(pppoeInf[26])]
    d["specialDialKindsNum"] = int(pppoeInf[28])
    d["specialDial"] = specialDialDict[pppoeInf[27]]
    d["wan_num"] = int(pppoeInf[5]) + 1
    return(d)

=======
>>>>>>> 2cb2df3c608618267872c390e5b0195ae2420ada
def get_wan_cfg(ckstr,url=URLS['user_wan_cfg'],base=BASE,coding='gb2312',**kwargs):
    ic = req(url,ckstr,base=BASE,referer=URLS['user_menu'])
    rslt = nvbody.show_resp_body(ic,'html body',coding=coding,only_print=False)
    regex = re.compile('"(.*)"')
    m = regex.search(rslt[1]['result'])
    url = base + m.group(1)
    ic = req(url,ckstr,base=BASE,referer=URLS['user_wan_cfg'])
    d = get_raw_script_dict(ic,coding=coding)
<<<<<<< HEAD
    d['wanTypeDetectInfo'] = wan_type_detect_l2d(d['wanTypeDetectInfoArray'])
    del d['wanTypeDetectInfoArray']
    d['wantypeinfo'] = wan_type_info_l2d(d['wantypeinfo'])
    detected_wan_type = d['wanTypeDetectInfo']['detected_wan_type']
    d['pppoeInf'] = pppoe_if_l2d(d['pppoeInf'],detected_wan_type)
    return(d)

=======
    
>>>>>>> 2cb2df3c608618267872c390e5b0195ae2420ada

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

def req(url,ckstr,base=BASE,**kwargs):
    ic,rc = nvsoli.keepalive_init(base)
    ic['url'] = url
    ic['req_head']['Cookie'] = ckstr
    if("referer" in kwargs):
        ic['req_head']['Referer'] = kwargs['referer']
    else:
        ic['req_head']['Referer'] = base
    ic = nvsoli.walkon(ic,records_container=rc)
    nvsoli.shutdown(ic)
    return(ic)

def wait_for_ip(ckstr,wannum,sleep=3):
    time.sleep(sleep)
    d = get_status(ckstr)
    ip = d['wanParas'][wannum-1]['ip']
    cond = "0.0.0.0" in ip
    while(cond):
        time.sleep(sleep)
        d = get_status(ckstr)
        ip = d['wanParas'][wannum-1]['ip']
        cond = "0.0.0.0" in ip
    return(d)

def handle_action(arr,action,base=BASE,debug=False):
    ckstr = load_ckstr()
    params = arr[1:]
    lngth = params.__len__()
    if(lngth == 0):
        wannums = [1]
    else:
        wannums = params
    for i in range(0,wannums.__len__()):
        num = wannums[i]
        ###
        d = get_status(ckstr)
        old_ip = d['wanParas'][num-1]['ip']
        ###
        url = base+ACTIONS[action]+str(num)
        ic = req(url,ckstr)
        d = wait_for_ip(ckstr,num)
        ###
<<<<<<< HEAD
        new_ip = d['wanParas'][num-1]['ip']
        print("old_ip: {0} for wan {1}".format(old_ip,num))
        print("new_ip: {0} for wan {1}".format(new_ip,num))
=======
        print("old_ip: {0} for wan {1}".format(old_ip,num))
        print("new_ip: {0} for wan {1}".format(d['wanParas'][num-1]['ip'],num))
>>>>>>> 2cb2df3c608618267872c390e5b0195ae2420ada
        ###
        if(debug):
            return(ic)
        else:
            pass
<<<<<<< HEAD
        return((old_ip,new_ip))
=======
>>>>>>> 2cb2df3c608618267872c390e5b0195ae2420ada

def do_actions():
    arr = sys.argv[1:]
    if(arr[0] == '-help'):
        s = '''
            #read from params,-login must be the first
            python3 mw316r.py -login -ip "192.168.1.1" -pw "lidapeng" 
            #read from config.cfg
            python3 mw316r.py -login
            python3 mw316r.py -status
            python3 mw316r.py -status wan
            python3 mw316r.py -status lan
            python3 mw316r.py -status wlan
            python3 mw316r.py -status general
            python3 mw316r.py -status wan_stats
            python3 mw316r.py -status wlan wan lan
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
            d = get_status(ckstr)
            pobj(d)
        else:
            params = elel.array_map(params,lambda ele:ACTIONS['status'][ele])
            d = get_status(ckstr)
            for key in params:
                pobj(d[key])
    elif(arr[0] == '-connect'):
<<<<<<< HEAD
        old_ip,new_ip = handle_action(arr,'connect')
    elif(arr[0] == '-disconnect'):
        old_ip,new_ip = handle_action(arr,'disconnect')
    elif(arr[0] == '-reconnect'):
        ckstr = load_ckstr()
        d = get_wan_cfg(ckstr)
        if(d['pppoeInf']['link_type'] == 'auto'):
            old_ip,new_ip = handle_action(arr,'disconnect')
        else:
            old_ip,new_ip =handle_action(arr,'disconnect')
            old_ip,new_ip =handle_action(arr,'connect')
    elif(arr[0] == '-changeip'):
        ckstr = load_ckstr()
        d = get_wan_cfg(ckstr)
        if(d['pppoeInf']['link_type'] == 'auto'):
            old_ip,new_ip = handle_action(arr,'disconnect')
        else:
            old_ip,new_ip1 =handle_action(arr,'disconnect')
            old_ip2,new_ip =handle_action(arr,'connect')
        while(old_ip == new_ip):
            if(d['pppoeInf']['link_type'] == 'auto'):
                old_ip,new_ip = handle_action(arr,'disconnect')
            else:
                old_ip,new_ip1 =handle_action(arr,'disconnect')
                old_ip2,new_ip =handle_action(arr,'connect')
    elif(arr[0] == '-renew'):
        old_ip,new_ip = handle_action(arr,'renew')
    elif(arr[0] == '-release'):
        old_ip,new_ip = handle_action(arr,'release')
=======
        handle_action(arr,'connect')
    elif(arr[0] == '-disconnect'):
        handle_action(arr,'disconnect')
    elif(arr[0] == '-reconnect'):
        handle_action(arr,'disconnect')
        handle_action(arr,'connect')
    elif(arr[0] == '-renew'):
        handle_action(arr,'renew')
    elif(arr[0] == '-release'):
        handle_action(arr,'release')
>>>>>>> 2cb2df3c608618267872c390e5b0195ae2420ada
    elif(arr[0] == '-fail_help'):
        ckstr = load_ckstr()
        params = arr[1:]
        lngth = params.__len__()
        if(lngth == 0):
            params = ["auth_reason", "resp_reason", "other_reason"]
        else:
            #auth_reason, resp_reason, other_reason,
            params = elel.array_map(params,lambda ele:ACTIONS['fail_help'][ele])
        for rel_url in params:
            url = base+rel_url
            ic = req(url,ckstr)
    #####################################
<<<<<<< HEAD
    elif(arr[0] == '-wan_cfg'):
        ckstr = load_ckstr()
        params = arr[1:]
        lngth = params.__len__()
        if(lngth == 0):
            d = get_wan_cfg(ckstr)
            pobj(d)
        else:
            params = elel.array_map(params,lambda ele:ACTIONS['wan_cfg'][ele])
            d = get_wan_cfg(ckstr)
            for key in params:
                pobj(d[key])
=======
>>>>>>> 2cb2df3c608618267872c390e5b0195ae2420ada
    
    
if(__name__=="__main__"):
    do_actions()
else:
    pass
##@user_menu

##@wizard_start

<<<<<<< HEAD

=======
>>>>>>> 2cb2df3c608618267872c390e5b0195ae2420ada
