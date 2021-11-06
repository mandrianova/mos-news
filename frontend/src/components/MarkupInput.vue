<template>
	<v-main class="grey lighten-3">
		<v-container>
			<v-row class="justify-center">
				<v-col md="6">
					<v-sheet min-height="80vh" rounded="lg">
						<v-navigation-drawer right absolute>
							<v-container>
								<div class="my-3">Input Panel</div>
								<v-divider />
								<div class="my-4">
									<v-textarea
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
								{{ executionTime }} sec<br>
								<div class="my-3">
									<v-btn color="secondary" @click="callApi">
										Submit
									</v-btn>
								</div>
							</v-container>
						</v-navigation-drawer>
						<v-container id="main">
							<v-row>
							<v-col md=6>
									<h5 class="text-left">TAGS</h5>
									<v-list dense>
										<v-list-item
											v-for="tag in tags"
											:key="tag"
										>
											{{ tag }}
										</v-list-item>
										</v-list>
								</v-col>
								<v-col md=6>
									<h5 class="text-left">SPHERES</h5>
									<v-list dense>
										<v-list-item
											v-for="sphere in spheres"
											:key="sphere"
										>
											{{ sphere }}
										</v-list-item>
										</v-list>
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
	name: 'markup-input',
	data() {
		return {
			payload: [ 
				{name: 'title', value: 'Бесстрашные бойцы и сладкоежки: в Московском зоопарке поселились медоеды'}, 
				{name: 'preview_text', value: 'Медоеды известны своей смелостью. В случае если их жизни что-то угрожает, они без колебаний идут в атаку. Они запросто могут напасть на льва, леопарда и буйвола, им нипочем яд кобры и скорпиона.'},
				{name: 'full_text', value: 'Один из самых известных отморозков животного мира. Только медоед способен вести схватку, один против шести львов. Есть королевских кобр. Периодически драться с леопардами. Он имеет настолько сильную иммунную систему, что даже после смертельного укуса кобры он просто засыпает, а проснувшись дальше продолжает, есть эту же кобру.'},
			],
			loading: false,
			tags: [],
			spheres: [],
			results: {},
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
								{});
			console.log('performing API query', payload);
			axios
				.post('/auto_markup/generate_markups', payload)
				.then((response) => {
						console.log('response', response.data);
						this.tags = response.data.tags;
						this.spheres = response.data.spheres;
						this.results = response.data;
						this.loading = false;
						const stop = Date.now();
						// console.log(stop);
						const executionTime = (stop - start) / 1000;
						this.executionTime = executionTime;
				})
				.catch((e) => console.log(e));
		},
	},
};
</script>

<style>
.v-list {
	font-family: monospace;
	font-weight: 300;
}
</style>
