log_file = open("ClosePeriod_log.txt", "r").readline()
addit_array = [str(i) for i in range(8)]
addit_array_2 = log_file.split(" ")[:-1]
addit_array.extend(addit_array_2)
print(list(set(addit_array)))