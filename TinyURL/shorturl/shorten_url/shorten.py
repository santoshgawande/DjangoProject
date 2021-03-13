import random
import string

# This is not work because at some interval it get collision and it will not work for unique url shorting
def shorten_url(long_url):
    # generate string using CAPITAL, Small letter and digit with k length
    gen_str = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=7))
    return gen_str