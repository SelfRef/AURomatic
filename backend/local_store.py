import os

def packages_dir():
	return '../pkgbuilds'

def local_package_list():
	return [entry.name for entry in os.scandir(packages_dir()) if entry.is_dir()]

def main():
	if not os.path.exists(packages_dir()):
		os.mkdir(packages_dir())

main()