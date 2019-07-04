from dbdict import dbdict

d = dbdict("dummy")
d["foo"] = "bar"
d["key"] = "value"
d["pi"] = 3.14159
print(d["key"])

d["foo"] = "foo foo"
print(d["foo"])
print(d.keys())

for key in d.keys():
    print("* d[" + str(key) + "] = " + str(d[key]))
