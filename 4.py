print("введите количество лет")
y=int(input())
e=(y*365*8*60)//5
print("просмотрено экспонатов:",e)

print("введите количество экспонатов")
e1=int(input())
m=e1*5
d=m//(8*60)
print("years=",(d//365))
print("days=",d)
print("minutes=",m%(8*60))
