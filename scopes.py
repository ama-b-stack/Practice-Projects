#y = 5

#def set_x(y):
#    print('inner y:', y)
#    x = y
#    y = x

#set_x(10)

#print('outer y:', y)

# will print:
# inner y: 10
# outer y: 5

#####

y = 5

def set_x(z):
    x = z
    global y
    global a
    y = x
    a = 7

print('y before set_x:', y)
set_x(10)

print('y after set_x:', y)
print('a after set_x:', a)

# will print:
# y before set_x: 5
# y after set_x: 10
# a after set_x: 7
