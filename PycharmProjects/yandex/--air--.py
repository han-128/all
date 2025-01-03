*a, = iter(input, '')
ma = len(max(a, key=len))

fmt = ('{:-^' + str(ma) + '}') + ('\n{:-^' + str(ma) + '}') * (len(a) - 1)
print(fmt.format(*a[::-1]))