# make sure to install INSTALOADER and OS library.

import instaloader
import input, func
import pandas as pd

L = instaloader.Instaloader()

target = input.target

username = input.user
password = input.passw
try:
    try:
        L.load_session_from_file(username) 
    except:
        L.login(username, password) 
except:
    raise Exception("Can't login, please check your credentials and try again.")
    
try:
    profile = instaloader.Profile.from_username(L.context, target)
except:
    raise Exception("Can't get the profile, please check the username's target and try again.")

try:
    fers = func.get_followers(profile)
    fing = func.get_following(profile)
except:
    raise Exception("Can't get data from profile, please try again.")

fname = target + '_AnalyzedResult' 

try:
    df = pd.DataFrame(func.get_fback(fers, fing), columns=[str(func.time.ctime(func.time.time()))])
    func.create_csv(fname, df)
except:
    Exception("Can't make the csv file, please try again.")