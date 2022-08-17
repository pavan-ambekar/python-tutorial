# %%
str = 'im learning python'
print(str[3])

# %%
str = 'im learning python 3'
print(str[3:11])

# %%
print(str[3:])

# %%
print(str[:11])
# %%
print(str[-7:-4])

# %%
str = '        im learning python 3'
print('before:', str)
x = str.strip()
print('after:', x)
# %%
a = ['BMW', '4', '3', '2', '5', '6']
print('before sort:', a)
a.sort(reverse=True)
print('after sort:', a)
# print(arr)

# %%
str = 'im learning python 3'
print('before:', str)
x = str.replace(' ', '')
x = str.replace('', _)
print('after:', x)
# %%
