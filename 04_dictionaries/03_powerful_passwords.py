from hashlib import sha256

def login(email, stored_logins, password_to_check):

    if stored_logins[email] == hash_password(password_to_check):
        return True
    
    return False

def hash_password(password):
    return sha256(password.encode('utf-8')).hexdigest()

def main():
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8", #password
        "code_in_place@cip.org": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855", #password
        "student@standford.edu":  "5f4dcc3b5aa765d61d8327deb882cf99" #password
    }

    print(login("example@gmail.com", stored_logins, "word"))
    print(login("example@gmail.com", stored_logins, "password"))

    print(login("code_in_place@cip.org", stored_logins, "Karel"))
    print(login("code_in_place@cip.org", stored_logins, "Karel"))

    print(login("student@standford.edu", stored_logins, "password"))
    print(login("student@standford.edu", stored_logins, "123!456?789"))

if __name__ == "__main__":
    main()

