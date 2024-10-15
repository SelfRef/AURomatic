<template>
	<Panel title="Package details">
		<table>
			<tr v-for="item in infoViewModel">
				<td><label :for="item.key">{{ item.key }}:</label></td>
				<td><span :id="item.key">{{ convertValue(item.value) }}</span></td>
			</tr>
		</table>
	</Panel>
	<NuxtPage/>
</template>

<script lang="ts" setup>
const route = useRoute()
const info = ref<IAURPackageInfo>()

onMounted(async () => {
	const pkgName = route.params.pkg
	info.value = await $fetch(`/api/pkgbuilds/${pkgName}`)
})

const infoViewModel = computed<{key: string, value: string}[]>(() => {
	if (!info.value) return {}
	return [
		'Name',
		'Description',
		'Keywords',
		'Version',
		'License',
		'URL',
		'MakeDepends',
		'Maintainer',
		'Submitter',
		'FirstSubmitted',
		'LastModified',
		'OutOfDate',
	].map(key => ({
		key,
		value: info.value[key]
	}))
})

function convertValue(input: string | number | string[]) {
	if (input === null) return '-'
	switch (typeof input) {
		case 'number':
			return new Date(input*1000).toLocaleString('pl-PL')
		case 'object':
			return input.join(', ')
		default:
			return input
	}
}
</script>

<style lang="scss" scoped>
.panel {
	max-width: 500px;
}
</style>