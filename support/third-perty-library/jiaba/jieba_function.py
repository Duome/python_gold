# -*- coding: utf-8 -*-
__author__ = 'Duome'

"""实现中文分词三方库 jieba 的基本使用
   内容为：分词、导入自定字典、获取词性
"""

import sys
sys.path.append('../')

import jieba
import jieba.analyse
import jieba.posseg as pseg
from optparse import OptionParser


def jieba_test():
    """用于演示一些算法
    """
    USAGE = "usage:    python extract_tags.py [file name] -k [top k]"
    parser = OptionParser(USAGE)
    parser.add_option("-k", dest="topK")
    opt, args = parser.parse_args()

    if len(args) < 1:
        print(USAGE)
        sys.exit(1)
    file_name = args[0]
    if opt.topK is None:
        topK = 10
    else:
        topK = int(opt.topK)
    content = open(file_name, 'rb').read()
    tags = jieba.analyse.extract_tags(content, topK=topK)
    print(",".join(tags))

def string_cut():
    """分词模式：
       精确模式——将句子最精确地分开，适合文本分析
       全模式——将句子所有可以成词的词语扫描出来，不能解决歧义
       搜索引擎模式——精确模式基础上，对长词再次切分
    """
    string = '我来到北京清华大学'
    default_mode = jieba.cut(string)    # 默认模式
    exact_mode = jieba.cut(string, cut_all = False)     # 精确格式，默认格式为精确格式
    full_mode = jieba.cut(string, cut_all = True)     # 全模式
    for_search_mode = jieba.cut_for_search(string)
    print '默认模式：', '/'.join(default_mode)
    print '精确模式：', '/'.join(exact_mode)
    print '全模式：', '/'.join(full_mode)
    print '搜索引擎模式：', '/'.join(for_search_mode)
    print type(exact_mode)
    for w in default_mode:
        print type(w)
        print w

def add_dict():
    """在分词前，导入自定义字典
       以便包含jieba词库中没有的词，提高正确率
       dict.txt中的内容
       字符+空格+词性
       eg:李小福 nr
    """
    string = '李小福是云计算方面的专家'
    cut_string = jieba.cut(string)
    print '/'.join(cut_string)
    jieba.load_userdict('test_dict.txt')
    cut_string = jieba.cut(string)
    print '/'.join(cut_string)

def string_analyse():
    pass

def string_flag():
    """获取词性
    """
    string = '我爱北京天安门'
    words = pseg.cut(string)
    for w in words:
        print w.word, w.flag
        print type(w)

if __name__ == '__main__':
    jieba_test()
    # string_cut()
    # add_dict()
    # string_flag()