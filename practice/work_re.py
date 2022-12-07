import re
import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context
auto_nums = urllib.request.urlopen("https://moskva1.jsprav.ru/zamena-vozdushnogo-filtra/").read().decode()

pattern = r'(?:class="company-info-name-org">)([^<]*)(?:[\w|\W]+?data-rating=")([^"]+)(?:[\w|\W]*?"company-info-address-full company-info-text">\s*)([^\n]*)(?:[\w|\W]*?data-phone=")([^"]*)'
match = re.findall(pattern, auto_nums)
print(match)










# ssl._create_default_https_context = ssl._create_unverified_context
# auto_nums = urllib.request.urlopen("https://msk.spravker.ru/avtoservisy-avtotehcentry/").read().decode()
#
# pattern = r'(?:class=\"org-widget\-header__title-link\">[^\w]*|<span class=\"org-widget\-header__meta ' \
#            r'org-widget\-header__meta\--location\">[^\w]*|<dt class=\"spec__index\"><span ' \
#            r'class=\"spec__index-inner\">Телефон</span></dt>\n*\s*<dd class=\"spec__value\">[^\w]*|<dt ' \
#            r'class=\"spec__index\"><span class=\"spec__index-inner\">Часы работы</span></dt>\n*\s*<dd ' \
#            r'class=\"spec__value\"[^\w]*>|<p>[^\w]*)([^<]*\b) '
#
# match = re.findall(pattern, auto_nums)
# match = [match[i:i+4] for i in range(0, len(match), 4)]
# print(match)


















