# y=2012
# # y=2100
# if y%4==0 and y%100!=0 or y%400==0:
#     print(True)
# else:
#     print((False))

y=2004

if y%4==0 or y%100==0:
    if y%4==0 and y%100!=0:
        print(True)
    else:
        print(False)
else:
    print(False)
