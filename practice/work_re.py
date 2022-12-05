import re
import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context
auto_nums = urllib.request.urlopen("https://msk.spravker.ru/avtoservisy-avtotehcentry/").read().decode()

pattern =
match = re.findall(pattern, auto_nums)
print(match)