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
