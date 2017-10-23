import platform
import subprocess


def get_list_of_env_vars_based_on_os():
    """ This function detects which OS is running and based on that reads all env variables """
    cmd = ''
    if platform.system() == 'Windows':
        print('Running Windows', platform.release())
        cmd = 'SET'
    elif platform.system() == 'Linux':
        print('Running Linux', platform.release())
        cmd = 'printenv'
    else:
        print('Running some other OS:', platform.system())

    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.readlines()


def print_all_env_vars():
    list_of_env_vars = get_list_of_env_vars_based_on_os()
    for line in list_of_env_vars:
        print(line.decode('utf-8'))

# print_all_env_vars()


def find_env_var(candidate):
    list_of_env_vars = get_list_of_env_vars_based_on_os()
    found = False
    for line in list_of_env_vars:
        var_name = line.decode('utf-8')[0:line.decode('utf-8').index('=')]
        if var_name == candidate:
            found = True
            print(line.decode('utf-8'))
    if not found:
        print('Environmental variable \'', candidate, '\' not found...')

# find_env_var('Path') # 'Path' on Windows & 'PATH' on Linux


def convert_list_into_dict_env_variables():
    dict_of_env_vars = {}
    list_of_env_vars = get_list_of_env_vars_based_on_os()
    for line in list_of_env_vars:
        line_as_list = line.decode('utf-8').split('=')
        if len(line_as_list) == 2:
            key = line_as_list[0]
            value = line_as_list[1].split('\r\n')[0] # discarding '\r\n'
            dict_of_env_vars[key] = value
    return dict_of_env_vars

print(convert_list_into_dict_env_variables())