<template>
	<nav class="panel">
		<ul>
			<li v-for="pkg in pkgList">
				<NuxtLink :to="'/packages/' + pkg">pkg</NuxtLink>
			</li>
		</ul>
	</nav>
	<NuxtPage/>
</template>

<script lang="ts" setup>
const pkgList = ref([])

onMounted(async () => {
	pkgList.value = await $fetch('/api/pkgbuilds')
})
</script>
