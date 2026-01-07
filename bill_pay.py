import random

print("***********************************")
print("Bill Payment Chooser")
print("***********************************")

pay = input("Enter the names of friends separated by comma (,): ")

pay_list = [name.strip() for name in pay.split(",") if name.strip()]

if not pay_list:
    print("No valid names entered!")
else:
    payer = random.choice(pay_list)
    print("\n🎉 Bill will be paid by:", payer)
