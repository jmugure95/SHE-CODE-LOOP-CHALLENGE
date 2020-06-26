import sys

names = ["Julia Wakaba","Kelly Knowles","Tonto Dike","Felicia Ngare","Ann Omaro","Leonard Delavive"]

def first_names():
    firsts = []
    for name in names:
        first_name = name.split()[0]
        firsts.append(first_name)
    return firsts
with open('subFolder1/script1.py', 'w') as f:
    sys.stdout = f
    print(first_names(), file=f)
    f.close()