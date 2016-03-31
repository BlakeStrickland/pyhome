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
            average = round(sum(nums)/len(nums), 3)
        except ValueError:
            data = str(data)
            items.append(data)
            string = "".join(items)

print("There are {} string item(s).".format(len(items)))
print("There are {} number item(s).".format(len(nums)))
if string != "":
    print(string)
if average != "":
    print(average)
