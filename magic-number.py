def calculate_salary_bonus(salary):
    return salary + (salary * 0.15)


# This code below is a refactored version of the original code above.

BONUS_PERCENTUAL = 0.15

def calculate_salary_bonus(salario):
    return salario + (salario * BONUS_PERCENTUAL)


######################################################################

data = ["Ana", "Silva", 28, "Engenheira"]

print(data[0])
print(data[1])
print(data[2])
print(data[3])

# This code below is a refactored version of the original code above.

NOME = 0
SOBRENOME = 1
IDADE = 2
PROFISSAO = 3

print(data[NOME])
print(data[SOBRENOME])
print(data[IDADE])
print(data[PROFISSAO])