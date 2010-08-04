from pycloudapp.cloud import Cloud
import re

mycloud = Cloud()
mycloud.auth('lego399@gmail.com', 'CdE33345tG')

txt=mycloud.list_items(page=1, per_page=1)
print txt
x = str(txt)

re1='.*?'       # Non-greedy match on filler
re2='(http)'    # Word 1
re3='(:)'       # Any Single Character 1
re4='(\\/)'     # Any Single Character 2
re5='((?:\\/[\\w\\.\\-]+)+)'    # Unix Path 1
rg = re.compile(re1+re2+re3+re4+re5,re.IGNORECASE|re.DOTALL)
m = rg.search(x)
if m:
	word1=m.group(1)
	c1=m.group(2)
	c2=m.group(3)
	unixpath1=m.group(4)
	url = word1+c1+c2+unixpath1
	print url
