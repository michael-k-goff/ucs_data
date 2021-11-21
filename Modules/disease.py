# Disease origins. Should be in parent directory

cause_dict = {}
total = 0

with open('Modules/disease.txt', 'r') as fp:
    line = fp.readline()
    cnt = 1
    while line:
        blocks = line.strip().split(' ')
        year_block = -1
        cause_block = -1
        for i in range(len(blocks)):
            if blocks[i].isnumeric():
                year = int(blocks[i])
                if year >= 1000 and year <= 9999:
                    year_block = i
                    for j in range(i+2, len(blocks)):
                        if cause_block == -1 and not blocks[j].isnumeric():
                            cause_block = j
        if year_block >= 0:
            if blocks[cause_block] not in ["Bushmeat","Unspecified","Other"]:
                cause = blocks[cause_block] + " " + blocks[cause_block + 1]
            else:
                cause = blocks[cause_block]
            if cause not in cause_dict:
                cause_dict[cause] = 0
            cause_dict[cause] += 1
            total += 1
        line = fp.readline()
        cnt += 1
        
print(cause_dict)
print(total)