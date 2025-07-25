email=input("Enter your Email:")
index=email.index("@")
username=email[:index]
domain=email[index:]
print(f"your email is {username} and domain is {domain}")