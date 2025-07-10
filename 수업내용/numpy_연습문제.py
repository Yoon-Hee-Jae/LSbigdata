import numpy as np
# 연습 문제 1
a = np.array([1, 2, 3, 4, 5])
plus_a = a + 5
print([plus_a])

# 연습 문제 2
a = np.array([12, 21, 35, 48, 5])
a[::2]

# 연습 문제 3
a = np.array([1, 22, 93, 64, 54])
np.max(a)
max(a)

# 연습 문제 4
a = np.array([1, 2, 3, 2, 4, 5, 4, 6])
a
a.dtype
np.unique(a)

##################################################

set_a = set(a)
list_a = list(set_a)
np.array(set_a)

# 연습 문제 5
a = np.array([21, 31, 58])
b = np.array([24, 44, 67])
c = np.empty(a.size+b.size,dtype=a.dtype)
c[::2] = a
c[1::2] = b
c

# 연습 문제 6
a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9])
c = a[:4] + b
c

# 연습 문제 7 
a = np.array([1, 3, 3, 2, 1, 3, 4, 2, 2, 2, 5, 6, 6, 6, 6])
unique, counts = np.unique(a,return_counts=True)
most_frequent = unique[np.argmax(counts)] # argmax는 최대값의 위치를 반환
most_frequent

# 연습 문제 8
a = np.array([12, 5, 18, 21, 7, 9, 30, 25, 3, 6])
multiples_3 = a[a % 3 == 0]
multiples_3

# 연습 문제 9
a = np.array([10, 20, 5, 7, 15, 30, 25, 8])
np.median(a)
lower_a = a[a<np.median(a)]
upper_a = a[a>np.median(a)]
print(lower_a)
print(upper_a)

# 연습 문제 10
a = np.array([12, 45, 8, 20, 33, 50, 19])
median_num = np.median(a)
closest_num = a[np.argmin(np.abs(a - median_num))]
closest_num