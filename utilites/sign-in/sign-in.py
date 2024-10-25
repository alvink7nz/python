import tkinter as tk

def getPasswords():
    with open("c:/Users/alvin/code/python/utilites/sign-in/passwords.txt", 'r') as passwordText:
        basepasswords = passwordText.read()
        basepasswords = basepasswords.split(",")
        passwords = {}
        
        for password in basepasswords:
            password = password.split(": ")
            
            # Check if the split results in exactly 2 items (key and value)
            if len(password) == 2:
                passwords[password[0]] = password[1]
            else:
                # Optionally handle malformed entries here
                print(f"Skipping malformed entry: {password}")

passwords = getPasswords()

def writePasswords(passwords):
    with open("c:/Users/alvin/code/python/utilites/sign-in/passwords.txt", 'w') as text:
        text.write(passwords)

def checkPassword(baseusername:tk.Entry, basepassword:tk.Entry):
    username = baseusername.get()
    password = basepassword.get()
    for user in passwords:
        if user == str(username):
            if passwords[user] == str(password):
                writePasswords(passwords)
                root.destroy()
            else:
                wrongLabel = tk.Label(root, text="Wrong username or password!", background="red", font=("Comic Sans MS", 30))
                wrongLabel.pack()
        else:
            try:
                wrongLabel = tk.Label(root, text="Wrong username or password!", background="red", font=("Comic Sans MS", 30))
                wrongLabel.pack()
            except:
                pass

def createPassword(baseusername:tk.Entry, basepassword:tk.Entry):
    username = baseusername.get()
    password = basepassword.get()
    passwords[username] = password
            
root = tk.Tk()

usernameLabel = tk.Label(root, text="Username: ", font=("Comic Sans MS", 30))
usernameEntry = tk.Entry(root, width=20, font=("Comic Sans MS", 30))
passwordLabel = tk.Label(root, text="Password: ", font=("Comic Sans MS", 30))
passwordEntry = tk.Entry(root, width=20, font=("Comic Sans MS", 30))
submit = tk.Button(root, text="Submit", command=lambda: checkPassword(usernameEntry, passwordEntry), font=("Comic Sans MS", 20))
change = tk.Label(root, text="Create new account", font=("Comic Sams MS", 30))
createUsernameLabel = tk.Label(root, text="Username: ", font=("Comic Sans MS", 30))
createUsernameEntry = tk.Entry(root, width=20, font=("Comic Sans MS", 30))
createPasswordLabel = tk.Label(root, text="Password: ", font=("Comic Sans MS", 30))
createPasswordEntry = tk.Entry(root, width=20, font=("Comic Sans MS", 30))
submitNew = tk.Button(root, text="Submit new username and password", command=lambda: createPassword(createUsernameEntry, createPasswordEntry))
usernameLabel.pack()
usernameEntry.pack()
passwordLabel.pack()
passwordEntry.pack()
submit.pack()
change.pack()
createUsernameLabel.pack()
createUsernameEntry.pack()
createPasswordLabel.pack()
createPasswordEntry.pack()
submitNew.pack()

root.mainloop()