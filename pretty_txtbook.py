# coding: utf-8
#
# 本模块用于对 utf-8格式的 txt电子书进行 去除不必要的换行, 空行, 减少行前空格,
# 格式转化, 过滤制定词汇的行 等功能.
#

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# 把 ansi格式的中文txt书转化成 utf8格式
def convert_ansic_txt_to_utf8(filename, outfile):
    fout = open(outfile, "w")
    with open(filename, "r") as f:
        str1 = f.readlines()
        for line in str1:
            line2 = line.decode('gbk')
            fout.write(line2)
    fout.close()

def get_start_white_count(line):
    ln = len(line)
    for i in range(0,ln):
        if line[i] == " ":
            continue
        return i

# 针对每行在固定长度换行的情况, 去掉不必要的换行
# 思路1: 根据标点符号
# 思路2: 根据换行位置的长度的统计学频次, 需要手动去调一下参数
#        也可以使用经验参数, 不过懒得弄了
def deal_unnecessary_enter_line(filename, outfile):
    words_counts = {}
    white_counts = {}
    fout = open(outfile, "w")
    with open(filename, "r") as f:
        str1 = f.readlines()
        for line in str1:
            line2 = line.decode("utf-8")
            print line2.strip("\r\n").strip("\n")

            n = len(line2)
            wc = get_start_white_count(line)

            if not words_counts.has_key(n):
                words_counts[n] = 0
            words_counts[n] += 1
            if not white_counts.has_key(wc):
                white_counts[wc] = 0
            white_counts[wc] += 1

            # 需要手动去调一下参数
            if n >= 20 and n <= 30 and wc<= 8:
                if wc == 0 and n < 24:
                    fout.write(line2)
                else:
                    fout.write(line2.strip("\r\n").strip("\n"))
            else:
                fout.write(line2)
    fout.close()


# 保留行前指定数量的空格
def filter_prefix_space(filename, outfile, space_num=10):
    fout = open(outfile, "w")
    with open(filename, "r") as f:
        str1 = f.readlines()
        for line in str1:
            line2 = line.decode("utf-8")
            fout.write(line2[0:space_num] + line2[space_num:].replace("  ", ""))
    fout.close()


# 过滤掉不必要的连续空行
def filter_double_empty_line(filename, outfile):
    fout = open(outfile, "w")
    last_enter = False
    with open(filename, "r") as f:
        str1 = f.readlines()
        for line in str1:
            line2 = line.decode("utf-8")
            line3 = line2.lstrip(" ")
            this_enter = False
            if line3 == "\n":
                this_enter = True
            if last_enter and this_enter:
                pass
            else:
                fout.write(line2)
            last_enter = this_enter
    fout.close()

# 过滤掉全部空行
def filter_empty_line(filename, outfile):
    fout = open(outfile, "w")
    with open(filename, "r") as f:
        str1 = f.readlines()
        for line in str1:
            line2 = line.decode("utf-8")
            line3 = line2.lstrip(" ")
            if line3 != "\n":
                fout.write(line2)
    fout.close()

# 过滤掉包含指定词汇集合的行
def filter_keys_line(filename, outfile, keys):
    fout = open(outfile, "w")
    last_enter = False
    with open(filename, "r") as f:
        str1 = f.readlines()
        for line in str1:
            line2 = line.decode("utf-8").lstrip(" ")
            exist = False
            _key = ""
            for k in keys:
                if line2.find(k) >= 0:
                    _key = k
                    exist = True
                    break
            if exist:
                pass
            else:
                fout.write(line2)
    fout.close()

def test_pretty_txtbook():
    convert_ansic_txt_to_utf8(u"./1984.txt", u"./1984-utf8-test1.txt")


if __name__ == "__main__":
    test_pretty_txtbook()
