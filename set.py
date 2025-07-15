s={2,4,2,3,"het"}
# a set is an unique collection of items
e=set()# dont use s ={} as it will create an empty distionary
print(s)
s.add(6)
print(s)
s.remove(2)
print(s)
s2={2,4,1,4,3}
print(s.union(s2))
print(s.intersection(s2))   