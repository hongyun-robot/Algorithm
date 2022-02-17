# -*- coding: UTF-8 -*-
# 散列表
# hash_table = dict() or hash_table = {}

voted = {}

def check_voter(name):
    if voted.get(name):
        print 'kick them out!!!'
    else:
        voted[name] = True
        print 'let them vote'

check_voter('张')
check_voter('鸿')
check_voter('张')
