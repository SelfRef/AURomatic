<template>
	<Panel title="Packages">
		<template #header>
			<button @click="addPackage">+</button>
		</template>
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

	.header {
		button {
			margin-left: 10px;
		}
	}
}
</style>