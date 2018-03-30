# coding: utf-8
#
# 本模块用于从 web网页html文本中解析出 文章集合.
#

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# sys.path.append('./')

import random
import time
import bs4
import web_fetch


# 抓取 指定文本
# 抓取过程需要针对指定需求定制代码
def catch_txt(html_data):
    tmp_html_data = html_data
    tmp_html = bs4.BeautifulSoup(tmp_html_data, "html.parser")
    for child in tmp_html.descendants:
        if type(child) == bs4.element.Tag:
            tmp_id = child.get("id")
            if tmp_id == "content":
                p_text = child.find_all("p")[0]
                p_str = str(p_text)
                p_txt = p_str.decode('utf-8')
                p_txt2 = p_txt.replace("<p>", "").replace("</p>", "").replace("</br>", "\n").replace("<br/>", "\n").replace("<br>", "\n")
                return p_txt2
    return ""


# 抓取文章集合的目录
# 根据需求要定制化
def catch_dir(html_data):
    dir_url_lis = []
    name_lis = []
    tmp_html = bs4.BeautifulSoup(html_data, "html.parser")
    for child in tmp_html.descendants:
        if type(child) == bs4.element.Tag:
            tmp_class = child.get("class")
            if tmp_class == ["dccss"]:
                tmp_children = child.children
                for tmp in tmp_children:
                    if type(tmp) == bs4.element.Tag:
                        url = tmp["href"].encode("utf-8")
                        name = tmp.string
                        name = name.strip(" ").strip("\n").strip(" ")
                        # print "url", url, "name", name
                        dir_url_lis.append(url)
                        name_lis.append(name)
    return dir_url_lis, name_lis


# 抓取文章集合
def catch_all_txt(dir_url, base_url, out_file):
    dir_html_data = web_fetch.getWebContextByProxy(dir_url)
    if not dir_html_data:
        return
    url_lis, name_lis = catch_dir(dir_html_data)
    f = open(out_file, "w")
    rd = random.Random()
    for i, url in enumerate(url_lis):
        full_path_url = base_url + url
        html_data = web_fetch.getWebContextByProxy(full_path_url)
        txt = catch_txt(html_data)
        f.write(name_lis[i] + "\n")
        f.write(txt)
        time.sleep(rd.randint(1, 3))
    f.close()


def test_catch_dir(filename):
    with open(filename, "r") as f:
        html_data = f.read()
        dir_url_lis, name_lis = catch_dir(html_data)
    print dir_url_lis
    print name_lis


def test_catch_txt(filename):
    with open(filename, "r") as f:
        data = f.read()
        txt = catch_txt(data)
    print txt


if __name__ == "__main__":
    test_catch_dir("tmp_html.html")
