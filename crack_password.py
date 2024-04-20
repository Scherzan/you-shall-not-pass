import time
import numpy as np

real_password = "1234"

def check_password(password): 
    if len(password) != len(real_password):
        return False
    for x, y in zip(password, real_password):
        time.sleep(0.05) # Simulates the wait time of the safe's mechanism
        if int(x) != int(y):
            return False
    return True


# 1. Brute force:
def brute_force_random():
    possible_combinations = int("".join(np.repeat(str(9), len(real_password)).tolist()))
    for pw_candidate in np.arange(0, possible_combinations, dtype=int).tolist():
        if not check_password(str(pw_candidate)):
            continue
        else:
            return str(pw_candidate)

start_brute_force = time.time()
cracked_password = brute_force_random()
end_brute_force  = time.time()
print(f"""An ordinary brute force attack identified {cracked_password} as the real password in {end_brute_force - start_brute_force} seconds.""")
    


# 2. Use a timing attack
def timimng_attack():
    pw_candidate = ["0","0","0","0"]
    check_time = 0.052
    for position_dig in range(4):
        for dig in np.arange(0, 10, dtype=int).tolist():
            pw_candidate[position_dig] = str(dig)

            start = time.time()
            if check_password("".join(pw_candidate)):
                return "".join(pw_candidate) 
            time_taken = time.time() - start

            if time_taken > check_time:
                check_time = check_time + 0.05
                break
  

start_brute_force = time.time()
cracked_password = timimng_attack()
end_brute_force  = time.time()
print(f"""The timing attack identified {cracked_password} as the real password in {end_brute_force - start_brute_force} seconds.""")


# 3. Use a password list
with open('10k-most-common.txt', 'r') as file:
    data = file.read()
data_into_list = data.split("\n") 

def brute_force_list():
    for pw_candidate in data_into_list:
        if not check_password(pw_candidate):
            continue
        else:
            return str(pw_candidate)
        
start_brute_force = time.time()
cracked_password = brute_force_list()
end_brute_force  = time.time()
print(f"""Brute force attack using 10k-most-common.txt list on common passwords identified {cracked_password} 
      as the real password in {end_brute_force - start_brute_force} seconds.""")
