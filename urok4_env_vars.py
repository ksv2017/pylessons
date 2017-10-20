import platform
import subprocess
import sys


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


def find_env_var(candidate):
    p = get_list_of_env_vars_based_on_os()
    for line in p.stdout.readlines():
        var_name = line.decode('utf-8')[0:line.decode('utf-8').index('=')]
        if var_name == candidate:
            print(line.decode('utf-8'))


find_env_var('Path') # can be split by ',' into different paths...


# to run from cmd: python urok4_env_vars.py Path
# find_env_var(sys.argv[1])
