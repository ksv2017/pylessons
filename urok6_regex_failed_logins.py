"""
    This script creates SSH connection to the remote server, reads from
    /var/log/secure and finds failed attempts to login, by using regex;
    the results are printed as a table: [datetime, username, ip, port].
"""
import re
from urok5_ssh_connection import *


def ssh_and_get_stdout_list(args):
    """ Uses ssh_connect_and_exec_command() from lesson 5 """
    stdout_str = ssh_connect_and_exec_command(args)
    return stdout_str.split('\n')


def get_matches_from_stdout_list(stdout_list):
    """ Uses regex to find matches from stdout """
    regex = "^(.*?)\s\w+\ssshd.*?:\sFailed\spassword\s.*?user\s(\w+)\sfrom\s(.*?)\sport\s(\d+)\s.*$"
    matches_list_of_tuples = []
    for row in stdout_list:
        if not (row == '') and re.search(regex, row):
            match = re.search(regex, row)
            match_tuple = match.groups()
            matches_list_of_tuples.append(match_tuple)
    return matches_list_of_tuples


if __name__ == "__main__":
    stdout_list = ssh_and_get_stdout_list(sys.argv[1:])
    matches_from_stdout = get_matches_from_stdout_list(stdout_list)
    for row in matches_from_stdout:
        print(row[0], '\t', row[1], '\t', row[2], ':', row[3])
        # Oct 25 21:46:06 	 admin 	 89.234.157.254 : 42807
