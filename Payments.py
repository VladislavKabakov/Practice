print("Введите кол-во счетов")
N = int(input())
print("Введите количество менеджеров")
M = int(input())

MaxPos = pow(10,8) + 1
full_sum = 0

for _ in range(N):
    sh = int(input())
    full_sum += sh
    MaxPos = min(sh, MaxPos)

payment = full_sum // M
print(MaxPos) if (payment > MaxPos) else print(payment)




    
