<template>
	<header>
		AURomatic
	</header>
	<main>
		<nav class="panel">
			<ul>
				<li><NuxtLink to="/" >Home</NuxtLink></li>
				<li><NuxtLink to="/packages" >Packages</NuxtLink></li>
			</ul>
		</nav>
		<NuxtPage />
	</main>
</template>

<style lang="scss">
#app {
	display: flex;
	flex-direction: column;

	main {
		display: flex;
		flex-direction: row;
	}
}
</style>