nums = []
print("Enter a number or enter to quit ")
while True:
    data = input("> ")

    if data == "":
        break

    else:
        try:
            data = float(data)
            nums.append(data)
            average = round(sum(nums)/len(nums), 3)
        except ValueError:
            print("That's not a number!")
            continue

print("There are {} item(s).".format(len(nums)))
print(nums)
print("The average is: {}".format(average))
