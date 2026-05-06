import pyperclip
password={
    'snap':'abc@123',
    'insta':'efg@123',
    'gmail':'ghi@123',
    }
account=input('enter the account name')
if account in pasword:
    pyperclip.copy(password[account])
    print('password copied to clipboard')

else:
    print('password not found')
