print("введите имя")
name=input()
print("введите фамилию")
surname=input()
print("введите год рождения")
year=int(input())

print(name+"_"+surname+"_"+str(year))

x=name
name=surname
surname=x

year+=60
print(name+"_"+surname+"_"+str(year))