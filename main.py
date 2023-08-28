# write your code here
favorite_animals = ['cat','dog','monkey','rabbit']
print(favorite_animals)
print(f'the secound element in the list is {favorite_animals[1]}')
favorite_animals.remove('monkey') # ['cat','dog','rabbit']
print(favorite_animals)
favorite_animals.append('lion') 
for animal in favorite_animals:
    print(animal) 
new_numbers = [1,2,3,4,5]
numbers_sum = 0