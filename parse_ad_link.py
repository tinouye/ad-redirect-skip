from urllib.parse import unquote

while True:
    input_str = input('Enter link to process: ')
    input_str = unquote(input_str)

    url_start = input_str.find('=http')+1
    url_end = -1

    if input_str.find('amazon', url_start) != -1:
        # dp_idx = input_str.find('dp', url_start)
        # url_end = input_str.find('%', dp_idx+3)
        url_end = input_str.find('?', url_start)-1
    else:
        url_end = input_str.find('&', url_start)

    print(input_str[url_start:url_end])
