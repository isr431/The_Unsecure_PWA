import bcrypt


def hash_pw(password):
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(password.encode(), salt)

    return hash, salt
