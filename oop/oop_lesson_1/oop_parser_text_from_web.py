import re

with open("index2.html", encoding="utf-8") as f:
    s = f.read()

comments = re.compile("<!--.*?-->", re.DOTALL)
scripts = re.compile("<script.*?</script>", re.DOTALL)
tags = re.compile("<[^<]*>")

s = comments.sub("", s)
s = scripts.sub("", s)
s = tags.sub("", s)

s = re.sub("[ ]+", " ", s)
s = re.sub("\s{2,}", "\n", s)

print(s)
