"""TASK 1. Answer: NameError"""
def action(a_parameter):
    a_variable = 15
    return a_parameter


action(10)
print(a_variable)



"""TASK 2. Answer: 22"""

i = 18

def just_func():
    global i
    i = 22
    return i

just_func()
print(i)


"""TASK 3. Answer: 182"""
def action_1():

  x = 123

  def action_2():
    nonlocal x
    x = 182
  action_2()
  return x

print(action_1())


"""TASK 4. Укажите переменные ТОЛЬКО локального пространства имён? Answer: a, b, c """
s, j = 3, 12


def some_action(a, b):
    c = 5
    print(locals())


print(some_action(8, 7))