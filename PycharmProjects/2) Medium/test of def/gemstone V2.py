def flower():
    print('; '.join(['flower' if i % 2 == 0 else 'gemstone' for i in range(len(input().split(', ')))]))

flower()