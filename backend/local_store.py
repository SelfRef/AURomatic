import os

def package_dir():
	return '../pkgbuilds'

def local_package_list():
	return [entry.name for entry in os.scandir(package_dir()) if entry.is_dir()]

def main():
	if not os.path.exists(package_dir()):
		os.mkdir(package_dir())

main()