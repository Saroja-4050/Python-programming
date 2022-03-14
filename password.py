print('LIMITED ACCESS ONLY')
print('Enter the user name:')
name=input()
print('Enter the password:')
password=input()
if name == 'saroja':
    print('Hello saroja')
    if password =='bluepen':
        print('Access granted')
    else:
        print('Access denied, wrong password')
elif name  != 'saroja':
    print('Invalid Username')
