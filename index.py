#!/usr/bin/python

#############################################
# @title What Is My IP (Python version)
#
# @author           Pierre-Henry Soria <pierrehs@hotmail.com>
# @copyright        Pierre-Henry Soria, All Rights Reserved.
# @license          General Public License (GPL) 3 or later (http://www.gnu.org/copyleft/gpl.html)
# @version          2.0
#
#############################################

from cgi import escape
from os import environ
from datetime import datetime
from ConfigParser import SafeConfigParser
import urllib2 
import json

INDEX_FILE = "index.tpl"
ip_address = escape(environ["REMOTE_ADDR"])

# Set the HTML type to HTTP header
print("Content-type: text/html")
print("")


# Get the template file 
def tpl_file(tpl_file):
  try:
    file = open('template/' + tpl_file, 'r') 
    return file.read()
  except IOError:
    print("Can't open the tpl file: ", tpl_file)
  finally:
    file.close()


# Get the geographic informations relative to the IP address
def geo_ip(ip_address, what):
	
  url = config.get("api", "geo_ip_url") + ip_address
    
  json_url = urllib2.urlopen(url)
  data = json.load(json_url)
  json_url.close()
    
  if what == 'country_code':
    return data["country_code"]
	  
  if what == 'country':
    return data["country_name"]
	  
  if what == 'city':
    return data["city"]


# Get the URL of Country Flag Icon
def country_flag_url():
  icon = geo_ip(ip_address, 'country_code').lower() + '.gif' # Lower for the flag image
  url_flag = config.get("webapp", "url") + 'static/img/flag/'
  
  try:
    urllib2.urlopen(urllib2.Request(url_flag + icon))
    return url_flag + icon
  except:
    return url_flag + 'none.gif'
     
  
# Get configuration file
try:
  config = SafeConfigParser()
  config.read("config/conf.ini")
except IOError as e_msg:
  print("Can't open the config file: ", e_msg)
	
	
# Template Parsing
html = tpl_file(INDEX_FILE)
html = html.replace("{include_header}", tpl_file('header.inc.tpl'))
html = html.replace("{include_footer}", tpl_file('footer.inc.tpl'))
html = html.replace("{include_map}", tpl_file('map.inc.tpl'))
html = html.replace("{include_analytics}", tpl_file('analytics.inc.tpl'))

html = html.replace("{url}", config.get("webapp", "url"))
html = html.replace("{style_name}", config.get("webapp", "style_name"))
html = html.replace("{site_name}", config.get("general", "site_name"))
html = html.replace("{contact_email}", config.get("general", "contact_email"))
html = html.replace("{api_ip_url}", config.get("api", "ip_url"))
html = html.replace("{map_type}", config.get("map", "type"))
html = html.replace("{map_zoom}", config.get("map", "zoom"))
html = html.replace("{analytics_id}", config.get("api", "analytics_id"))
html = html.replace("{contact_email}", config.get("general", "contact_email"))

html = html.replace("{ip}", ip_address)
html = html.replace("{url_flag}", country_flag_url())
html = html.replace("{country}", geo_ip(ip_address, 'country'))
html = html.replace("{city}", geo_ip(ip_address, 'city'))
html = html.replace("{year_date}", str(datetime.today().year))


# Output
print(html)
