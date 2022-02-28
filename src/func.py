import time
import os

def count_file(filename):
    count = 0
    for x in os.listdir():
        if x.find(filename) != -1:
            count += 1
    return count

def create_csv(filename, df):
    num = count_file(filename)
    filenow = ""
    if num <= 1:
        filenow = filename + '.csv'
    else:
        filenow = filename + str(num) + '.csv'
    filename = filenow

    if os.path.exists(filename):
        res = file_number(filename)
        if res == 1:
            pos = filename.find(".csv")
            newname = filename[:pos] + str(res+1) + '.csv'
            df.to_csv(newname, index=False)
            print(newname, "successfully created.")
        else:
            pos = filename.find(str(res))
            newname = filename[:pos] + str(res+1) + '.csv'
            df.to_csv(newname, index=False)
            print(newname, "successfully created.")
    else:
        df.to_csv(filename, index=False)
        print(filename, "successfully created.")

def file_number(string):
    pos = string.rfind('_')
    pos2 = string.rfind('.')
    res = -1
    for x in range(pos,pos2):
        if string[x].isdigit():
            res = x
            break
    strnum = string[res:pos2]
    if strnum:
        return int(strnum)
    else:
        return 1

def get_followers(profile):
    seconds = time.time()
    lst = []
    count = 0
    for f in profile.get_followers():
        lst.append(f.username)
        count = count + 1
    print( "Total Followers :",  count)

    followers_time = time.time()
    print("Time spent on Followers :" + str(followers_time - seconds))
    return lst

def get_following(profile):
    seconds = time.time()
    lst = []
    count = 0
    for f in profile.get_followees():
        lst.append(f.username)
        count = count + 1
    print( "Total Following :",  count)

    followers_time = time.time()
    print("Time spent on Following :" + str(followers_time - seconds))
    return lst

def get_fback(fers, fing):
    len_followers = len(fers)

    pop_iter = 0
    for x in range(len_followers):
        if fers[x - pop_iter] in fing:
            fing.remove(fers[x - pop_iter])
            fers.pop(x - pop_iter)
            pop_iter += 1
    return fers