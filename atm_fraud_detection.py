import random
import time

# Simulated user database
users = {
    "1234567890": {
        "pin": "1234",
        "balance": 5000,
        "phone": "+491234567890"
    }
}

# OTP generator
def generate_otp():
    return random.randint(100000, 999999)

# Fraud detection logic
def fraud_check(amount):
    if amount > 2000:
        print("\n⚠ Suspicious transaction detected.")
        return True
    return False

# OTP verification
def verify_otp(phone):
    otp = generate_otp()
   # Simulated OTP delivery (in real systems this would be sent via SMS)
    print(f"\nOTP sent to {phone}: {otp}")
    entered = input("Enter OTP: ")

    if entered == str(otp):
        return True
    else:
        return False

# ATM workflow
def atm_session(card):
    user = users.get(card)

    if not user:
        print("Invalid card.")
        return

    pin = input("Enter PIN: ")

    if pin != user["pin"]:
        print("Incorrect PIN.")
        return

    print("\nLogin successful.")
    print("\nSelect an option:")
    print("1 - Withdraw Money")
    print("2 - Check Balance")
    choice = input("Enter option number (1 or 2): ")

    if choice == "1":
        amount = int(input("Enter withdrawal amount: "))

        if fraud_check(amount):
            print("OTP verification required.")

            if verify_otp(user["phone"]):
                print("OTP verified.")
            else:
                print("OTP verification failed. Transaction blocked.")
                return

        if amount <= user["balance"]:
            user["balance"] -= amount
            print(f"Transaction successful. Remaining balance: {user['balance']}")
        else:
            print("Insufficient balance.")

    elif choice == "2":
        print(f"Available balance: {user['balance']}")

    else:
        print("Invalid option.")

def main():
    print("ATM Fraud Detection System")

    card = input("Insert card number: ")
    atm_session(card)

if __name__ == "__main__":
    main()