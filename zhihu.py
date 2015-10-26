# -*- coding:utf-8 -*-
__author__ = 'hedtao'

import requests

from bs4 import BeautifulSoup

request = requests.session()

class Search:
    base_url = "http://www.zhihu.com/search?"
    soup = None
    search_word = None

    def __init__(self):
        return



    def parser(self,url):
        print(url)
        r = request.get(url)
        self.soup = BeautifulSoup(r.content)


    def get_result_num(self):
        #if self.soup == None:
        #    self.parser()
        #soup = self.soup
        #result_num = soup.find()
        return

    def get_person_detail(self,type,value):
        url = self.base_url +"type=" + type + "&q=" + value

        if self.soup == None:
            self.parser(url)
        result = self.soup.find_all('a',attrs={"class": "name-link"})
        if result == None:
         #   print "no answer..."
            return
        for item in result:
            print(item)

class User:
    user_base_url = "http://www.zhihu.com/people/"
    soup = None

    def __init__(self,user_id):
        self.url = self.user_base_url + user_id
        return

    def parser(self):
        r = request.get(self.url)
        self.soup = BeautifulSoup(r.content)

    def get_user_update(self):
        if self.soup == None:
            self.parser()
        result = self.soup.find_all('a',attrs={"class":"question_link"})
        if result == None:
            return
        for item in result:
            print (item)







