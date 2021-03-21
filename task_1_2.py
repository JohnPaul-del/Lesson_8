import re

res_str = re.compile(r'^(.+)\s-\s-.*\[(.+)].*\"([A-Z]+)\s+(/.+?)\s.*?"\s(\d+)\s(\d+)')
with open("nginx_log.txt", "r", encoding="utf-8") as f:
    for strings in f:
        print(re.findall(res_str, strings))
