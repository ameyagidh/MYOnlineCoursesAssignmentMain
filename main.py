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




















