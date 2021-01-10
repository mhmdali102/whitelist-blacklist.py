white_list = []
black_list = []
users_list = []

num = int(input("Enter number of users: "))
for i in range(num):
    name = input("Enter user name: ")
    while name == "":
        name = input("Enter non empty user name: ")
    users_list.append(name)
for user in users_list:
    if user not in black_list:
        white_list.append(user)

print(f"Only {str(len(white_list))} users are accepted to login: ")
print(*sorted(white_list), sep="\n")