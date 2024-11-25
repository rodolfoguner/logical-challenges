import math

students, min_litters, ml_per_student = map(int, input().split())
min_coffee = ml_per_student * students / (min_litters * 1000)

print(math.ceil(min_coffee) * min_litters)
