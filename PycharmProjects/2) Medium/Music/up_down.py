new = open("321.txt", "a", encoding="utf-8")

with open('123.txt', "r", encoding="utf-8") as fp:
    lines = fp.readlines()

line_count = sum(1 for line in fp)


print(lines[45])
#print(line_count)
#while line_count > 0:
#    new.write(file(line_count))