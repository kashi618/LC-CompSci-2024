def sameString(stringA,stringB):
    # Compares stringA and stringB
    if (stringA == stringB):
        return "They are the Same"
    else:
        return "No"

# Uses sameString function to compare two user inputs
print(sameString(input("Enter String A: "), input("Enter String B: ")))