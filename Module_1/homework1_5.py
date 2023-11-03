integ = int(input())  # первое число
flot = float(input())  # второе число
intg_pos = int(input())  # третье число
print(f"{integ:0=+10}")  # с первым и вторым числами код работает
#проблема началась с третьим числом
#print(f"{round(flot,2):#>10}")
print(f"{flot:#>10.2f}")
res_current = f"{intg_pos :0>16b}"
res_current = str(res_current)
result = str(res_current)
result = (result[::-1])
print('_'.join(result[i:i+4] for i in range(0, len(result), 4))[::-1])