from data import data

f = open("converted.txt", "w")

f.write("{")

count = 0
row_count = 0
for i in range(len(data)):
    if count == 0:
        f.write("{")
        f.write('0x%02X' % data[i])
        f.write(", ")
        count += 1
    elif count == 1:
        f.write('0x%02X' % data[i])
        f.write(", ")
        count += 1
    elif count == 2:
        f.write('0x%02X' % data[i])
        f.write("}, ")
        count = 0
    row_count += 1
    if row_count == 12:
        f.write("\n")
        row_count = 0

f.write("}")

f.close()