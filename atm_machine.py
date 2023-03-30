def register_account(database):
    print()
    username_reg = input('Username: ')
    password_reg = input('Password: ')

    if username_reg not in database:
        database[username_reg] = [password_reg, 0]
        return [username_reg, password_reg, database[username_reg][1]]
    else:
        return False


def log_in(database):
    print()
    username_log = input('Username: ')
    password_log = input('Password: ')

    if username_log in database and database[username_log][0] == password_log:
        return [username_log, password_log]
    else:
        return False


def database_inspect(database):
    print()
    if len(database) > 0:
        print('------ ACCOUNTS ------')
        for key, value in database.items():
            print(f'Username: {key}')
            print(f'Password: {value[0]}')
            print(f'Balance:  {format(value[1], ".2f")}$')
            print('----------------------')
        print()
    else:
        print('No records in the database!', '\n')


def user_logged_in():
    while True:
        print('1. Deposit')
        print('2. Withdraw')
        print('3. Current balance')
        print('4. <- Log out', '\n')
        operation_second = int(input('Select operation: '))

        if operation_second == 1:
            deposit(accounts_database, username)
        elif operation_second == 2:
            withdraw(accounts_database, username)
        elif operation_second == 3:
            balance_check(accounts_database, username)
        elif operation_second == 4:
            print()
            return


def deposit(database, username_deposit):
    print()
    amount = float(input('Amount to deposit: '))
    database[username_deposit][1] += amount
    print()
    print(f'You have just deposited {format(amount, ".2f")}$!', '\n')


def withdraw(database, username_withdraw):
    print()
    amount = float(input('Amount to withdraw: '))
    print()
    if database[username_withdraw][1] - amount >= 0:
        database[username_withdraw][1] -= amount
        print(f'You have just withdrawn {format(amount, ".2f")}$!', '\n')
    else:
        print(f'Withdraw failed!', '\n')


def balance_check(database, username_check):
    print()
    print(f'Current balance: {format(database[username_check][1], ".2f")}$', '\n')


accounts_database = {}
username, password = None, None

# Creating the text file if it does not exist
database_file = open('database.txt', 'a')
database_file.close()

# Opening the text file and reading all items
database_file = open('database.txt', 'r')
records = database_file.read().splitlines()

# Splitting the data into different nested lists
# Each nested list contains the info of exactly 1 account
records = [records[x:x+3] for x in range(0, len(records), 3)]

for account in records:
    account_name = account[0]
    account_password = account[1]
    account_balance = float(account[2])
    accounts_database[account_name] = [account_password, account_balance]
database_file.close()

while True:
    print('1. Register an account')
    print('2. Log in ->')
    print('3. Inspect database')
    print('4. Save & Exit', '\n')
    operation = int(input('Select operation: '))

    if operation == 1:
        registered = register_account(accounts_database)
        # Writing down the data only if the registration
        # is successful (No other username matches the current)
        if registered:
            print()
            print('Registration successful!', '\n')
            database_file = open('database.txt', 'a')
            database_file.write(registered[0] + '\n')
            database_file.write(registered[1] + '\n')
            database_file.write(str(registered[2]) + '\n')
            database_file.close()
        else:
            print()
            print('Registration failed!', '\n')

    elif operation == 2:
        # Returns either a list containing the
        # username and password or False
        logged_in = log_in(accounts_database)

        # Proceeding to the next menu if the user prompted
        # the correct username - password combination
        if logged_in:
            print()
            print('Login successful!', '\n')
            username = logged_in[0]
            password = logged_in[1]
            user_logged_in()
        else:
            print()
            print('Login failed!', '\n')

    elif operation == 3:
        # Printing all usernames, passwords and balances
        database_inspect(accounts_database)

    elif operation == 4:
        # Saving the updated data
        database_file = open('database.txt', 'w')
        for key_save, value_save in accounts_database.items():
            username = key_save
            password = value_save[0]
            balance = str(value_save[1])

            database_file.write(username + '\n')
            database_file.write(password + '\n')
            database_file.write(balance + '\n')
        database_file.close()

        exit(0)
