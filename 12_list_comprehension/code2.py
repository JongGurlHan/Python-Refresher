friends = ["Sam", "Samantha", "Saeed"]
starts_s =[friend for friend in friends if friend.startswith("S")]

# for friend in friends:
#     if friend.startswith("S"):
#         starts_s.append(friend)

print(friends)
print(starts_s)
print(friends is starts_s)
print(friends[0] == starts_s[0])