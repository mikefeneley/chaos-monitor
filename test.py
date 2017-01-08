import sys

print(sys.path)
#sys.path.append('/usr/lib/python2.7/dist-packages')
try:
    import mysql
    print("Imported")
except Exception as e:
    print(e)
    print("Not imported")
print(sys.path)
