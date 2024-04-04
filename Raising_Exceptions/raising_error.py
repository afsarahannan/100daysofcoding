# try and except is used in the case when you want to try out a code but know that the code might return an error.
# In such a case the except keyword is used to catch a very specific error message such as a FileNotFoundError or a KeyError
# And in the case when the try method has not returned any error and everything is running smoothly then the code moves to the
# else statement
# the finally will run no matter what happens
# try:
#     file = open("data.txt")
#     dict = {'key':'value'}
#     print(dict["key"])
# except FileNotFoundError:
#     file = open("data.txt", "w")
#     file.write("This is a test statement")
# except KeyError as error_message:
#     print(f"The {error_message} could not be found.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("The file was closed.")

#knowing when to raise an error

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height cannot be greater than 3 meters. Unless you sir are a Sasquatch.")

bmi = weight / height ** 2
print(bmi)