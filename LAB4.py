from numpy import *

# Question 1
# 1

q1_a = array([[1, 1, 1], [0, 1, 1], [0, 0, 1]])
q1_b = array([[7, 5, 3], [0, 7, 5], [0, 0, 7]])

def search_matrix_ab_minus_ba(a, b):
    return dot(a, b) - dot(b, a)

print("""
Question # 1 : 
""", search_matrix_ab_minus_ba(q1_a, q1_b))

# 2

q2_a = [[-1, 0, 2], [0, 1, 0], [1, 2, -1]]

def matrix_in_exponentiation(a, b):
    return linalg.matrix_power(a, b)

print("""
Question # 2 : 
""", matrix_in_exponentiation(q2_a, 2))

# 3

q3_a = [[3, 0, 7], [-4, 2, 3], [-1, 1, 2]]
q3_b = [[1], [2], [4]]

def search_multiply_a_b(a, b):
    return dot(a, b)

print("""
Question # 3 : 
""", search_multiply_a_b(q3_a, q3_b))

# 4

q4_a = [[1, 5, -5], [4, 0, 3], [2, -10, 3]]

def determinant(a):
    return linalg.det(a)

print("""
Question # 4 : 
""", int(determinant(q4_a)))

# 5

q5_a = [[1, 2, 3, 4], [-2, 1, -4, 3],
        [3, -4, -1, 2], [4, 3, -2, -1]]

print("""
Question # 5 : 
""", int(determinant(q5_a)))

# 6

q6_a = [[1, 2, -3], [0, 1, 2], [0, 0, 1]]

def wrapped_matrix(a):
    return linalg.inv(a)

print("""
Question # 6 : 
""", wrapped_matrix(q6_a))

# 7

q7_a = [[1, 2, 3, 4], [3, -1, 2, 5],
        [1, 2, 3, 4], [1, 3, 4, 5]]

def rank_matrix(a):
    return linalg.matrix_rank(a)

print("""
Question # 7 : 
""", rank_matrix(q7_a))

# 8

equation = """14x + 4y + 6z = 30
              5x - 3y + 2z = 15
              10x - 11y + 5z = 36
"""
q8_a = [[14, 4, 6], [5, -3, 2], [10, -11, 5]]
q8_b = [30, 15, 36]
q8_1_b = [[30], [15], [36]]

def kramar_matrix(a, b):
    return linalg.solve(a, b)

def matrix_Kramar(a, b):
    x_y_z = []
    det_A = determinant(a)
    if det_A != 0:
        x = matrix(a)
        x[:, 0] = b
        x_y_z.append(round(determinant(x)/det_A))
        y = matrix(a)
        y[:, 1] = b
        x_y_z.append(round(determinant(y) / det_A))
        z = matrix(a)
        z[:, 2] = b
        x_y_z.append(round(determinant(z) / det_A))
        return x_y_z
    else:
        print("Withot roots")


def matrix_method(a, b):
    return linalg.solve(a, b)

def matrix_Method(a, b):
    return linalg.inv(a).dot(b)

print("""
Question # 8 : 
""", kramar_matrix(q8_a, q8_b))

print("""
Question # 8.1 : 
""", matrix_method(q8_a, q8_1_b))

print("""
Question # 8.2 : 
""", matrix_Method(q8_a, q8_b))

print("""
Question # 8.3 : 
""", matrix_Kramar(q8_a, q8_1_b))

# Question 2

a = random.randint(-10, 11, (4, 4))
print("""A = 
""", a)

def seach_in_row(a):
    row = []
    for i in range(len(a)):
        counter = 0
        for j in range(len(a)):
            if a[i][j] < 0:
                counter += 1
        row.append([counter])
    return row

def seach_in_col(a):
    col = []
    for i in range(len(a)):
        counter = 0
        for j in range(len(a)):
            if a[j][i] < 0:
                counter += 1
        col.append(counter)
    return col


print("""
Question # 2 : 
In row 
""", seach_in_row(a),
"""
In column
""", seach_in_col(a))
