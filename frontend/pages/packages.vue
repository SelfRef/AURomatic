<template>
	<Panel title="Packages">
		<div class="header">
			<button @click="addPackage">Add package</button>
		</div>
		<ul>
			<li v-for="pkg in usePackage.packageList">
				<NuxtLink :to="'/packages/' + pkg">{{ pkg }}</NuxtLink>
			</li>
		</ul>
	</Panel>
	<NuxtPage/>
</template>

<script lang="ts" setup>
const usePackage = usePackageState()

onMounted(async () => {
	fetchPackages()
})

</script>

<style scoped lang="scss">
.panel {
	display: flex;
	flex-direction: column;
}
</style>