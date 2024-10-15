<template>
	<Panel title="Clonning package repository">
		<pre class="output">{{ usePackage.addPackage.output }}</pre>
	</Panel>
</template>

<script lang="ts" setup>
const usePackage = usePackageState()
</script>

<style lang="scss" scoped>
.panel {
	.output {
		overflow: scroll;
	}
}
</style>