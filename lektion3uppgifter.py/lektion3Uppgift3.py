from password_spraying import user_credentials, password_list

# 3. Password spraying
# Ladda ner password_spraying.py från ITHSdistans.
# Kontrollera om någon utav lösenorden i password_list matchar lösenordet för en
# user i user_credentials
# Skriv resultatet till fil (och i konsolen) med varje lösenord per user och om det
# lyckades eller inte.
# Exempel:
# user1: 123456 -> failed
# user1: Welcome123 -> failed

# set1 = set(user_credentials.values())
# set2 = set(password_list)

# passwords = set1 & set2

# print(passwords)

# result = {"user1": "lyckad", "admin": "inte lyckad", "user2": "lyckad", "guest": "lyckad"}

with open("password_check.txt", "w") as file_output:
    for users,passwords in user_credentials.items():
        for passwrd in password_list:
            if passwrd == passwords:
                resultat = (f"{users}: {passwrd} -> lyckades")
            else:
                resultat = (f"{users}: {passwrd} -> lyckades inte")
            print(resultat)