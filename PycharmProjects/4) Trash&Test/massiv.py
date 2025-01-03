'''
spisok

lst = [1, 1.0 ,"1", True, [1,2,3]]
lst.append(1)
print(lst)
print(lst.count(1))

lst[-1] = 2
print(lst)

lst.insert(1, 3.14)
print(lst)

lst.pop(4)
print(lst)

lst.remove('1')
print(lst)

print(len(lst))


#kartej

tpl = (1,2,3)

tempList = list(tpl)
tempList.append(4)
tpl = tuple(tempList)
print(tpl)



#set

lst = [1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5]
s = set(lst)
if len(lst) == len(s):
    print('дубликатов нет')
else:
    print('есть повторения')


'''

# dict словарь

d = {'у': 0,'е': 0,'ы': 0,'а': 0,'о': 0,'э': 0,'я': 0,'и': 0,'ю': 0,}
text = 'В целом, конечно, укрепление и развитие внутренней структуры влечет за собой процесс внедрения и модернизации экономической целесообразности принимаемых решений'

for i in text:
    if i in d:
        d[i] += 1
print(d)

for key, value in d.items():
    print(f'{key} - {value}')

