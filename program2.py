h = input("Enter gender in terms of M or F: ")
hg = float(input("Enter hemoglobin value (g/l): "))

if h == 'M':
    if 134 <= hg <= 167:
        print("normal level  hemoglobin for males.")
    elif hg < 134:
        print("low level  hemoglobin for males.")
    else:
        print("high level  hemoglobin for males.")
elif h == 'F':
    if 117 <= hg <= 155:
        print("normal level  hemoglobin  for females")
    elif hg < 117:
        print("low level of hemoglobin females.")
    else:
        print("high level of hemoglobin for females.")
else:
    print("enter correct gender")