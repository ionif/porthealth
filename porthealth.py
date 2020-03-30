import argparse
import requests
from bs4 import BeautifulSoup

"""
find the latest successful build of a port
"""
def findLatestBuild(portname):
	res = requests.get('https://ports.macports.org/port/' + portname)

	#use beautiful soup to parse html
	soup = BeautifulSoup(res.text, 'html.parser')

	#list of version numbers that build successfully
	version_list = []
	#all successful builds link to the build stats so we can search for links
	for link in soup.find_all('a'):
		#target is an attribute, the build badges all have target = "_blank"
		if link.get('target') == "_blank":
			#each link has a name and text, text gives the version number in this case
			version = link.text
    		#check if the first char is a digit, then its a version
			if version[0].isdigit():
				version_list.append(link.text)

	#return the first index since it's the latest version
	return(version_list[0])

"""
main func
"""
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-name')
    args = parser.parse_args()

    if args.name:
    	portname = args.name
    	print("The latest successful build of " + args.name + " is " + findLatestBuild(portname) + ".")
    else:
    	print("No port specified. Type 'python porthealth.py -h for more information.")

if __name__ == "__main__":
    main()