import os

username = os.environ.get('USERNAME')
print(f"buenos dias señor {username}")

for i in [1,2,3]:
    print (f"{username} " * i )