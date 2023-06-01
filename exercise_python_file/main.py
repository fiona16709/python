user_input = input("Please insert the context.")

file_object = open('./data.txt','w')
file_object.write(user_input)

file_object.close()