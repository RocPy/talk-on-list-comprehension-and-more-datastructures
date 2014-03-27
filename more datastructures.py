print

emptyTuple = ()
myTuple = 'hi',
myTuple = 'hi', 'there', 'friend'


# Packing
a, b, c = myTuple

myList = [10, 20, 40]

x, y, z = myList
x, y = myList
x, y, z, l = myList

a, (b, c), d = [1, (2, 3), 4]

a, b = b, a


# Slices
a = [0, 1, 2, 3, 4, 5]

LASTTHREE = slice(-3, None)

a[LASTTHREE]


# Sets
A = {1, 2, 3, 3}
B = {3, 4, 5, 6, 7}

print A | B

print A & B

print A - B

print B - A

print A ^ B

print (A ^ B) == ((A - B) | (B - A))

import collections
A = collections.Counter([1, 2, 3, 3])
B = collections.Counter([3, 4, 5, 6, 5, 7, 5])

B.most_common(2)


# Ordered Dictionaries
m = dict((str(x), x) for x in range(10))
print ', '.join(m.keys())

m = collections.OrderedDict((str(x), x) for x in range(10))
print ', '.join(m.keys())

m = collections.OrderedDict((str(x), x) for x in range(10, 0, -1))
print ', '.join(m.keys())


# Default dict
m = dict()
print m['a']

m = collections.defaultdict(int)
print m['a']

print m['b']

m = collections.defaultdict(str)
print m['a']

m['b'] += 'x'
print m['b']

m = collections.defaultdict(lambda: '[default value]')
print m['a']

def DefaultValue():
    return 'blah'

m = collections.defaultdict(DefaultValue)
print m['kdk']

import json
tree = lambda: collections.defaultdict(tree)
root = tree()
root['menu']['id'] = 'file'
root['menu']['value'] = 'File'
root['menu']['menuitems']['new']['value'] = 'New'
root['menu']['menuitems']['new']['onclick'] = 'new();'
root['menu']['menuitems']['open']['value'] = 'Open'
root['menu']['menuitems']['open']['onclick'] = 'open();'
root['menu']['menuitems']['close']['value'] = 'Close'
root['menu']['menuitems']['close']['onclick'] = 'close();'
print json.dumps(root, sort_keys=True, indent=4, separators=(',', ': '))