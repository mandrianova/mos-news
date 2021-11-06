<template>
	<v-main class="grey lighten-3">
		<v-container>
			<v-row>
				<v-col md="10">
					<v-sheet min-height="80vh" rounded="lg">
						<v-navigation-drawer right absolute>
							<v-container>
								<div class="my-3">Input Panel</div>
								<v-divider />
								<div class="my-6">
									<v-text-field
										v-for="p in payload"
										v-model="p.value"
										:label="p.name"
										:key="p.name"
										dense
										outlined
									/>
								</div>
								<h6 v-if="executionTime > 0">
									Execution time:
								</h6>
								{{ executionTime }} sec<br><br>
								<div class="my-3">
									<v-btn color="secondary" @click="callApi">
										Submit
									</v-btn>
								</div>
							</v-container>
						</v-navigation-drawer>
						<v-container id="main">
							<v-row>
								<v-col md="6">
									<h3>Recommendations</h3>
									<v-data-table
										:headers="headers"
										:items="recommendations"
										:loading="loading"
										loading-text="Loading... Please wait"
										class="elevation-1"
									/>
								</v-col>
								<v-col md="6">
									<h3 v-if="history">History</h3>
									<v-data-table
										:headers="headers"
										:items="history"
										:loading="loading"
										loading-text="Loading... Please wait"
										class="elevation-1"
									/>
								</v-col>
							</v-row>
						</v-container>
						<!--  -->
					</v-sheet>
				</v-col>
			</v-row>
		</v-container>
	</v-main>
</template>

<script>
import axios from 'axios';

export default {
	name: 'rec-input',
	data() {
		return {
			payload: [{ name: 'user_id', value: 20, type: 'int' }],
			loading: false,
			headers: [
				{
					text: 'id',
					value: 'id',
				},
				{
					text: 'title',
					value: 'title',
				},
				{
					text: 'date',
					value: 'date',
				},
			],
			recommendations: [
				{
					id: 248,
					title: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!',
					date: '2021-08-16 08:00',
				},
			],
			history: [
				{
					id: 1,
					title: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!',
					date: '2021-08-16 08:00',
				},
			],
			executionTime: null,
		};
	},
	methods: {
		callApi () {
			// reformat the payload from [{name: Age, value: 10}, ...] to {Age:10, ...}
			const start = Date.now();
			this.loading = true;
			const payload = this.payload.reduce(
				(acc, cur) => ({ ...acc, [cur.name]: cur.value }),
				{}
			);
			console.log('sending payload', this.payload);
			axios
				.get(`/recommendations/${payload.user_id}`, this.payload)
				.then((response) => {
					console.log('response', response);
					this.recommendations = response.data.recommendations;
					this.history = response.data.history;
					this.loading = false;
					const stop = Date.now();
					console.log(stop);
					const executionTime = (stop - start) / 1000;
					this.executionTime = executionTime;
				})
				.catch((e) => console.log(e));
		},
	},
};
</script>

<style>
.v-container {
	font-family: monospace;
	font-size: 0.3rem;
	font-weight: 100;
}
</style>
