number = np.random.randint(1,100)    # загадали число
n_min = 1
n_max = 100
count = 0
while True:        # более компактный вариант счетчика
    predict = (n_min+n_max)//2 # предполагаемое число
    count +=1
    if number == predict: break    # выход из цикла, если угадали
    elif number > predict: 
        n_min = predict+1
    elif number < predict: 
        n_max = predict-1
               
print (f"Вы угадали число {number} за {count} попыток.")