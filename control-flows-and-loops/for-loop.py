fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

vegetables = ['tomato','potato','brinjal']
for vegetable in vegetables:
    if vegetable == 'tomato':
        print(vegetable)
        continue
    elif vegetable == 'potato':
        print('potato has starch')
        break

# range

table_of_5 = {i:i*5 for i in range(5)}
print(table_of_5)