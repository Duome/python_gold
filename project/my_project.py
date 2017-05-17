# -*- coding: utf-8 -*-
__author__ = 'Duome'

""" 构建人民的名义关系图
    将人民的名义文件汇总
    jieba库
    Gephi软件
"""

import codecs
import jieba
import jieba.posseg as pseg

names = {}            # 姓名字典
relationships = {}    # 关系字典
lineNames = []        # 每段内人物关系
initial_name = {
    u'小艾': u'钟小艾',
    u'达康': u'李达康',
    u'刘总': u'刘新建',
    u'侯局': u'侯亮平',
    u'肖检': u'肖钢玉',
    u'赵董': u'赵瑞龙',
    u'季检': u'季昌明',
    u'赵公子': u'赵瑞龙',
    u'老杜': u'老杜',
    u'陈老': u'陈岩石',
    u'孙书记': u'孙连城',
    u'昌明': u'季昌明',
    u'郑董': u'郑胜利',
    u'老肖': u'肖钢玉',
    u'师母': u'师母',
    u'同伟': u'祁同伟',
    u'赵总': u'赵瑞龙',
    u'小高': u'高小凤',
    u'杜总': u'老杜',
    u'郑乾': u'郑胜利',
    u'郑西坡': u'郑西坡',
    u'赵立春': u'赵立春',
    u'高小凤': u'高小凤',
    u'钟小艾': u'钟小艾',
    u'郑成功': u'郑成功',
    u'易学习': u'易学习',
    u'祁同伟': u'祁同伟',
    u'宝宝': u'宝宝',
    u'王大陆': u'王大陆',
    u'刘新建': u'刘新建',
    u'高育良': u'高育良',
    u'陈岩石': u'陈岩石',
    u'李达康': u'李达康',
    u'沙振江': u'沙振江',
    u'吴慧芬': u'吴慧芬',
    u'欧阳菁': u'欧阳菁',
    u'赵瑞龙': u'赵瑞龙',
    u'刘庆祝': u'刘庆祝',
    u'张华华': u'张华华',
    u'沙瑞金': u'沙瑞金',
    u'季昌明': u'季昌明',
    u'赵东来': u'赵东来',
    u'田杏枝': u'田杏枝',
    u'老程': u'老程',
    u'秦局': u'秦局',
    u'陈清泉': u'陈清泉',
    u'赵德汉': u'赵德汉',
    u'孙连城': u'孙连城',
    u'肖钢玉': u'肖钢玉',
    u'陆亦可': u'陆亦可',
    u'陈海': u'陈海',
    u'高小琴': u'高小琴',
    u'郑胜利': u'郑胜利',
    u'张桂兰': u'张桂兰',
    u'梁璐': u'梁璐',
    u'侯亮平': u'侯亮平'
}
jieba_function.load_userdict('dict.txt')             # 加载字典

with codecs.open('renmin.txt','r','utf-8') as f:
    for line in f.readlines():
        poss = pseg.cut(line)               # 分词并返回词词性
        lineNames.append([])                # 为新读入的一段添加人物名称列表

        for w in poss:
            if w.flag != 'nr' or len(w.word) < 2:
                continue                    # 当分词长度小于2或该词性不为nr时认为该次不为人名
            if initial_name.get(w.word) is None:
                continue

            lineNames[-1].append(initial_name[w.word])    # 当前环境增加一个人物
            if names.get(initial_name[w.word]) is None:
                names[initial_name[w.word]] = 0
                relationships[initial_name[w.word]] = {} #[]
            names[initial_name[w.word]] += 1              # 该人物出现次数加 1
# for name, time in names.items():
#     print name,time

for line in lineNames:                      # 对于每一段
    for name1 in line:
        for name2 in line:                  # 每段中的任意两个人
            if name1 == name2:
                continue
            if relationships[name1].get(name2) is None:  # 若两个人尚未同时出现则新建项
                relationships[name1][name2] = 1
            else:
                relationships[name1][name2] += 1

with open('renmin_node.txt', 'w') as f:
    tmp_lst = ['Id Label Weight']
    for name, times in names.iteritems():     # 遍历字典尽量用迭代器版本
        if times > 3:
            tmp_lst.append('%s %s %d' % (name.encode('utf-8'), name.encode('utf-8'), times))
    f.write('\r\n'.join(tmp_lst))

with open('renmin_edge.txt', 'w') as f:
    edge_lst = ['Source Target Weight']
    for name, edges in relationships.items():
        for val, times in edges.items():
            if times > 3:
                edge_lst.append('%s %s %d' % (name.encode('utf-8'), val.encode('utf-8'), int(times)))
    f.write('\r\n'.join(edge_lst))


