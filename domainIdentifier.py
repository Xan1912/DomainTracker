from tld import get_tld



def get_domain_name(url):
	domain_name = get_tld(url)
	return domain_name

def main():
	url = "http://www.totalpest.co/"
	name = get_domain_name(url)
	print name

if __name__=='__main__':
	main()