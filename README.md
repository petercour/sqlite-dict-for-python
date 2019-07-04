## Dictionary-like database object

For large dictionaries, it may be useful to store them into a database.
The file dbdict.py contains a class that lets you store data directly into
a sqlite database.

You can use it like a normal dictionary:

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

But it's data is stored in a SQLite database, with the name specified in the dbdict constructor.

![program](/program.png)

It's a fork from sebsauvage, which was a Python 2 version.
This version is Python 3.

## Development

Developed in Python,

* https://pythonbasics.org/
* https://pythonprogramminglanguage.com/



