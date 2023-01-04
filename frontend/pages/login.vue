<template>
  <v-container fluid fill-height>
    <v-layout align-center justify-center>
      <v-flex xs12 sm8 md4>
        <v-card class="elevation-12">
          <v-toolbar dark color="primary">
            <v-toolbar-title>Login form</v-toolbar-title>
          </v-toolbar>
          <v-card-text>
            <v-form>
              <v-text-field
                prepend-icon="mdi-account"
                name="username"
                label="Username"
                type="text"
                v-model="user.username"
              ></v-text-field>
              <v-text-field
                id="password"
                prepend-icon="mdi-lock"
                name="password"
                label="Password"
                type="password"
                v-model="user.password"
                @keydown.enter="login"
              ></v-text-field>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" @click="login" @enter="login">Login</v-btn>
          </v-card-actions>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from "axios";
axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';
export default {
  name: "LoginPage",
  data() {
    return {
      user: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    async login() {
      await this.$auth.loginWith('local', { data: this.user }).then(() => {
        this.$forceUpdate();
        this.$router.push("/");
      });
    }
  },
};
</script>

<style></style>
