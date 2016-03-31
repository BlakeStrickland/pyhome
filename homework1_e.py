
from statistics import median
from statistics import stdev
import re

string_lengths = []
num_of_e = []
items = []
nums = []
string = ""
average = 0
print("Enter a word or a space to quit ")
while True:
    data = input("> ")

    if data == "":
        break
    else:
        try:
            data = int(data, 10)
            nums.append(data)
            the_median = median(nums)
            standard_dev = stdev(nums)
            average = round(sum(nums)/len(nums), 3)
        except ValueError:
            data = str(data)
            items.append(data)
            average_length = sum(len(string) for string in items)/len(items)
            num_of_e.append(len(re.findall(r"e", data)))
            string = "".join(items)

if string != "":
    print("There are {} string item(s).".format(len(items)))
    print(string)
    print("The average string length is {}".format(average_length))
    print("All the e counts: {}".format(num_of_e))
if average != 0:
    print("There are {} number item(s).".format(len(nums)))
    print("The average is {}".format(average))
    print("The median is {}".format(the_median))
    print("The standard deviation is {}".format(standard_dev))
