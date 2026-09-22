time = int(input())

time_h = time // 3600
time_m = time // 60 % 60
time_s = time % 60

print(f'{time_h:02d}:{time_m:02d}:{time_s:02d}')