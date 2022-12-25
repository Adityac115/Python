def group_to_user(group_dictionary):
    user_groups={}
    for group,users in group_dictionary.items():       # group will iterate over all group values while users will iterate over all users,
        for user in users:                                       # user will iterate over users as there as multiple users for 1 group
            if user not in user_groups:                           #to check if we already encouter this user , if yes then,
                user_groups[user]=[]                              #we create the user as a key and a empty list as its value for now,
            user_groups[user].append(group)                       #then we append the groups in that list we created as the value of users
    return user_groups                                            # returning the value of user_groups                            



print(group_to_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))