#Sukhdeep Singh
#Sukhdeep.singh144@myhunter.cuny.edu

import tldextract

def get_domain_type(url):
    domain = tldextract.extract(url)
    tld_type = domain.suffix
    
    if tld_type == 'com':
        return 'commercial'
    elif tld_type == 'edu':
        return 'education'
    elif tld_type == 'org':
        return 'organization'
    elif tld_type == 'gov':
        return 'government'
    else:
        return 'other'

def main():
    url = input('Enter a website URL: ')
    domain_name = tldextract.extract(url).domain
    domain_type = get_domain_type(url)
    
    print(f'The website name is {domain_name} and its top-level domain is {domain_type}.')

if __name__ == '__main__':
    main()