# coding: utf-8
#
# 本模块用于从网站抓取 html web页面.
#
import random
import requests

# 添加 代理服务器地址
proxy_lis = [
    "1.2.3.4:8080",
    "1.1.1.1:8080",
]

def get_random_proxy():
     pxy = proxy_lis[rd.randint(0, len(proxy_lis)-1)]
     return pxy


# 设置 header 参数
def getRandomFakeheaders():
    Hosts = [
        "",
        # "heyaq.com",
        # "http://heyaq.com",
    ]
    UserAgents = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    ]
    AcceptEncodings = [
        "gzip, deflate, sdch, br",
        "gzip, deflate, sdch",
        "gzip, deflate, br",
        "gzip, deflate",
    ]
    AcceptLanguages = [
        "zh-CN,zh;q=0.8,en;q=0.6",
        "zh-CN,zh;q=0.8,ja;q=0.6",
        "zh-cn,zh;q=0.5",
        "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7",
    ]
    Accepts = [
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5",
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    ]
    UpgradeInsecureRequests = [
        "",
        "1",
    ]
    CacheControls = [
        "",
        "max-age=0",
    ]
    Cookies = [
        "",
        "acw_tc=AQAGAA0O/3k0VCSa5CJd/BQrRQgAMHch; fuid=1174039178f32b4d892614beac9a7e58;",
    ]
    Connections = [
        "",
        "keep-alive",
    ]
    rd = random.Random()
    headers = {}
    hs = Hosts[rd.randint(0, len(Hosts)-1)]
    if hs:
        headers['Host'] = hs
    headers['User-Agent'] = UserAgents[rd.randint(0, len(UserAgents)-1)]
    headers['Accept-Encoding'] = AcceptEncodings[rd.randint(0, len(AcceptEncodings)-1)]
    headers['Accept-Language'] = AcceptLanguages[rd.randint(0, len(AcceptLanguages)-1)]
    headers['Accept'] = Accepts[rd.randint(0, len(Accepts)-1)]
    uir = UpgradeInsecureRequests[rd.randint(0, len(UpgradeInsecureRequests)-1)]
    if uir:
        headers['Upgrade-Insecure-Requests'] = uir
    cc = CacheControls[rd.randint(0, len(CacheControls)-1)]
    if cc:
        headers['Cache-Control'] = cc
    ck = Cookies[rd.randint(0, len(Cookies)-1)]
    if ck:
        headers['Cookie'] = ck
    cn = Connections[rd.randint(0, len(Connections)-1)]
    if cn:
        headers['Connection'] = cn
    return headers

def getResWithProxyAndFakeheader(dst_url, proxy_addr=None):
    headers = getRandomFakeheaders()
    try:
        if proxy_addr:
            proxies = {"http": proxy_addr}
            r = requests.get(dst_url, headers=headers, proxies=proxies)
            r.encoding = 'utf-8'
            res = r.content
        else:
            r = requests.get(dst_url, headers=headers)
            r.encoding = 'utf-8'
            res = r.content
    except Exception as e:
        res = None
        print "getResWithProxyAndFakeheader err", str(e)
    return res

def getWebContextByProxy(dst_url, use_proxy=False):
    if use_proxy == False:
        res = getResWithProxyAndFakeheader(dst_url)
        return res

    proxy = get_random_proxy()
    res = getResWithProxyAndFakeheader(dst_url, proxy)
    return res

def test_web_fetch():
    dst_url = "abc.xyz.com"
    res = getWebContextByProxy(dst_url)
    if res:
        with open("tmp_html.html", "w") as f:
            f.write(res)
    print res

if __name__ == "__main__":
    test_web_fetch()

