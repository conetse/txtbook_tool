
## txtbook_tool

本工具组 txtbook_tool 从网站抓取文章集合, 对txt电子书进行格式化等功能.


### 主要功能

本工具主要提供了一些工具例子, 并非开箱即用的通用模块.

主要功能:

1. 从文章网站抓取web网页, 并从网页中解析出所需要的文章集合.
2. 对 utf-8格式的 txt电子书进行 去除不必要的换行, 空行, 减少行前空格, 格式转化, 过滤制定词汇的行 等功能.

### 使用场景

例子中提供了一个套路, 需要根据需求定制化代码的地方, 请自行修改.

### 模块简介

```web_fetch```   用于抓取web网页, 伪装了header, 可使用代理.

```catch_txtbook```  用于从html文本中解析出所感兴趣的文本和数据. 这里需要自行定制化.

```pretty_txtbook```  用于对文章集合的txt文件进行格式化, 例如去除不必要的换行, 空行, 减少行前空格等.


### 使用方式

需先安装 beautifulsoup4 和 requests 模块:
```
pip install beautifulsoup4
pip install requests
```

例子:


```
# coding: utf-8
# filename: test_txtbook_tool.py

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# sys.path.append('./')
import pretty_txtbook

def test_txtbook_tool():
    pretty_txtbook.convert_ansic_txt_to_utf8(u"./1984.txt", u"./1984-utf8-test1.txt")

if __name__ == "__main__":
    test_txtbook_tool()
```


