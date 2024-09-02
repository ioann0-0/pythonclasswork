data = {
    'apple': 50,
    'banana': 20,
    'orange': 30,
    'mango': 40,
}
datac= dict(sorted(data.items(),key=lambda item: item[1]))
dataca= dict(sorted(data.items(),key=lambda item: item[1],reverse=True))

print("сортировкая по возрастанию",datac)
print('сортировка по убыванию',dataca)
