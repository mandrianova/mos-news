import sendRequest from './axios.js';
// import getCookie from './helpers/getCookie.js';

// Vue.use(VueFormulate);
// Vue.use(Vuetify);

const app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    vuetify: new Vuetify(),
    data: function () {
        return {
            payload: [
                { name: 'user_id', value: 20, type: 'int' },
            ],
            headers: [
                {
                    text: 'id',
                    align: 'start',
                    value: 'id'
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
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
            ],
            history: [
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
                {id: 248, title: 'some title Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem eum in voluptatem impedit ex modi eaque voluptatibus est dolorem. Tenetur esse vel laboriosam eos dolor unde eaque distinctio dolorem natus!', date: '2021-08-16 08:00'},
            ],
            links: ['Recommendations', 'Auto markup', 'Documentation', 'About us'],
        }
    },
    methods: {
        call_api: function() {
            // reformat the payload from [{name: Age, value: 10}, ...] to {Age:10, ...}
            payload = this.payload.reduce(
                (acc, cur) => ({ ...acc, [cur.name]: cur.value }),
                {}
            );
            console.log('sending payload', payload);
            axios
                .post(`/recommendations/${payload.user_id}`, this.payload)
            // sendRequest(`/recommendations/${payload.user_id}`, "POST", this.payload)
                // .then((response) => {
                //     console.log("response", response);
                // })
                // .then((data) => {
                //     // console.log(data);
                //     this.recommendations = data.recommendations;
                // })
                // .catch((e) => console.log(e));
        },
    },
    template: `
    <v-app id="inspire">
    <v-app-bar app color="white" flat>
        <v-container class="py-0 fill-height">
            <v-avatar>
                <img src="static/img/dudaism.gif" alt="Dude">
            </v-avatar>

            <v-btn v-for="link in links" :key="link" text>
                [[ link ]]
            </v-btn>

            <v-spacer></v-spacer>

            <v-responsive max-width="260">
                <v-text-field
                    dense
                    flat
                    hide-details
                    rounded
                    solo-inverted
                ></v-text-field>
            </v-responsive>
        </v-container>
    </v-app-bar>

    <v-main class="grey lighten-3">
        <v-container>
            <v-row>
                <v-col md=10>
                    <v-sheet min-height="80vh" rounded="lg">
                        <v-navigation-drawer right absolute>
                            <v-container>
                                <div class="my-3">Input Panel</div>
                                <v-divider></v-divider>
                                <div class="my-6">
                                    <v-text-field
                                        v-for="p in payload"
                                        v-model="p.value"
                                        :label="p.name"
                                        :key="p.name"
                                        dense
                                        outlined
                                    >
                                    </v-text-field>
                                </div>
                                <div class="my-3">
                                    <v-btn
                                        color="secondary"
                                        @click="call_api"
                                    >
                                        Submit
                                    </v-btn>
                                </div>
                            </v-container>
                        </v-navigation-drawer>
                        <v-container id="main">
                            <v-row>
                                <v-col md=6>
                                <h1>New recommendations</h1>
                                    <v-data-table
                                    :headers="headers"
                                    :items="recommendations"
                                    class="elevation-1"
                                    ></v-data-table>  
                                    [[ payload ]]
                                </v-col>
                                <v-col md=6>
                                <h1 v-if="history">History</h1>
                                    <v-data-table
                                    :headers="headers"
                                    :items="history"
                                    class="elevation-1"
                                    ></v-data-table>
                                </v-col>
                            </v-row>
                        </v-container>
                        <!--  -->
                    </v-sheet>
                </v-col>
            </v-row>
        </v-container>

    </v-main>
</v-app>
`
});
