"""
    This script creates SSH connection to the remote server, executes shell command and prints to the console.
    From command line run the python command followed by filename, hostname, port, username and password
"""
import paramiko
import sys


def validate_user_input(args):
    """ This function validates user input """
    if len(args) != 4:
        print('The number of command line arguments must be 4 (hostname, port, username, password)...')
        return False
    else:
        return True


def ssh_connect_and_exec_command(args):
    """ This function creates SSH connection to the remote server and executes shell command """
    if validate_user_input(args):
        hostname, port, username, password = args[0], int(args[1]), args[2], args[3]
    else:
        sys.exit('There was a problem validating the command line arguments...')

    try:
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        # the next line is needed because the public hostname might take extra time to resolve new IP
        # otherwise the SSHException('Server %r not found in known_hosts' % hostname) will be thrown.
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, port, username, password)
        stdin, stdout, stderr = ssh.exec_command('ls -la /var/log')
        print(stdout.read().decode('utf-8'))
        ssh.close()
    except:
        sys.exit('There was a problem establishing SSH connection to the remote server...')


ssh_connect_and_exec_command(sys.argv[1:])
