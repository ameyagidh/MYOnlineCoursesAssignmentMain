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

# Beautiful Soup


































