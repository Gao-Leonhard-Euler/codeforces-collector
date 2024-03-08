import requests
import html
import os

n = 1
t = int(input('查找的样例个数:'))
h = 0
s = requests.get('https://codeforces.com/api/problemset.recentStatus?count='+str(t))
while s.status_code != 200:
    s = requests.get('https://codeforces.com/api/problemset.recentStatus?count=' + str(t))
s = s.json()['result']
for i in range(t):
    if s[i]['contestId'] < 2000:
        df = str(s[i]['problem']['contestId']) + '/' + str(s[i]['problem']['index']) + '/' + s[i]['programmingLanguage']
        submission = 'https://codeforces.com/problemset/submission/' + str(s[i]['contestId']) + '/' + str(s[i]['id'])
        r = requests.get(submission)
        while r.status_code != 200 or (r.text.find('verdict-waiting') != -1 and r.text.find('verdict-waiting') < r.text.find('linenums')):
            r = requests.get(submission)
        r = r.text
        if r.find('verdict-accepted') != -1 and r.find('verdict-accepted') < r.find('linenums'):
            df = df + '/goodCase'
        else:
            df = df + '/badCase'
        if not os.path.exists(df):
            os.makedirs(df)
        f = open(df + '/' + str(s[i]['id']) + '.txt', 'w', encoding='utf-8')
        r = r[r.find('linenums') + 49:len(r)]
        r = html.unescape(r[0:r.find('</pre>')])
        f.write(r)
        n = n+1
        f.close()
