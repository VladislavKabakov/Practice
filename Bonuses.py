print("Number of employers: ")
n_workers = int(input()) 
print("Number of accounts: ")
m_accounts = int(input()) 
account_values = []
print("Account values: ")
for i in range(m_accounts):
    account_values.append(int(input()))

max_bonus = int(sum(account_values)/n_workers)
bonus_count = 0
for value in account_values:
    bonus_count += value//max_bonus
print(bonus_count)


def calculate_max_bonus_amount(account_values, n_workers):
    max_bonus = int(sum(account_values)/n_workers)
    if max_bonus == 0:
        return 0
    for bonus_amount in range(max_bonus,0,-1):
        if available_bonus_count(account_values, bonus_amount)>=n_workers:
            return bonus_amount
        
#calculate_max_bonus_amount(account_values, n_workers)       

def available_bonus_count(account_values, bonus_amount):
    bonus_count = 0
    for value in account_values:
        bonus_count += value//bonus_amount
    return bonus_count

def calculate_max_bonus_amount_v2(account_values, n_workers):
    max_bonus = int(sum(account_values)/n_workers)
    if max_bonus == 0:
        return 0
    a = 1
    b = max_bonus
    while True:
        m = (a + b)//2
        if available_bonus_count(account_values,m) >= n_workers:
            a = m
        else:
            b = m
        if b - a==1:
            if available_bonus_count(account_values,b) >= n_workers:
                return b
            else:
                return a

#calculate_max_bonus_amount_v2(account_values, n_workers)
