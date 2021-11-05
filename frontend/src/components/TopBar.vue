<template>
	<v-app-bar app color="white" flat>
		<v-container class="py-0 fill-height">
			<v-avatar>
				<img src="../assets/dudaism.gif" alt="Dude">
			</v-avatar>

			<v-btn v-for="link in links" :key="link" text>
				<router-link :to="{ name: link }">{{ link }}</router-link>
			</v-btn>

			<v-spacer />

			<v-responsive max-width="260">
				<v-text-field dense flat hide-details rounded solo-inverted />
			</v-responsive>
		</v-container>
	</v-app-bar>
</template>

<script>
export default {
	name: 'TopBar',
	data: () => ({
		links: ['recommendations', 'markup', 'documentation', 'about'],
	}),
};
</script>
