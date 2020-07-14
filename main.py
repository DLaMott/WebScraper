from general import *
from domain_name import *
from ip_address import *
from nmap import *
from robots_txt import *
from whois import *

#Created by GothamsJoker
#This is a scanner to find a site's domain, host name, IP, Whois, Nmap, and robot.txt.
#Users must have whois and nmap installed on their system.
#Ip address is found with host name EX:www.***.com
#Other functions find information via full URL.
#Refer to 'gather_info' inorder to properly place website identification.

#Creates a new directory called companies.
ROOT_DIR = 'companies'
create_dir(ROOT_DIR)

def gather_info(name, url, host):
    #Variables for performing data retrieval
    domain_name = get_domain_name(url)
    ip_address = get_ip_address(host)
    nmap = get_nmap('-F', ip_address)
    robots_txt = get_robots_txt(url)
    whois = get_whois(domain_name)
    create_report(name, url, domain_name, nmap, robots_txt, whois)

def create_report(name, full_url, domain_name, nmap, robots_txt, whois):
    project_dir = ROOT_DIR + '/' + name
    create_dir(project_dir)
    #Finds the full URL and places it in a file.
    write_file(project_dir + 'full_url.txt', full_url)
    #Finds the domain name and places it in a file.
    write_file(project_dir + 'domain_name.txt', domain_name)
    #Deploys nmap on intended website.
    write_file(project_dir + 'nmap.txt', nmap)
    #Searches for robot.txt file for website.
    write_file(project_dir + 'robots_txt.txt', robots_txt)
    #Performs whois on intended website.
    write_file(project_dir + 'whois.txt', whois)

#Gather info creates the name for it on the directory, URL for your intended website, Hostname for your intended website.
gather_info('www.reddit.com', 'http://reddit.com/', 'www.reddit.com')