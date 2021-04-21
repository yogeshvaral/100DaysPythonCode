

try:
    file = open("abc.txt")
    a_dictionary = {"key":"Value"}
    print(a_dictionary["key11"])
except FileNotFoundError:
    file = open("abc.txt", 'w')
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exists")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")