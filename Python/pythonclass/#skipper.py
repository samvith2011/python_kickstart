'''
1. Kaee sure i can print from 1-30
2. Add an if statement thsat says if therr is a remainder when dividing by 4, skip but if  it does not, do it



'''
def number_skip():
    for i in range(1,31):
        if i % 4 == 0:
            continue
        if i % 4 != 0:
            print(i)


number_skip()