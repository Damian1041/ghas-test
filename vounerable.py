def execute_user_input(user_input):
    eval(user_input)

user_code = input("Podaj kod do wykonania: ")
execute_user_input(user_code)
