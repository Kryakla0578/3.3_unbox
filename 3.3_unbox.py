
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b= 25,c=[1,2,3])

values_list = [54.32, 'Stroka']
values_dict = {'a': 78, 'b': 'stroka', 'c': False}

print_params(*values_list)
print_params(*values_dict)
print_params(**values_dict)

