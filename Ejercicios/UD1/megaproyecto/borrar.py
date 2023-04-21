my_list = ['Mary','had','a','little','lamb']

def f(my_list):
    del my_list[3]
    my_list[3] = 'ram'

f(my_list)
print(my_list)