# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Dictionary Methods Cheat Sheet

# %%
# Definition

# x = {key1:value1, key2:value2}

# Operations

# len(dictionary) - Returns the number of items in the dictionary
# for key in dictionary - Iterates over each key in the dictionary
# for key, value in dictionary.items() - Iterates over each key,value pair in the dictionary
# if key in dictionary - Checks whether the key is in the dictionary
# dictionary[key] - Accesses the item with key key of the dictionary
# dictionary[key] = value - Sets the value associated with key
# del dictionary[key] - Removes the item with key key from the dictionary

# Methods

# dict.get(key, default) - Returns the element corresponding to key, or default if it's not present
# dict.keys() - Returns a sequence containing the keys in the dictionary
# dict.values() - Returns a sequence containing the values in the dictionary
# dict.update(other_dictionary) - Updates the dictionary with the items coming from the other dictionary. Existing entries will be replaced; new entries will be added.
# dict.clear() - Removes all the items of the dictionary


# %%
file_counts = {"jpg": 10, "txt": 14, "csv": 3, "py": 23}
for extension in file_counts:
    print(extension)


# %%
for ext, amount in file_counts.items():
    print("There are {} files with the .{} extension".format(amount, ext))


# %%
file_counts.keys()


# %%
file_counts.values()


# %%
def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result


count_letters(
    "The permissions of a file in a Linux system are split into three sets of three permissions: read, write, and execute")


# %%
wardrobe = {"shirt": ["red", "blue", "white"], "jeans": ["blue", "black"]}
for cloths in wardrobe:
    for color in wardrobe[cloths]:
        print("{} {}".format(color, cloths))


# %%
# The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values.
# Fill in the blanks to generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).

def email_list(domains):
    emails = []
    print(domains)
    for domain, users in domains.items():
        for user in users:
            emails.append(user + "@" + domain)

    return(emails)


print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": [
      "barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))


# %%
# The groups_per_user function receives a dictionary, which contains group names with the list of users.
# Users can belong to multiple groups. Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values.

def groups_per_user(group_dictionary):
    user_groups = {}

    # Go through group_dictionary
    for group, users in group_dictionary.items():
        # Now go through the users in the group
        for user in users:
            # Now add the group to the the list of
            # groups for this user, creating the entry
            # in the dictionary if necessary
            if len(user_groups[user]) == 0:
                groups_list = []
            groups = group_dictionary[group]
            if user in groups and group not in groups_list:
                groups_list.append(group)

            user_groups[user] = groups_list

    return(user_groups)


print(groups_per_user({"local": ["admin", "userA"],
                       "public":  ["admin", "userB"],
                       "administrator": ["admin"]}))


# %%
