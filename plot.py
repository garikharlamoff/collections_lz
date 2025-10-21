#Импорт библиотек
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-20,20,500) #Заданный размер
y = np.cos(x**2)      #Триганометрическая функция
plt.plot(x, y)  #Соединение точек
plt.show() #Вывод графика
