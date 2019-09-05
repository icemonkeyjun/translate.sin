#!C:\python35\python.exe
#-*- coding:utf-8 -*-
print("content-type: text/html; charset=UTF-8")
print()

import cgi
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
with open("index.html", "r", encoding="utf-8") as f:
    html_source = f.read()
#print(html_source.format(translate_result=result, backInputSentence=pageId))
print(html_source)