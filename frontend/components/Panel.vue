<template>
	<section class="panel">
		<div class="header">
			<span class="title">{{ props.title }}</span>
			<slot name="header" />
		</div>
		<slot/>
	</section>
</template>

<script lang="ts" setup>
const props = defineProps({
	title: String
})
</script>

<style lang="scss" scoped>
.panel {
	display: flex;
	flex-direction: column;

	.header {
		width: 100%;
		display: flex;
		flex-direction: row;

		.title {
			display: inline-block;
			width: 100%;
			text-align: center;
		}
	}
}
</style>