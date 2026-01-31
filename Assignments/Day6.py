import numpy as np

# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(a)
# print(a.shape)
# print(a.size)
# print(a.dtype)
# print(a.ndim)

# zeros = np.zeros((2, 3))
# print(zeros)

# ones = np.ones((2, 3))
# print(ones)

# range_array = np.arange(0,10,2)
# print(range_array)

# range_array = np.arange(10).reshape(2,5)
# print(range_array)

# linespace_array = np.linspace(0,1,5)
# print(linespace_array)

# b=np.random.randint(0,10,3)
# print(b)

# b1=np.random.randint(0,10,(2,3))
# print(b1)

# b2=np.random.exponential(1,3)
# print(b2)

# a=np.array([[1, 2, 3, 4]])
# b=np.array([[5, 6, 7, 8]])
# c=a+b
# print(c)
# print(np.mean(c))
# print(np.std(c))
# print(np.median(c))
# print(np.max(c))
# print(np.min(c))
# print(np.sum(c))
# print(np.prod(c))
# print(np.sin(1))

# print(a.size)


scores = np.array([78, 85, 92, 70, 88, 94, 67, 73, 82, 90,
                   76, 84, 95, 69, 80, 87, 91, 77, 83, 86,
                   79, 81, 89, 72, 68, 93, 74, 75, 96, 88])

average_score=np.mean(scores)
print(average_score)

max_score=np.max(scores)
print(max_score)

std_score=np.std(scores)
print(std_score)

above_average=scores[scores>average_score]
print(above_average)