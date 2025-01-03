t = input()

if (("*" in t) or ("?" in t)) and (not (" " in t)):
    print("Возможно маска")
else:
    print("Нет, это не маска!")
