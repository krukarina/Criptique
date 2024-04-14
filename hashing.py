import bcrypt


def hash_masterpwd(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8'), salt

# def checkpwd(password, hashed_password, email):
#   salt = get_salt(email)
#  if not salt:
#     print('User not found.')
#    return False
# else:
#   hash_input = bcrypt.hashpw(password.encode('utf-8'), salt.encode('utf-8'))
#  check = bcrypt.checkpw(hash_input, hashed_password)
# return check
