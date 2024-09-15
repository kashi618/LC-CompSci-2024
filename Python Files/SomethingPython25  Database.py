
userList = []
userName = input("Enter your name: ")
userList.append(userName)
userAge = int(input("What age are you "+ userName+ "? " ))
userList.append(userAge)
userCity = input("What is your CUERRERRENNT CICITITIYYY LIVIVVNGGG? ")
userList.append(userCity)
userCountry = input("What is your country of birth? ")
userList.append(userCountry)



print("My data base for "+userName+"\n"+str(userList))

userList.reverse()
print(userList)