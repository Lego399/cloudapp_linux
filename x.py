
import re

txt='[{u\&apos;name\&apos;: u\&apos;20_21_21_04-08-2010.png\&apos;, u\&apos;url\&apos;: u\&apos;http://cl.ly/1sUC\&apos;, u\&apos;owner_id\&apos;: 45450, u\&apos;created_at\&apos;: u\&apos;2010-08-04T18:21:34Z\&apos;, u\&apos;public_slug\&apos;: u\&apos;1sUC\&apos;, u\&apos;updated_at\&apos;: u\&apos;2010-08-04T18:21:34Z\&apos;, u\&apos;content_url\&apos;: u\&apos;http://cl.ly/1sUC/content\&apos;, u\&apos;item_type\&apos;: u\&apos;image\&apos;, u\&apos;view_counter\&apos;: 0, u\&apos;href\&apos;: u\&apos;http://my.cl.ly/items/944950\&apos;, u\&apos;private\&apos;: False, u\&apos;redirect_url\&apos;: None, u\&apos;private_slug\&apos;: None, u\&apos;deleted_at\&apos;: None, u\&apos;id\&apos;: 944950, u\&apos;remote_url\&apos;: u\&apos;http://f.cl.ly/items/f94a16539b3a1b6b5046/20_21_21_04-08-2010.png\&apos;, u\&apos;icon\&apos;: u\&apos;http://my.cl.ly/images/item_types/image.png\&apos;}] '

re1='.*?'	# Non-greedy match on filler
re2='(http)'	# Word 1
re3='(:)'	# Any Single Character 1
re4='(\\/)'	# Any Single Character 2
re5='((?:\\/[\\w\\.\\-]+)+)'	# Unix Path 1

rg = re.compile(re1+re2+re3+re4+re5,re.IGNORECASE|re.DOTALL)
m = rg.search(txt)
if m:
    word1=m.group(1)
    c1=m.group(2)
    c2=m.group(3)
    unixpath1=m.group(4)
    url = word1+c1+c2+unixpath1

#-----
# Paste the code into a new python file. Then in Unix:'
# $ python x.py 
#-----
