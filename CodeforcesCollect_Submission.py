import requests
import html
import os
import random
import fake_useragent

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

t = int(input('input a number not greater than 1000:'))
s = requests.get('https://codeforces.com/api/problemset.recentStatus?count='+str(t), headers={'User-Agent':randomUA()})
while s.status_code != 200:
    s = requests.get('https://codeforces.com/api/problemset.recentStatus?count=' + str(t), headers={'User-Agent':randomUA()})
s = s.json()['result']
for i in range(t):
    if s[i]['contestId'] < 2000:
        df = str(s[i]['problem']['contestId']) + '/' + str(s[i]['problem']['index']) + '/' + s[i]['programmingLanguage']
        submission = 'https://codeforces.com/problemset/submission/' + str(s[i]['contestId']) + '/' + str(s[i]['id'])
        r = requests.get(submission, headers={'User-Agent':randomUA()})
        while r.status_code != 200 or (r.text.find('<span class=\'verdict-waiting\'') != -1 and r.text.find('<span class=\'verdict-waiting\'') < r.text.find('linenums')):
            r = requests.get(submission, headers={'User-Agent':randomUA()})
        r = r.text
        if r.find('<span class=\'verdict-accepted\'') != -1 and r.find('<span class=\'verdict-accepted\'') < r.find('linenums'):
            df = df + '/goodCase'
        else:
            df = df + '/badCase'
        if not os.path.exists(df):
            os.makedirs(df)
        f = open(df + '/' + str(s[i]['id']) + '.txt', 'w', encoding='utf-8')
        r = r[r.find('linenums') + 49:len(r)]
        r = html.unescape(r[0:r.find('</pre>')])
        f.write(r)
        f.close()
