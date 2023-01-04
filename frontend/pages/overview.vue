<template>
  <v-data-table
		:loading="!loaded"
		:headers="headers"
		:items="items" 
		:search="search"
		:custom-filter="filter"
		class="elevation-1"
		@click:row="handleRow($event)">
		<template v-slot:top>
        <v-text-field
          v-model="search"
          label="Search Applicant"
          class="mx-4"
        ></v-text-field>
      </template>
    <template v-slot:item.accept="{ item }">
        <v-simple-checkbox
              v-model="item.accept"
              :value="item.accept"
							@input="handleAccept(item)"
        ></v-simple-checkbox>    
    </template>
  </v-data-table>
</template>

<script>
// import axios
import axios from "axios";
export default {
  name: "OverviewPage",
  data() {
    return {
      items: [],
      applicant_id: 1,
      loaded: false,
      score: 0,
      reviews: [],
			search: "",
      headers: [
				{text: "報名序號", value: "id", width: 100},
        {
          text: "姓名",
          align: "start",
          sortable: false,
          value: "name",
        },
        { text: "性別", value: "sex"},
        { text: "平均評分", value: "avg_score"},
				{ text: "報名階段", value: "phase" },
        { text: "錄取", value: "accept" },
      ],
    };
  },
  async created() {
    axios.defaults.headers.common["Authorization"] =
      this.$auth.strategy.token.get();
    console.log(this.$auth.strategy.token.get());
    await axios.get("/api/applicant/api").then((response) => {
      this.items = response.data;
      this.items.sort(function (a, b) {
        return a.id - b.id;
      });
    });
    
    this.loaded = true;
  },
  methods: {
    async handlePagination(e) {
      // get score with applicant_id if not found return 0
      await axios.get("/api/applicant/review/api").then((response) => {
        this.reviews = response.data;
        this.score =
          this.reviews.find((review) => {
            return review.applicant == this.applicant_id;
          })?.score || 0;
      });
    },
    async handleScoring(e) {
      axios.defaults.headers.common["Authorization"] =
        this.$auth.strategy.token.get();
      await axios.post("/api/applicant/review/api", {
        applicant: this.applicant_id,
        score: this.score,
      });
    },
		async handleAccept(item) {
			// console.log(item);
			axios.defaults.headers.common["Authorization"] =
				this.$auth.strategy.token.get();
			await axios.put("/api/applicant/api/"+item.id, item);
			await axios.get("/api/applicant/api").then((response) => {
      this.items = response.data;
      this.items.sort(function (a, b) {
        return a.id - b.id;
      });
    });
		},
		async handleRow(e) {
			console.log(e.id);
			this.$router.push("/review?id="+e.id);
		},
		filterName(value, search, item){
			return value != null &&
          search != null &&
          typeof value === 'string' &&
          value.toString().indexOf(search) !== -1
		}
  },
};
</script>
