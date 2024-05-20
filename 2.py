import sys , requests, re, random, string
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init
from requests.packages.urllib3.exceptions import InsecureRequestWarning
init(autoreset=True)
fr  =   Fore.RED
fg  =   Fore.GREEN

banner = '''{}
		   
hmei7  
\n'''.format(fr)
print banner
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')

def ran(length):
	letters = string.ascii_lowercase
	return ''.join(random.choice(letters) for i in range(length))

Pathlist = ['/wp-admin/setup-config.php?step=1', '/wordpress/wp-admin/setup-config.php?step=1', '/wp-admin/install.php?step=1', '/images/images/cache.php']

class EvaiLCode:
	def __init__(self):

		self.headers = {"User-Agent": "Apache/2.4.34 (Ubuntu) OpenSSL/1.1.1 (internal dummy connection)",
		  "Accept": "*/*",
		  "Accept-Language": "en-US,en;q=0.5",
		  "Accept-Encoding": "gzip, deflate",
		  "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
		  "X-Requested-With": "XMLHttpRequest",
		  "Connection": "close"}

	
	def URLdomain(self, site):

		if site.startswith("http://") :
			site = site.replace("http://","")
		elif site.startswith("https://") :
			site = site.replace("https://","")
		else :
			pass
		pattern = re.compile('(.*)/')
		while re.findall(pattern,site):
			sitez = re.findall(pattern,site)
			site = sitez[0]
		return site
		
		
	def checker(self, site):
		try:
			
			url = "http://" + self.URLdomain(site)
			for Path in Pathlist:
				check = requests.get(url + Path, headers=self.headers, verify=False, timeout=10).content
				if('setup-config.php?step=2' in check or 'install.php?step=2' in check or 'method=post ><input type=password name=' in check):
					print('Target:{} --> {}[Succefully]').format(url, fg)
					open('SEA-GHOST.txt','a').write(url + Path + "\n")
					break
				else:
					print('Target:{} -->! {}[Failid]').format(url, fr)
					
		except:
			pass



	
Control = EvaiLCode()	
def RunUploader(site):
	try:
		Control.checker(site)
	except:
		pass
mp = Pool(15)
mp.map(RunUploader, target)
mp.close()
mp.join()
