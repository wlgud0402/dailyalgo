def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    my_power = yourLeft + yourRight
    friend_power = friendsLeft + friendsRight
    my_strong_arm = max(yourRight, yourLeft)
    friends_arm = max(friendsLeft, friendsRight)

    if my_strong_arm == friends_arm and my_power == friend_power:
        return True
    else:
        return False
