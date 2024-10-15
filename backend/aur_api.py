import requests

def aur_package_info(name: str):
	result = requests.get(f'https://aur.archlinux.org/rpc/v5/info?arg[]={name}').json()
	print(result)
	if result['resultcount'] == 0:
		return None
	return result['results'][0]