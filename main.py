# Python for every body
# https://github.com/ameyagidh/MYOnlineCoursesAssignmentMain.git
# Token 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
# /Users/ameyagidh/AAAmeya/AllWork/PythonForEverybody

# Course 1

# week1
# print("hello world")

# week2
# P1
# a = input("Enter your name \n")
# print("Hello",a)

# P2
# hrs = input("Enter hrs \n")
# rate = input("enter rate \n")
# print(float(hrs)*float(rate))

# week3, week4
# P1
#hrs = float(input("Enter hrs \n"))
# rate = float(input("Enter rate \n"))
# if hrs > 40:
#     res = (hrs-40)*rate*1.5 + 40*rate
# else:
#     res = hrs*rate
#
# print(res)

# week 5
# P1
# ans = []
# while (True):
#     res = input("Enter a number or done to exit \n")
#     if res == "done":
#         break
#     try:
#         res.isdigit()
#         ans.append(res)
#         largest = max(ans)
#         smallest = min(ans)
#         print("Largest ",largest)
#         print("Smallest ", smallest)
#     except:
#         raise "not a digit"
# print("Done")

# ------------------------------------------

# Course 2

# P1
# text = "X-DSPAM-Confidence:    0.8475"
# import re
# res = re.findall(r"\d+",text)
# res2 = ".".join(res)
# print(res2)

# text = "X-DSPAM-Confidence:    0.8475"
# res = text.find(":")
# print(text[res+1:].strip())

# P2
# fname = input("Enter file name \n")
# fname = "words.txt"
# fh = open(fname,"r")
# f = fh.read()
# print(f.upper().rstrip())
# for line in fh:
#     print(line.upper())
# print(fh.read())

# P3
# fname = "mbox-short.txt"
# fh = open(fname,"r")
# # f = fh.read()
# res = []
# total = 0
# ctr = 0
# for line in fh:
#     if not line.startswith("X-DSPAM-Confidence:"):
#         continue
#     idx = line.find(":")
#     ctr += 1
#     total += float(line[idx+1:].strip())
# print(total/ctr)

# P4
# fname = "romeo.txt"
# fh = open(fname)
# res = []
# for line in fh:
#     words = line.split()
#     # for word in words:
#     res.append(words)
# res2 = []
# for i in res:
#     res2.extend(i)
# res2 = list(set(res2))
# res2.sort()
# print(res2)

# P5
from collections import Counter
# fname = "mbox-short.txt"
# fh = open(fname,"r")
# # c = 0
# res = {}
# for line in fh:
#     if not line.startswith("From "):
#            continue
#     words = line.split()
#     res[words[1]] = 1+res.get(words[1],0)
    # print(words[1])
    # c += 1
# print(c)
# Counter(res)
# print(res)
# print(max(res.values()))
# curr = max(res.values())
# for k,v in res.items():
#     if v == curr:
#         print(k)

# fname = "mbox-short.txt"
# fh = open(fname,"r")
# # f = fh.read()
# # print(f)
# dicta = {}
# for line in fh:
#     if not line.startswith("From "):
#         continue
#     words = line.split()
#     temp = words[5].split(":")[1]
#     dicta[temp] = 1 + dicta.get(temp,0)
# print(dicta.keys())
# maxi = max(dicta.values())
# for k,v in dicta.items():
#     if v == maxi:
#         print(k)

# Using Regex
import re
# fname = "regex_sum_42.txt"
# fh = open(fname,"r")
# pattern = '[0-9]+'
# # 1 or more is + 0 or more is *
# sum_ = 0
# for line in fh:
#     a = re.findall(pattern,line)
#     if a == []:
#         continue
#     for each in a:
#         sum_ += float(each)
# print(sum_)

# Http
# import socket
# url = "data.pr4e.org"
# mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# mysock.connect((url,80))
# cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)
# c = 0
# str = ""
# while True:
#     c += 1
#     data = mysock.recv(512)
#     if len(data)<1:
#         break
#     str += data.decode()
# print(str)
# lastMod=re.findall('Last-Modified: (.+)\r',str)
# print(lastMod)

# Tabular data structure
# Beautiful Soup
import ssl, urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
# url = "https://py4e-data.dr-chuck.net/comments_22077.html"
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
# html = urllib.request.urlopen(url,context=ctx).read()
# soup = BeautifulSoup(html,"html.parser")
# tags = soup('span')
# pattern = "[0-9]+"
# sum_ = 0
# for tag in tags:
#     # print(type(tag))
#     # print(tag.contents)
#     # print(tag)
#     val = re.findall(pattern,tag.contents[0])
#     print(val)
#     sum_ += float(val[0])
# print(sum_)


# Beautiful soup 2
# jumping over the urls

# url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
# itr = 3
# pos = 3
# for each in range(itr):
#     ctx = ssl.create_default_context()
#     ctx.check_hostname = False
#     ctx.verify_mode = ssl.CERT_NONE
#     html = urllib.request.urlopen(url, context=ctx).read()
#     soup = BeautifulSoup(html, "html.parser")
#     tags = soup("a")
#     curr_lst = []
#     for tag in tags:
#         # print(tag.get("href",None))
#         curr_lst.append(tag.get("href",None))
#     url = curr_lst[pos-1]
#     print(url)

# xml
import xml.etree.ElementTree as et
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
# url = "http://py4e-data.dr-chuck.net/comments_22079.xml "
# html = urllib.request.urlopen(url, context=ctx).read()
# print(html)
# tree = et.fromstring(html)
# for tag in tree.findall("comments/comment"):
#     print(tag.find("count").text)
#     print(tag.find("name").text)

# json
import json
# url = "http://py4e-data.dr-chuck.net/comments_22080.json"
# html = urllib.request.urlopen(url).read()
# json_ = json.loads(html.decode())
# jd = json.dumps(json_,indent=2)
# # print(type(jd))
# # print(jd)
# ex = json_["comments"]
# for val in ex:
#     print(val["count"])

# url = "http://py4e-data.dr-chuck.net/geojson?"
# loc = "Northeastern University"
#
# ans = url + urllib.parse.urlencode({"address":loc})
# uh = urllib.request.urlopen(ans).read()
# # print(uh.decode())
# js= json.loads(uh)
# id = js['results'][0]["place_id"]
# print(id)

# Database
import sqlite3
# conn = sqlite3.connect("dbcount.sqlite")
# curr = conn.cursor()
# cmd = '''
# Drop table if exists Counts'''
# curr.execute(cmd)
#
# curr.execute('''CREATE TABLE Counts(org TEXT, count INTEGER)''')
# fname = "mbox-short.txt"
# fh = open(fname,"r")
#
# for line in fh:
#     if not line.startswith("From:"):
#         continue
#     lt = line.split("@")
#     domain = lt[1]
#     curr.execute('''SELECT count from Counts WHERE org =?''',(domain,))
#     row = curr.fetchone()
#     if row is None:
#         curr.execute('''INSERT INTO Counts (org,count) VALUES(?,1)''',(domain,))
#     else:
#         curr.execute('''UPDATE Counts SET count = count + 1 WHERE org =?''',(domain,))
#         conn.commit()
#
# cmd = '''SELECT * FROM Counts ORDER BY count DESC'''
# for r in curr.execute(cmd):
#     print(r[0],r[1])
# curr.close()

# P1
# conn = sqlite3.connect('rosterdb.sqlite')
# curr = conn.cursor()
#
# curr.executescript('''
# DROP TABLE IF EXISTS User;
# DROP TABLE IF EXISTS Member;
# DROP TABLE IF EXISTS Course;
#
# CREATE TABLE User(
#     name TEXT UNIQUE,
#     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE
# );
#
# CREATE TABLE Member(
#     user_id     INTEGER,
#     course_id   INTEGER,
#     role        INTEGER,
#     PRIMARY KEY (user_id, course_id)
# );
#
# CREATE TABLE Course(
#     title  TEXT UNIQUE,
#     id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE
# )
#
# ''')
#
#
# fname = "roster_data.json"
# fh = open(fname,"r").read()
# js = json.loads(fh)
# for line in js:
#     # print(line[0],line[1],line[2])
#     curr.execute('''INSERT OR IGNORE INTO User(name)
#      VALUES(?)
#      ''',(line[0],))
#     curr.execute('SELECT id FROM User WHERE name = ? ', (line[0], ))
#     usr_id = curr.fetchone()[0]
#     curr.execute('''INSERT OR IGNORE INTO Course(title)
#          VALUES(?)
#          ''', (line[1],))
#     curr.execute('SELECT id FROM Course WHERE title = ? ', (line[1], ))
#     cr_id =curr.fetchone()[0]
#     curr.execute('''INSERT OR REPLACE INTO Member
#             (user_id, course_id,role) VALUES ( ?, ?, ? )''',
#                 (usr_id, cr_id, int(line[2])))
#     conn.commit()
# curr.close()















































