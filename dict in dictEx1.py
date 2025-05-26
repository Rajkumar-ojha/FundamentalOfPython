d1={"sno":10,"sname":"rs","intmarks":{"cm":17,"cpp":16,"os":19},"extmarks":{"cm":78,"cpp":77,"os":79},"cname":"oucet"}
print(d1,type(d1))
for its in d1.items():
    print(its)
for k,v in d1.items():
    print(k,"------>",v)
for k,v in d1.items():
    print(k,v,type(d1))
d1["intmarks"]["dbms"]=16
d1["extmarks"] ["dbms"]=77
print(d1,type(d1))
d1["intmarks"].pop("cm")
d1["extmarks"].pop("os")
print(d1,type(d1))