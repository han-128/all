for i in range(2023,10**10, 2023):
    if (i%10==4) and (str(i)[2:6] == '2139') and (str(i)[0] == '1'):
        print(i, i//2023)

# 1?2139*4