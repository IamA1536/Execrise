import copy

a = [1, 2, 3, 4, ['a', 'b', 'c']]

b = a  # 与a指向同一个列表
c = a[:]  # 浅拷贝，类copy
d = copy.copy(a)  # 浅拷贝，指向之前的地址()
e = copy.deepcopy(a)  # 深拷贝，寻常的copy，将被复制对象完全再复制一遍作为独立的新个体单独存在
f = copy.copy(d)

a.append(5)
a[4].append('d')
a.append('a')

print("a = ", a)
print("memory : ", id(a))
print("Use = ", b)
print("memory : ", id(b))
print("Use [:] ", c)
print("memory : ", id(c))
print("Use copy ", d)
print("memory : ", id(d))
print("Use deepcopy ", e)
print("memory : ", id(e))
print("Double copy ", f)
print("memory : ", id(f))
