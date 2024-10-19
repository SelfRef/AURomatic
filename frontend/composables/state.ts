import type { IAURPackageInfo } from "~/utils/api-models"

export const usePackageState = () => useState<{
	addPackage: {
		output: string,
		name: string
	},
	packageList: string[]
	packageInfo: {
		[key: string]: IAURPackageInfo | null
	}
}>('package', () => ({
	addPackage: {
		output: '',
		name: ''
	},
	packageList: [],
	packageInfo: {}
}))

export function isDev() {
	return process.env.NODE_ENV === 'development'
}

export async function fetchPackages() {
	const usePackage = usePackageState()
	usePackage.value.packageList = await $fetch('/api/pkgbuilds')
}

export async function addPackage() {
	const usePackage = usePackageState()
	const name = prompt("AUR package name")

	if (name) {
		navigateTo(`/packages/${name}/add`)
		usePackage.value.addPackage.name = name
		usePackage.value.addPackage.output = ''
		const response = await fetch('/api/pkgbuilds/'+name, { method: 'post' });
		await streamResponseToVariable(response, usePackage.value.addPackage, 'output')
		fetchPackages()
	}
}