import os
files = os.listdir('name')
new_dict = {}
for file in files:
    file = f'name/{file}'
    with open(file,'rt', encoding="utf-8" ) as f:
        new_dict[file] = (sum(1 for line in f))
len_list_sorted = sorted(new_dict, key = lambda k:new_dict[k])

with open('4.txt','a', encoding="utf-8" ) as f:
    for k in len_list_sorted:
        with open(k,'rt',encoding="utf-8" ) as x:
            X = x.read()
            f.write(f"{k}"+'\n')
            f.write(f"{new_dict[k]}"+'\n')
            f.write(X+'\n')