<template>
<div>
  <top-bar />
  <div>
  <v-container class="grey lighten-5 m-5 p-lg-5" style="height: 1000px;">
    <v-row class="justify-content-center m-lg-5">
      <template v-for="z in zonderTeam">
          <v-card
            :key="z.id"
            class="mx-auto"
            width="260"
            outlined
            tile
          >
          <v-img
            :key="z.id"
            :src="z.img"
            height="300px"
          />
          <v-card-title>
           {{ z.fullName }}
          </v-card-title>

          <v-card-subtitle>
            {{ z.role }}
          </v-card-subtitle>

          <v-card-actions>
            <v-btn
              color="grey lighten-2"
              text
            >
              Explore
            </v-btn>

            <v-spacer />

            <v-btn
              icon
              @click="show = !show"
            >
              <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
            </v-btn>
          </v-card-actions>

          <v-expand-transition>
            <div v-show="show">
              <v-divider />

              <v-card-text>
                {{ z.tel }}
                {{ z.info }}
                {{ z.img }}
                
              </v-card-text>
            </div>
          </v-expand-transition>
        </v-card>

          </template>
      </v-row>
    </v-container>
    </div>
  </div>
</template>


<script>
import TopBar from '../components/TopBar.vue'

export default {
    data () {
      return {
        show: false,
        zonderTeam: [
          {
            id: 1,
            fullName: "Nikita Stegura",
            role: "Developer",
            tel: "+7 (909) 920-99-94",
            img: "../assets/nikita.png",
            motto: "",
            info: "",

          },
          {
            id: 2,
            fullName: "Margo Andrianova",
            role: "Team Lead",
            tel: "+7 (916) 661-94-65",
            img: "../assets/margo.png",
            motto: "",
            info: "",
          },
          {
            id: 3,
            fullName: "Indiko Dzhalagonia",
            role: "Data Scientist",
            tel: "+7 (999) 989-26-85",
            img: "../assets/nick.png",            
            motto: "",
            info: "",
          },
          {
            id: 4,
            fullName: "Denis Volchugin",
            role: "Developer",
            tel: "+7 (985) 965-11-87",
            img: "../assets/den.png",            
            motto: "",   
            info: "4.434.682.001th Man on Earth",
          },                              
        ]
      }
    },
  components: {
    TopBar,
  }
}

</script>

