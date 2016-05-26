import os
import requests
import sqlite3

def populate():
    url = 'https://api.clicky.com/api/stats/4?site_id=100716069&sitekey=93c104e29de28bd9&type=visitors-list'
    date = '&date=2016-05-26'
    limit = '&limit=all'
    output = '&output=json'
    # nyu = '&ip_address=59.79.127.0,59.79.127.255|91.230.41.0,91.230.41.255|94.56.130.144,94.56.130.159|94.56.170.16,94.56.170.31|94.200.220.160,94.200.220.191|101.231.120.128,101.231.120.159|103.242.128.0,103.242.131.255|128.122.0.0,128.122.255.255|128.238.0.0,128.238.255.255|176.74.48.32,176.74.48.63|180.169.77.32,180.169.77.63|192.76.177.0,192.76.177.255|192.86.139.0,192.86.139.255|192.114.110.0,192.114.110.255|193.175.54.0,193.175.54.255|193.205.158.0,193.205.158.128|193.206.104.0,193.206.104.255|194.214.81.0,194.214.81.255|195.113.94.0,195.113.94.255|195.229.110.0,195.229.110.191|198.71.44.128,198.71.44.191|202.66.2.16,202.66.2.31|202.66.60.160,202.66.60.191|203.174.165.128,203.174.165.255|212.219.93.0,212.219.93.255|213.42.147.0,213.42.147.63|216.165.0.0,216.165.127.255'
    r = requests.get(url+date+limit+output)
    # print(url+date+limit+output+nyu)
    data = r.json()
    # html = []
    for item in data[0]['dates'][0]['items']:
        si = item["session_id"]
        ip = item["ip_address"]
        org = item["organization"]
        add_entry(si,ip,org)

def add_entry(si,ip,org):
    entry = Analytics.objects.get_or_create(si=si,ip=ip,org=org)[0]
    return entry

# if __name__ == '__main__':
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'A1.settings')
print "Starting population script..."
from models import Analytics
populate()

        # html.append("<tr><td>%s</td><td>IP_Address</td><td>%s</td><td>Session_ID</td><td>%s</td></tr>" %(org, ip, si))
        # conn = sqlite3.connect("/Users/arifshaikh/JomiAnalytics/pythonsqlite.db")
        # cursor = conn.cursor()
        # cursor.execute("""CREATE TABLE IF NOT EXISTS xjomi
        #                       (org text, ip text, si text)
        #                    """)
        # varhtml = []
        # varhtml = [(org, ip, si)]
        # cursor.executemany("INSERT INTO xjomi VALUES (?,?,?)", varhtml)
        # conn.commit()
    # return HttpResponse('<table>%s</table>' % '\n'.join(html))



#
# def populate():
#     python_cat = add_cat('Python')
#
#     add_page(cat=python_cat,
#         title="Official Python Tutorial",
#         url="http://docs.python.org/2/tutorial/")
#
#     add_page(cat=python_cat,
#         title="How to Think like a Computer Scientist",
#         url="http://www.greenteapress.com/thinkpython/")
#
#     add_page(cat=python_cat,
#         title="Learn Python in 10 Minutes",
#         url="http://www.korokithakis.net/tutorials/python/")
#
#     django_cat = add_cat("Django")
#
#     add_page(cat=django_cat,
#         title="Official Django Tutorial",
#         url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")
#
#     add_page(cat=django_cat,
#         title="Django Rocks",
#         url="http://www.djangorocks.com/")
#
#     add_page(cat=django_cat,
#         title="How to Tango with Django",
#         url="http://www.tangowithdjango.com/")
#
#     frame_cat = add_cat("Other Frameworks")
#
#     add_page(cat=frame_cat,
#         title="Bottle",
#         url="http://bottlepy.org/docs/dev/")
#
#     add_page(cat=frame_cat,
#         title="Flask",
#         url="http://flask.pocoo.org")
#
#     # Print out what we have added to the user.
#     for c in Category.objects.all():
#         for p in Page.objects.filter(category=c):
#             print "- {0} - {1}".format(str(c), str(p))
#
# def add_page(cat, title, url, views=0):
#     p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
#     return p
#
# def add_cat(name):
#     c = Category.objects.get_or_create(name=name)[0]
#     return c

# Start execution here!
