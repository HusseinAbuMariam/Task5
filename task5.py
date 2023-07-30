name = input("your name is :")
age = input("your age is :")
street = input("street is :")
city = input("city is :")
country = input("country is :")
print(f"\"Name: {name}\""+f"\n\"Age: {age}\""+f"\n\"Address: {street}, {city}, {country}\"")
print(f"\"Hello {name} your age is {int(age)-5} years Old, Your Address is {street}, {city}, {country}.\"")
print(type(name), type(age))
print(type(street), type(city))
print(type(country))
print(f"\"Hello \'{name}\', How Are You?  \  \"\"\"  Your Age Is \"{int(age)-5}\"\" + And Your Country Is: {country}")
print(f"""\"Hello \'{name}\', How Are You?  \ 
\"\"\"  Your Age Is \"{int(age)-5}\"\" + And
 Your City Is: {city}""")
name ='Doaa Reem'
print("First Letter Is "+"\""+name[0]+"\"")
print("Third Letter Is "+"\""+name[2]+"\"")
print("Last Letter Is  "+"\""+name[-1]+"\"")
print(name[-3:])
print(name[0:4])
name2 = name.replace("a","A",1)
print(name2[2:7])
print(name[-1:-5:-1])
print(name[:4:2]+name[4:7])
name = "$&$&Mohammed$&$&"
print(name.strip("$&"))
msg = "I %7 Python And Although I %7 GSG with Zakaria"
print(msg.replace("%7","Love",2))
# Bonus
title="gaza sky geeks "
print(title.title())
print(title.capitalize())
# The difference between them is that the title capitalizes each letter at the beginning of each word
# Either capitalize it enlarges the first letter in the first word only As shown in the example.
num1 = "4"
num2 = "56"
num3 = "963"
num4 = "385"
num5 = "8719"
num6 = "87190"
print(f"{0:04d}"+num1)
print(f"{0:03d}"+num2)
print(f"{0:02d}"+num3)
print(f"{0:02d}"+num4)
print(num5)
print(num6)
first_name = "Hadeel"
print("***********"+first_name)
print("***********"+first_name+"***********")
print(first_name+"***********")
name_one = "HaLA"
name_two = "shaHD"
print(name_one.swapcase())
print(name_two.swapcase())
print(name_one.lower())
print(name_two.upper())
#Check if name_one contains Only Upper Case letters
print(name_one.isupper())
#Check if  name_two contains Only Lower Case letters?
print(name_two.islower())
print(name_one.startswith("S"))
print(name_two.endswith("HD"))
msg = "I Love Python And Although I Love GSG with Zakaria"
print("Number of <Love> is:",msg.count('Love'))
print("Number of <t> is:",msg.count('t'))
name = "Zakaria"
print(name.find("r"))
msg = "I %7 Python And Although I %7 GSG with Zakaria"
print(msg.replace("%7","Love",1))



