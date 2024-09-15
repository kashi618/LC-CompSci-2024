# intro sentence
print("Welcome to Temperature Alert System")

# enter the temperature
temperature = int(input("Enter temperature value in degrees Celsius: "))

# too hot
if temperature < 20:
    print("Too cold. Turn up heating.")
    
    # just right
elif temperature > 20 and temperature < 24:
    print("Temperature is juuuuuuuuuust right.")

# too warm
else:
    print("Too warm. Turn down heating.")
    
