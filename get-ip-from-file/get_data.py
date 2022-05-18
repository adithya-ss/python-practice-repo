import re


with open('details.txt', 'r') as read_file:
    for data in read_file:
        if len(data.rstrip()) > 0:
            regex_pattern = "^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$"
            ip_data = data.rstrip().split("=")[1]
            check_ip_data = bool(re.match(regex_pattern, ip_data))
            if (check_ip_data):
                print(ip_data)
            else:
                pass
        else:
            pass