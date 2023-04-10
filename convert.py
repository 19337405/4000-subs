import datetime
f = open("4000.srt", "w")
i = 0

for i in range(4000):
    f.write(str(i + 1) + "\n" + str(str(datetime.timedelta(milliseconds=(i) * 10))[:11] + " --> " + str(datetime.timedelta(milliseconds=(i + 1) * 10))[:11]).replace(".", ",") + "\n" + str(i + 1) + "\n\n")

f.close()
