import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits

password_list = list(lower[:4] + upper[:4] + digits[:4])
random.shuffle(password_list)

password = "".join(password_list)

print(password)