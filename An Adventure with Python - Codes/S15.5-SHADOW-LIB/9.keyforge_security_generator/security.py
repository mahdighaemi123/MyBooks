import random
import string

def generate_key(length):
    # Combine letters and digits
    chars = string.ascii_letters + string.digits
    # Select random characters
    key = "".join(random.choices(chars, k=length))
    return key
