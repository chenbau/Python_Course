import myFuncs
import platform
import csv

with open("test.csv", "w") as f:
    reader = csv.reader(f, delimiter="\t")
    # for i, line in enumerate(reader):
    #     print 'line[{}] = {}'.format(i, line)



# x = platform.system()
# print(x)

x = dir(platform)
print(x)
myFuncs.person1