import os, re

for i in os.listdir('.'):
    if i.endswith('.m4a'):
        os.rename(i, re.sub(r'  ', ' ', i))
    # os.rename(i, re.sub(r'\(\d{4}\)', '(2009) ({n})'.format(n=n), i))
