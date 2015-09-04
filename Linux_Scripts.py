#!/usr/bin/env python
import sys
import os
import subprocess

def find_files():
    """
    Linux Find in Python
    find_files.py path_to_start_search filename_to_search_for
    """
    arguments = sys.argv
    path = arguments[1]
    pattern = arguments[2]

    files = walk_dirs(path)[0]
    dirs = walk_dirs(path)[1]

    for file in files:
        if pattern in file:
            print file

def walk_dirs(dir_name):
    """ Walk all dirs recursively and return all files, dirs with their full path """
    file_list = []
    dir_list = []

    for root, dirs, files in os.walk(dir_name):
        for item in files:
            file_list.append(os.path.join(root, item))
        for item in dirs:
            dir_list.append(os.path.join(root, item))

    return file_list, dir_list


def copy_files(source, destination):
    """ Copy source to destionation, if destination doesn't exist, it is created """
    with open(source, 'r') as file_object:
        text = file_object.read()
        file_object.close()

    with open(destination, 'w') as write_object:
        write_object.write(text)
        write_object.close()

    print "Copied %s to %s" % (source, destination)


def zip_files(name_of_zip, array_of_files):
    """Create a ZIP file containing the array of files"""
    for item in array_of_files:
        subprocess.call(['zip', name_of_zip, item])

def grep_search(file, pattern):
    """ Pass file and pattern - if pattern in line, print the line """
    with open(file, 'r') as file_object:
        for line in file_object.readlines():
            if line.find(pattern) != -1:
                print line
                
def dir_usage(path):
    """ Check disk usage of a directory - provide full path"""
    cmd = 'du '
    arg = '-sh '
    os.system(cmd + arg + path)

def check_port(port):
    """ Check if a certain port is open, provide info about processes using it """
    cmd = 'netstat '
    arg = '-apn '
    search = 'grep ' + port
    os.system(cmd + arg + '|' +  search)

def user_add(user_name, action):
    """ Add or delete a Linux User - user, pass, add or delete"""
    add = 'useradd '
    delete = 'userdel '
    if action == 'add':
        os.system(add + user_name)
        print "User %s created." % (user_name)
        print "Switch to %s and execute passwd, to change your password" % (user_name)
    elif action == 'delete':
        os.system(delete + user_name)
        print "User %s deleted" % (user_name)
    else:
        print "Action should be either 'add' or 'delete', not - %s" % (action)
        

def main():
    #copy_files('/home/burizz/Desktop/test.txt', '/home/burizz/Desktop/askldjs.txt')
    #walk_dirs('/home/burizz')
    #find_files()
    #zip_files('test123', ['/home/burizz/Desktop/asd', '/home/burizz/Desktop/askjdh'])
    #grep_search('/home/burizz/Desktop/asd', 'test123')
    #dir_usage('/etc')
    #check_port('631')
    user_add('testing', 'delete')
        
if __name__ == "__main__":
    main()
