import json
import time
def main():
    print("Welcome to the ATM")
    account = load_account()
    account_name = input("Enter your account name: ")
    if account_name in account["createaccount"]["name"]:
        print("Account Exist")
    else:
        print("Account doesn't exit")
        while True:
            new = input("Press 1 to create acc: ")
            if new == "1":
                name, pin = create_account()
                account["createaccount"]["name"] = name
                account["createaccount"]["pin"] = pin
                account["deposit"] = 0
                account["withdraw"] = 0
                account["balance"] = 0
                account["history"] = []
                save_account(account)
                print(f"Account of {name} created successfully with pin")
                break
            else:
                print("Entered Invalid Option, Please select 1 to create acc.")
                continue
    print("Press 1. to Deposit\nPress 2. to Withdraw\nPress 3. to Check Balance\nPress 4. to History\nPress 5. to exit")
    chance = 3
    while True:
        try:
            user = input("Enter your option: ")
            if user == "1":
                amount, a_pin = deposit()
                if account["createaccount"]["pin"] != a_pin:
                    chance -= 1
                    if chance == 0:
                        print("You have reached the maximum limit")
                        break
                    else:
                        print(f"Entered pin is incorrect. {chance} attempt(s) left.")
                        continue

                account["deposit"]+=amount
                account["history"].append(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Deposited ${amount}")
                save_account(account)
                print(f"You deposited ${amount}")

            elif user == "2":
                w_amount,a_pin = withdraw()
                if account["createaccount"]["pin"] != a_pin:
                    chance -= 1
                    if chance == 0:
                        print("You have reached the maximum limit")
                        break
                    else:
                        print(f"Entered pin is incorrect. {chance} attempt(s) left.")
                        continue
                else:
                    remaining = account["deposit"] - account["withdraw"]
                    if remaining < w_amount:
                        print(f"You do not have enough balance to withdraw ${w_amount}")
                    else:
                        account["withdraw"]+=w_amount
                        account["history"].append(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Withdrawn ${w_amount}")
                        save_account(account)
                        print(f"Your withdraw of ${w_amount} is successful" )

            elif user == "3":
                a_pin = input("Enter your pin: ")
                if account["createaccount"]["pin"] != a_pin:
                    chance -= 1
                    if chance == 0:
                        print("You have reached the maximum limit")
                        break
                    else:
                        print(f"Entered pin is incorrect. {chance} attempt(s) left.")
                        continue
                else:
                    account["balance"] = account["deposit"] - account["withdraw"]
                    save_account(account)
                    print(f"Your remaining balance is ${account['balance']}")


            elif user == "4":
                a_pin = input("Enter your pin: ")
                if account["createaccount"]["pin"] != a_pin:
                    chance -= 1
                    if chance == 0:
                        print("You have reached the maximum limit")
                        break
                    else:
                        print(f"Entered pin is incorrect. {chance} attempt(s) left.")
                        continue
                print(account["history"])

            elif user == "5":
                print("Enjoy your day, Visit again!")
                break

            else:
                print("Invalid Option, Please Try again.")
        except ValueError:
            print("Please Enter valid amount")


def load_account():
    with open("data.json", "r") as f:
        return json.load(f)

def save_account(account):
    with open("data.json", "w") as f:
        json.dump(account, f, indent=4)

def create_account():
    name = input("Enter your name:")
    pin = input ("Enter your pin: ")
    return name,pin

def deposit():
    amount = int(input("Enter your amount to be deposited: "))
    a_pin = input("Enter your pin: ")
    return amount,a_pin

def withdraw():
    w_amount = int(input("Enter you amount to withdraw: "))
    a_pin = input("Enter your pin: ")
    return w_amount,a_pin


if __name__ == "__main__":
    main()

