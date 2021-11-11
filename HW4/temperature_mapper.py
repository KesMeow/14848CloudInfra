import sys

quality_flags = [0, 1, 4, 5, 9]
for line in sys.stdin:
    line = line.strip()
    temperature = int(line[87:92])
    quality = int(line[92])
    if ((temperature != 9999) and (quality in quality_flags)):
        print('%s\t%d' % (line[15:23], int(line[87:92])))