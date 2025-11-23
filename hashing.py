import bcrypt


def hash_password(password):
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(password.encode(), salt)

    return hash, salt
