s = '!' + 30 * '1' + 30 * '2' + 50 * '3' + 50 * '4'
while ('!1' in s) or ('!2' in s) or ('!3' in s) or ('!4' in s):
    if '!1' in s:
        s = s.replace('!1', '1244!', 1)
    if '!2' in s:
        s = s.replace('!2', '412!', 1)
    if '!3' in s:
        s = s.replace('!3', '422!', 1)
    if '!4' in s:
        s = s.replace('!4', '111!', 1)
print(s.count('1'))