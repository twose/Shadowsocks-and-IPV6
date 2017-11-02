# Shadowsocks and IPV6

Shadowsocks 和 IPV6,两者配合使用风味更佳.

**但是如何让有IPV6的走IPV6,没有IPV6的走SS呢?这就是这个脚本的存在意义.**

### 使用方式

clone本仓库 或 下载 [SShost.py](https://raw.githubusercontent.com/twose/Shadowsocks-and-IPV6/master/SShosts.py)

1. 修改代码中的 user_rule_file 为 你的 Shadowsocks user_rule(用户规则)文件路径 [默认是Shadowsocks-NG]
2. 修改代码中的 hosts_file 为 你的 系统hosts文件路径[默认是 /etc/hosts]
3. 修改代码中的 proxies 为你的本地代理地址(如果你可以访问gayhub的raw服务器,那就删除它)
4. 以管理员权限运行脚本

```bash
# linux
sudo SShost.py 
```

脚本会从仓库 [**ipv6-hosts**](https://github.com/lennylxx/ipv6-hosts)下载最新的ipv6-hosts文件并提取其中的hosts到PAC过滤列表中

### 依赖

```bash
pip3 install requests
```