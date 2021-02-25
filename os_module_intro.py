import os
#print(dir(os))

#print(os.getcwd())
#os.rmdir("made with os")
#os.chdir("..")
#os.mkdir("made with os")
#print(os.listdir(os.getcwd()))
#print(os.stat("calculator.py"))
'''
for dir_path, dir_name, files in os.walk(os.getcwd()):
    print(dir_path)
    print(dir_name)
    print(files)
'''
#print(os.environ.get("PATH").split(";"))

path_to_new_test = os.path.join(os.getcwd(), "new_test.py")
#print(path_to_new_test)

#print(os.path.exists("calculator.py"))

#print(os.path.isfile("calculator.py"))

print(os.path.splitext(path_to_new_test))
