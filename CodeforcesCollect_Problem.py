import requests
import html
import os
import fake_useragent
import random

def randomUA():
    rx = random.randint(1,4)
    if rx==1:
        return fake_useragent.UserAgent().chrome
    elif rx==2:
        return fake_useragent.UserAgent().firefox
    elif rx==3:
        return fake_useragent.UserAgent().safari
    else:
        return fake_useragent.UserAgent().random

t = input('contest:')+'/'+input('problem:')
if not os.path.exists(t):
    os.makedirs(t)
r = requests.get('https://codeforces.com/problemset/problem/' + t, headers={'User-Agent':randomUA()})
while r.status_code != 200:
    r = requests.get('https://codeforces.com/problemset/problem/' + t, headers={'User-Agent':randomUA()})
if str(r.headers).find('application/pdf') != -1:
    f = open(t+'/problem.pdf','wb')
    f.write(r.content)
    f.close()
else:
    r = html.unescape(r.text)
    r = r[r.find('<head>'):r.find('</head>')+8] + r[r.find('<div class="ttypography"><div class="problem-statement"><div class="header"><div class="title">'):r.find('    <script>\r\n        $(function () {')-11]
    f = open(t+'/problem.html', 'w', encoding='utf-8')
    f.write(r)
    f.close()
