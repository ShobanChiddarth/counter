import os, pickle
# All the numbers are steps of '### Programming Logic used' in 'README.md'

file=os.path.join(os.getcwd(), 'counterfile.bin') # The link to binary file where value is stored

if os.path.exists(file): # 1
    counterfile=open(file, 'rb')
    count=pickle.load(counterfile)
else: # 2
    count=0
    counterfile=open(file, 'wb')
    pickle.dump(count, counterfile)

counterfile.close() # 3
count+=1 # 4
counterfile=open(counterfile.name, mode='rb+') # 5


# 6
pickle.dump(count, counterfile)

counterfile.close() # 7

# 8
print('This file counts number of times it was run')
print('count =', count, end='') # `end` is simply useless
input() # Just to freeze the file so that it doesn't close when opened