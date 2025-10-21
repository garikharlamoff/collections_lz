f=0
x=1
y=1
k=0
n=int(input('Введите количество элементов для списка:'))
a=[]
for i in range(0,n):
    a.append(f)
    y=y+x
    x=y-x
    f=x-f
print(a)
for i in range(0,n):
    if a[i]%2==0:
        a[i]*=2
for i in range(0,n):
    if a[i]%2==1:
        a[i]**=2
print(a)
for i in range(0,n):
    if a[i]>sum(a)/n:
        k+=1
print("Минимальный элемент:",min(a),'\nМаксимальный элемент:',max(a),'\nДлина списка:',n,"\nКоличество элементов больше медианного значения:",k)
