"""
    This script creates SSH connection to the remote server, executes the shell command
    and prints the standard output to the console.
    In order to execute the script, cd into the folder where it is located (pylessons),
    run the python command followed by filename, hostname, port, username and password:
        e.g. 'python urok5_ssh_connection.py <hostname> 22 <username> <password>'
"""
import sys
import paramiko


def validate_user_input(args):
    """ This function validates user input """
    if len(args) != 4:
        print('The number of command line arguments must be 4: hostname, port, username, password!')
        return False
    return True


def ssh_connect_and_exec_command(args):
    """ This function creates SSH connection to the remote server and executes shell command """
    if validate_user_input(args):
        hostname, port, username, password = args[0], int(args[1]), args[2], args[3]
    else:
        sys.exit('There was a problem validating the command line arguments...')
    standard_console_output = ''
    try:
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        # the next line is needed because public hostname might take extra time to resolve new IP
        # otherwise SSHException('Server %r not found in known_hosts' % hostname) will be thrown.
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname, port, username, password)
        stdin, stdout, stderr = ssh.exec_command('df -k')
        standard_console_output = stdout.read().decode('utf-8')
        ssh.close()
    except (Exception) as e:
        print(e)
        sys.exit('There was a problem establishing SSH connection to the remote server...')
    return standard_console_output


print(ssh_connect_and_exec_command(sys.argv[1:]))
