def spy_game(list):

    for i in range(0, len(list) - 1):

        if list[i] == 0 and list[i+1] == 0 and list[i+2] == 7 :

            return True


    return False

a = [int(s) for s in input().split()]

print(spy_game(a))