import time

time_start = time.time()
time.sleep(3)
time_stop = time.time()
print("Время запуска", time_start)
print("Время завершения", time_stop)
print("Прошло времени", time_stop - time_start)
