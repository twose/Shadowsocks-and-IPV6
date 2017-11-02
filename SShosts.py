import re
import requests
import time

hosts_file = '/etc/hosts'
hosts_default = '''\
##
# Host Database By Twosee
#
# localhost is used to configure the loopback interface
# when the system is booting.  Do not change this entry.
#
# upgrade time is %s 
##


127.0.0.1	localhost
255.255.255.255	broadcasthost
::1             localhost

127.0.0.1	www.cust.com
192.168.221.225 git.tusi.studio
138.68.27.161 gowalker.org


''' % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

user_rule_file = '/Users/twosee/.ShadowsocksX-NG/user-rule.txt'
user_rule = '''\
github.com
githubapp.com
raw.githubusercontent.com
githubusercontent.com
gitbooks.io
gowalker.org
google-analytics.com
biuss.com
tinypng.com
ip138.com
amazonaws.com
pixiv.net
pixiv.org
pximg.net
atlassian.com
rackcdn.com
github.io
mozilla.org
alfredworkflow.com
v2ex.com
hacklang.org
godaddy.com
msxiaoice.com
xclient.info
jetbrains.com
ads-twitter.com
'''
proxies = {
    'http': '127.0.0.1:1087',
    'https': '127.0.0.1:1087'
}
hosts_ipv6 = requests.get('https://raw.githubusercontent.com/lennylxx/ipv6-hosts/master/hosts', proxies=proxies).text
hosts_ipv6_groups = re.findall('^([:0-9a-f]{5,}) ([^\s]+).*$', hosts_ipv6, re.MULTILINE)
for i in hosts_ipv6_groups:
    user_rule += ('\n@@' + i[1])  # 生成一个过滤ipv6的列表
try:
    with open(user_rule_file, 'w') as f:
        f.write(user_rule)
    print('success create %i lines to %s' % (len(hosts_ipv6_groups), user_rule_file))
except:
    print('write %s failed')

try:
    with open(hosts_file, 'w') as f:
        f.write(hosts_default + hosts_ipv6)
    print('success upgrade %s' % hosts_file)
except:
    print('failed write %s, it need root privileges' % hosts_file)
