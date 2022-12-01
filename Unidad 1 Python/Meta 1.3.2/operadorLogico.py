# Conjuntos
U = {"a","b","c","d","e"}
A = {"a","b","d"}
B = {"b","d","e"}
C = {"a","b","e"}

# Operaciones de Conjuntos Uniones
#a
print(A.union(B))
#b
print(A.union(C))
#c
print(B.union(C))
#d
print(B.union(B))


#interseccion
#e
print(A.intersection(B))
#f
print(A.union(B.intersection(C)))
#g
print(A.intersection(A))
#h
print(B.intersection(C))
#i
print(A.intersection(B).intersection(C))
#j
print(A.intersection(B.intersection(C)))


# Operaciones de Diferencia
#k
print(A.difference(B))
#l
print(U.difference(U.difference(A)))
#m
print(C.difference(A))
#n
print(B.difference(C))
#o
print(B.difference(A))
#p
print(B.intersection(U.difference(A)))
#q
print(A.difference(A))
#r
print(U.difference(A))
#s
print(U.difference(B))
#t
print(U.difference(A.intersection(C)))
#u
print((A.union(B).union(C))-U)
#v
print(A.union(U.difference(A)))
#w
print(A.intersection(U.difference(A)))
#x
print(U)
#y
print(U.difference(A)|U.difference(C))
#z
print(U.difference(A.union(B)))
#aa
print(U.difference(A) & U.difference(B))
#ab
print(U.difference(B-C))
#ac
print(A.union(U.difference(B)))
#ad
print(U.difference(B)-U.difference(A))