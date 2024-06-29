"""
========================================
Name:webpc Author: Lalevin Martin
 Mailbox: rsjdcl@gmail.com                                               
 Github: http://github.com/nacglalevin
Written in 2022-11-2
==================NACG==================
"""
import requests
import sys
import os

web_tx = """
                __
 _      _____  / /_  ____  _____
| | /| / / _ \/ __ \/ __ \/ ___/
| |/ |/ /  __/ /_/ / /_/ / /__
|__/|__/\___/_.___/ .___/\___/
< by Lalevin. >  /_/ 
"""
print(web_tx)

def web_pcxz():
    if os.name == 'posix':
        c = os.system('which pip')
        if c == 256:
            os.system("apt-get install python-pip")
        else:
            pass
    else:
        print ('[-] Check your pip installer')
    try:
        import requests
    except:
        os.system('pip install requests')
        sys.exit('[+] I have installed necessary modules for you')

def web_pc():
    heed = {"User-Agent":"Mozilla/5.0(Windows NT 10.0; Win64; ×64"}
    web_sr = input("请输入网站域名:")
    web_cz = requests.get(web_sr)
    web_sc = requests.get(web_sr).text
    if web_cz.ok:
        web_pd = input("是否保存爬取的html文件(y/n):")
        if web_pd == "y":
            web_cr = input("请输入保存文件名:")
            with open(web_cr,"w") as web_wj:
                web_wj.write(web_sc)
                web_os = os.path.abspath(web_cr)
                print(f"保存至{web_os}")
        elif web_pd == "n":
            web_dy = input("是否打印出爬取的html(y/n):")
            if web_dy == "y":
                print(web_sc)
            elif web_dy == "n":
                os.system("clear")
                print("程序结束")
            else:
                print("请输入正确的选项")
        else:
            print("请输入正确的选项")
            web_pd = input("是否保存爬取的html文件(y/n):")
            web_cr = input("请输入保存文件名:")
    elif web_cz.status_code =="404":
        print("网页不存在,请确保输入正确的网站域名")
    else:
        os.system("clear")
        print("请求失败")
    try:
        web_cz = requests.get(web_sr)
        web_sc = requests.get(web_sr).text
    except:
        print("请输入正确的网站域名")
if __name__ == '__main__':
    web_pcxz()
    web_pc()