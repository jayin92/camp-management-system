<template>
  <!-- <v-data-table :headers="headers" :items="items" class="elevation-1"></v-data-table> -->
  <v-row no-gutters align-self="center" v-if="loaded">
    <v-col cols="3" md="3"></v-col>
    <v-col cols="6" md="6" align-self="center">
      <v-pagination
        v-model="applicant_id"
        :length="items.length"
        @input="handlePagination($event)"
        v-if="loaded"
      ></v-pagination>
    </v-col>
    <v-col cols="3" md="3"></v-col>
    <v-col cols="auto" md="2">
      <v-card tile height="100%">
        <v-card-text>報名序號</v-card-text>
      </v-card>
    </v-col>
    <v-col cols="auto" md="10">
      <v-card tile height="100%">
        <v-card-text>{{ items[applicant_id - 1].id }}</v-card-text>
      </v-card>
    </v-col>

    <v-col cols="auto" md="2">
      <v-card tile height="100%">
        <v-card-text>報名時間</v-card-text>
      </v-card>
    </v-col>
    <v-col cols="auto" md="10">
      <v-card tile height="100%">
        <v-card-text>{{ items[applicant_id - 1].register_time }}</v-card-text>
      </v-card>
    </v-col>

    <v-col cols="auto" md="2">
      <v-card tile height="100%">
        <v-card-text>Email</v-card-text>
      </v-card>
    </v-col>
    <v-col cols="auto" md="10">
      <v-card tile height="100%">
        <v-card-text>{{ items[applicant_id - 1].email }}</v-card-text>
      </v-card>
    </v-col>
    <v-col cols="auto" md="2">
      <v-card tile height="100%">
        <v-card-text>姓名</v-card-text>
      </v-card>
    </v-col>
    <v-col cols="auto" md="10">
      <v-card tile height="100%">
        <v-card-text>{{ items[applicant_id - 1].name }}</v-card-text>
      </v-card>
    </v-col>
    <v-col cols="auto" md="2">
      <v-card tile height="100%">
        <v-card-text>生日</v-card-text>
      </v-card>
    </v-col>
    <v-col cols="auto" md="10">
      <v-card tile height="100%">
        <v-card-text>{{ items[applicant_id - 1].birthday }}</v-card-text>
      </v-card>
    </v-col>
    <v-col cols="auto" md="2">
      <v-card tile height="100%">
        <v-card-text>性別</v-card-text>
      </v-card>
    </v-col>
    <v-col cols="auto" md="10">
      <v-card tile height="100%">
        <v-card-text>{{ items[applicant_id - 1].sex }}</v-card-text>
      </v-card>
    </v-col>
    <v-col cols="auto" md="2">
      <v-card tile height="100%">
        <v-card-text>地址</v-card-text>
      </v-card>
    </v-col>
    <v-col cols="auto" md="10">
      <v-card tile height="100%">
        <v-card-text>{{ items[applicant_id - 1].address }}</v-card-text>
      </v-card>
    </v-col>
    <v-col cols="auto" md="2">
      <v-card tile height="100%">
        <v-card-text>學校</v-card-text>
      </v-card>
    </v-col>
    <v-col cols="auto" md="10">
      <v-card tile height="100%">
        <v-card-text>{{ items[applicant_id - 1].school }}</v-card-text>
      </v-card>
    </v-col>
    <v-col cols="auto" md="2">
      <v-card tile height="100%">
        <v-card-text>就讀班群</v-card-text>
      </v-card>
    </v-col>
    <v-col cols="auto" md="10">
      <v-card tile height="100%">
        <v-card-text>{{ items[applicant_id - 1].major }}</v-card-text>
      </v-card>
    </v-col>
    <v-col cols="auto" md="2">
      <v-card tile height="100%">
        <v-card-text>社團</v-card-text>
      </v-card>
    </v-col>
    <v-col cols="auto" md="10">
      <v-card tile height="100%">
        <v-card-text>{{ items[applicant_id - 1].club }}</v-card-text>
      </v-card>
    </v-col>
    <v-col cols="auto" md="2">
      <v-card tile height="100%">
        <v-card-text>特殊飲食</v-card-text>
      </v-card>
    </v-col>
    <v-col cols="auto" md="10">
      <v-card tile height="100%">
        <v-card-text>{{ items[applicant_id - 1].special_dietary }}</v-card-text>
      </v-card>
    </v-col>
    <v-col cols="auto" md="2">
      <v-card tile height="100%">
        <v-card-text>特殊疾病</v-card-text>
      </v-card>
    </v-col>
    <v-col cols="auto" md="10">
      <v-card tile height="100%">
        <v-card-text>{{ items[applicant_id - 1].special_disease }}</v-card-text>
      </v-card>
    </v-col>
    <v-col cols="auto" md="2">
      <v-card tile height="100%">
        <v-card-text>Facebook</v-card-text>
      </v-card>
    </v-col>
    <v-col cols="auto" md="10">
      <v-card v-bind:href="items[applicant_id - 1].facebook">
        <v-card-text>{{ items[applicant_id - 1].facebook }}</v-card-text>
      </v-card>
    </v-col>
    <v-col cols="auto" md="2">
      <v-card tile height="100%">
        <v-card-text>自我介紹</v-card-text>
      </v-card>
    </v-col>
    <v-col cols="auto" md="10">
      <v-card tile height="100%">
        <v-card-text>{{
          items[applicant_id - 1].self_introduction
        }}</v-card-text>
      </v-card>
    </v-col>
    <v-col cols="auto" md="2">
      <v-card tile height="100%">
        <v-card-text>生活照</v-card-text>
      </v-card>
    </v-col>
    <v-col cols="auto" md="10">
      <v-card tile height="100%" v-bind:href="items[applicant_id - 1].picture">
        <v-card-text>{{ items[applicant_id - 1].picture }}</v-card-text>
      </v-card>
    </v-col>
    <v-col cols="auto" md="2">
      <v-card tile height="100%">
        <v-card-text>參加動機</v-card-text>
      </v-card>
    </v-col>
    <v-col cols="auto" md="10">
      <v-card tile height="100%">
        <v-card-text>{{ items[applicant_id - 1].motivation }}</v-card-text>
      </v-card>
    </v-col>

    <v-col cols="auto" md="2">
      <v-card tile height="100%">
        <v-card-text>想要說的話</v-card-text>
      </v-card>
    </v-col>
    <v-col cols="auto" md="10">
      <v-card tile height="100%">
        <v-card-text>{{ items[applicant_id - 1].want_to_say }}</v-card-text>
      </v-card>
    </v-col>

    <v-col cols="auto" md="2">
      <v-card tile height="100%">
        <v-card-text>報名階段</v-card-text>
      </v-card>
    </v-col>
    <v-col cols="auto" md="10">
      <v-card tile height="100%">
        <v-card-text>{{ items[applicant_id - 1].phase }}</v-card-text>
      </v-card>
    </v-col>
    <v-col cols="auto" md="2">
      <v-card tile height="100%">
        <v-card-text>評分</v-card-text>
      </v-card>
    </v-col>
    <v-col cols="auto" md="10">
      <v-card tile height="100%">
      <v-rating
        color="primary"
        empty-icon="mdi-star-outline"
        full-icon="mdi-star"
        half-icon="mdi-star-half-full"
        hover
        size="35"
        length="10"
        v-model="score"
        @input="handleScoring($event)"
      ></v-rating>
    </v-card>
    </v-col>
    <v-col cols="3" md="3"></v-col>
    <v-col cols="6" md="6" align-self="center">
      <v-pagination
        v-model="applicant_id"
        :length="items.length"
        @input="handlePagination($event)"
        v-if="loaded"
      ></v-pagination>
    </v-col>
    <v-col cols="3" md="3"></v-col>
  </v-row>
</template>

<script>
// import axios
import axios from "axios";
export default {
  name: "ReviewPage",
  data() {
    return {
      items: [],
      applicant_id: 1,
      loaded: false,
      score: 0,
      reviews: []
    };
  },
  async created() {
    this.applicant_id = parseInt(this.$route.query.id) || 1;
    axios.defaults.headers.common["Authorization"] =
      this.$auth.strategy.token.get();
    console.log(this.$auth.strategy.token.get());
    await axios.get("/api/applicant/api").then((response) => {
      this.items = response.data;
      this.items.sort(function (a, b) {
        return a.id - b.id;
      });
    });
    await axios.get("/api/applicant/review/api").then((response) => {
      this.reviews = response.data;
      this.score = this.reviews.find((review) => {
        return review.applicant == this.applicant_id;
      })?.score || 0;
    });
    this.loaded = true;
  },
  methods: {
    async handlePagination(e) {
      // get score with applicant_id if not found return 0
      await axios.get("/api/applicant/review/api").then((response) => {
        this.reviews = response.data;
        this.score = this.reviews.find((review) => {
          return review.applicant == this.applicant_id;
        })?.score || 0;
      });
    },
    async handleScoring(e){
      axios.defaults.headers.common["Authorization"] = this.$auth.strategy.token.get();
      await axios.post("/api/applicant/review/api", {
        applicant: this.applicant_id,
        score: this.score,
      });
    }
  },
};
</script>
