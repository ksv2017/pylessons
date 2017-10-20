import platform
import subprocess


def get_list_of_env_vars_based_on_os():
    """ This script detects which OS is running and based on that reads all env variables """
    cmd = ''
    if platform.system() == 'Windows':
        print('Running Windows', platform.release())
        cmd = 'SET'
    elif platform.system() == 'Linux':
        print('Running Linux', platform.release())
        cmd = 'printenv'
    else:
        print('Running some other OS:', platform.system())

    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


def print_all_env_vars():
    p = get_list_of_env_vars_based_on_os()
    for line in p.stdout.readlines():
        print(line.decode('utf-8'))


print_all_env_vars()


def find_env_var(candidate):
    p = get_list_of_env_vars_based_on_os()
    for line in p.stdout.readlines():
        var_name = line.decode('utf-8')[0:line.decode('utf-8').index('=')]
        if var_name == candidate:
            print(line.decode('utf-8'))

# find_env_var('PATH') # 'Path' on Windows
