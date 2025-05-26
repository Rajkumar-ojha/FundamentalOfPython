d1={"sno":100,"name":"raj","intmarkss":{"cm":17,"c++":70},"extmarks":{"cm":90,"c++":90},"cname":"mukul"}
print(d1,type(d1))
for k in d1.keys():
    print(k)
for v in d1.values():
    print(v)
for its in d1.items():
    print(its)
for mukul,rupesh in d1.items():
    print(mukul,"----->",rupesh)