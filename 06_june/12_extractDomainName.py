'''
Write a function that when given a URL as a string, parses out just the domain name 
and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
'''
import re

def domain_name(domain):
	newstring = domain.replace('http://', '').replace('https://', '').replace('www.', '')
	return newstring.partition('.com')[0]

print domain_name("http://github.com/carbonfive/raygun") == "github" 
print domain_name("http://www.zombie-bites.com") == "zombie-bites"
print domain_name("https://www.cnet.com") == "cnet"

'''
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]

import re
def domain_name(url):
    return re.findall(".*[\.\/](.*)\.", url)[0]
'''