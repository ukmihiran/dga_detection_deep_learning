# import os
# import csv

# import pandas as pd

# header = ['URL', 'STATUS', 'DGA', 'DGA_Class', 'Comment']
# save_file = r'data.csv'
# if not os.path.exists(save_file):
#     with open(save_file, 'w', encoding='UTF8') as f:
#         writer = csv.writer(f)
#         writer.writerow(header)
# else:
#     data_file = pd.read_csv(save_file)
#     print(data_file)


# URL = "lsklsa"
# STATUS = "lsklsa"
# DGA = "lsklsa"
# DGA_Class = "lsklsa"
# Comment = "lsklsa"

# with open(save_file, 'w', encoding='UTF8') as f:
#     writer = csv.writer(f)
#     writer.writerow(header)
from urllib.parse import urlparse
url = "https://scikit-learn.org/stable/install.html"
url = "www.facebook.com"
print(url[:4])

first_part = url[:4]
last_part = url[-3:]

print(last_part)
if first_part == "http":
    domain = urlparse(url).netloc
    print(domain)
elif first_part == "www.":
    domain = url[4:]
    print(domain)
else:
    pass



