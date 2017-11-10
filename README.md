# Shadowsocks and IPV6

Shadowsocks and IPV6, let flavor better.

**But how to get IPV6 go IPV6, IPV4 go SS? This is the meaning of the existence of this script.**

### How to use

clone this repository or download [SShost.py](https://raw.githubusercontent.com/twose/Shadowsocks-and-IPV6/master/SShosts.py)

1. Modify user_rule_file in your code to your Shadowsocks user_rule file path [default is Shadowsocks-NG]
2. Modify the code in the hosts_file for your system hosts file path [default is / etc / hosts]
3. Change the proxies in your code to your local proxy address (if you can access gayhub's raw server, delete it)

```bash
# linux 
sudo SShost.py
```

The script downloads the latest ipv6-hosts file from the repository [**ipv6-hosts**](https://github.com/lennylxx/ipv6-hosts) and extracts the hosts into the PAC filter list

### Rely

```Bash
pip3 install requests
```