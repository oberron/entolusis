# list categories in category folder

from os import walk
from os.path import abspath,join, pardir

categories_folder = abspath(join(__file__,pardir,pardir,"category"))
post_folder = abspath(join(__file__,pardir,pardir,"_posts"))

site_categories = []
for root,directories,files in walk(categories_folder):
    for f in files:
        site_categories.append(f.split(".md")[0])
        
site_categories = set(site_categories)
        
for root,directories,files in walk(post_folder):
    for f in files:
        with open(join(root,f),'r',encoding="utf-8") as fi:
            lines = fi.readlines()
            for l in lines:
                if l.find("categories")==0:
                    categories = l.split(":")[1]
                    for c in [" ","[","]","\n"]:
                        categories = categories.replace(c,"")
                    categories=categories.split(",")
                    if len(set(categories)-site_categories)>0:
                        print(f,set(categories)-site_categories)
                    break
print("done")