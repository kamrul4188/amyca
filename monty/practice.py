users = [['admin', 'admin123', 4], ['kamrul', 'kamrul123', 3]]

new_user = []


access_level = 0


def check_user(user_id, usre_pw):
    try:
        for i, user in enumerate(users):
            temp_user_id = users[i][0]
            temp_user_pw = users[i][1]
            set_user_level = users[i][2]

            if temp_user_id == user_id and temp_user_pw == user_pw:
                print('Access Grantred !!!!!')

                return set_user_level
        print('Access Not Grantred !!!!')

    except ValueError:
        print('user id or passowd not match')


while True:
    print('\nCurrent ID: admin, PW: admin123 or ID: kamrul PW: kamrul123\n ')
    user_id = input('Please Enter User_ID: ')
    user_pw = input('Please Enter Password: ')
    access_level = check_user(user_id, user_pw)
    print(access_level)

    if access_level is 4:
        print('Welcom to ' + str(user_id))
        print('Your previlage level is ' + str(access_level))

        while True:
            user_input = input('Please enter your command ')
            print('Your command is : ' + str(user_input))

    elif access_level is 3:
        print('Welcome to' + str(user_id))
        print('Your previlage level is ' + str(access_level))

        while True:
            user_input = input('Please enter your command: ')
            print('Your Command is: ' + str(user_input))

