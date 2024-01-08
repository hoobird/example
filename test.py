import time

currtime = time.time()
# time.time() gives me the time in seconds from a special 
# time called epoch (1 Jan 1980 00:00 UTC)

print(f"Start game time: {currtime}")
time.sleep(3)

print(f"Current time: {time.time()}")

