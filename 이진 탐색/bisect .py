from bisect import bisect_left, bisect_right

a=[2,3,4,4,8]
x=4

print(bisect_left(a,3))
print(bisect_right(a,8))
