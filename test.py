# -*- coding:utf-8 -*-
__author__ = 'hedtao'
from zhihu import Search
from zhihu import User

def person_attention(url,person_name):
    return#搜索与某人关注的话题
def main():
    name = 'xxx'
    type ='people'
    #search = Search()
    #search.get_person_detail(type,name)
    userid = 'dong-yuan-18'
    user = User(userid)
    user.get_user_update()


if __name__ == '__main__':
    main()


