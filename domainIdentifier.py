from tld import get_tld

def getUrl():
	name = raw_input("Enter company name:")
	url = "https://www.google.co.in/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=" + name


def get_domain_name(url):
	domain_name = get_tld(url)
	return domain_name

def main():
	url = ""
	name = get_domain_name(url)
	print name

if __name__=='__main__':
	main()