friends = ["Haryx" , "Punith" , "Guru Kiran" , "Pavan" , "Sangeetha" , "Hansika"]

import random 

# 1st option - To use random.choice()
# print(random.choice(friends))

# 2nd option - To use random.randint()
random_index= random.randint(0 , len(friends)-1)
print(friends[random_index])