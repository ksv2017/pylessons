""" This module prints ten most frequent unique IPs from logs file """
import re


def get_all_ips_addresses_from_logfile(logfile):
    """ Uses regex to find all IPs (non-unique) in a logfile """
    with open(logfile) as f:
        lines = f.readlines()
    # Oct 29 06:25:28 haproxy-a haproxy[3561]: IP:PORT ******
    regex = "^(.*?)\shaproxy-a\shaproxy.*:\s(.*?):(.*?)\s.*$"
    matches_list_of_tuples = []
    for row in lines:
        if re.search(regex, row):
            match = re.search(regex, row)
            match_tuple = match.groups()
            matches_list_of_tuples.append(match_tuple)
    # print(matches_list_of_tuples[0]) => ('Oct 29 06:25:28', 'IP', 'PORT')
    return matches_list_of_tuples


def extract_unique_ip_addresses(processed_logs):
    """ Returns a dict of unique IP addresses from processed logs """
    dict_unique_ips_times = {}
    for _ in processed_logs:
        if _[1] not in dict_unique_ips_times.keys():
            dict_unique_ips_times[_[1]] = 1
        else:
            dict_unique_ips_times[_[1]] += 1
    return dict_unique_ips_times


def sort_ip_addresses_by_times_desc(dict_ips_times):
    """ This function sorts dict in a descending order, returns a list """
    return sorted(dict_ips_times.items(), key=lambda x: x[1], reverse=True)


if __name__ == "__main__":
    rows = get_all_ips_addresses_from_logfile('haproxy.log')
    dict_ips_times = extract_unique_ip_addresses(rows)
    print('Total number of unique IP addresses is:', len(dict_ips_times))
    list_sorted = sort_ip_addresses_by_times_desc(dict_ips_times)
    for item in list_sorted[:10]:
        print('IP address %16s : %6d occurrences' % (item[0], item[1]))
