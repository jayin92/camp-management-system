<template>
  <v-app dark>
    <v-navigation-drawer
      :key="$auth.loggedIn"
      v-model="drawer"
      :mini-variant="miniVariant"
      :clipped="clipped"
      fixed
      app
      v-if="render"
    >
      <v-list>
        <v-list-item
          v-for="(item, i) in filtered_item()"
          :key="item.title"
          :to="item.to"
          nuxt
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-divider />
        
        <v-list-item key="20" v-if="this.$auth.loggedIn">
          <v-list-item-action>
            <v-icon>mdi-account</v-icon>
          </v-list-item-action>
          <v-list-item-title> {{ this.$auth.user }} </v-list-item-title>
        </v-list-item>
      </v-list>

      <template v-slot:append>
        <div v-if="$auth.loggedIn" class="pa-2">
          <v-btn block @click="logout"> Logout </v-btn>
        </div>
      </template>
    </v-navigation-drawer>
    <v-app-bar :clipped-left="clipped" fixed app>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title>{{ title }}</v-toolbar-title>
      
    </v-app-bar>
    <v-main>
      <v-container fluid>
        <Nuxt />
      </v-container>
    </v-main>
    <v-footer app>
      <span>&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script>
export default {
  name: "DefaultLayout",
  data() {
    return {
      clipped: false,
      drawer: false,
      fixed: false,
      render: true,      
      items: [
        {
          icon: "mdi-apps",
          title: "Welcome",
          to: "/",
        },
        {
          icon: "mdi-file-account",
          title: "Review",
          to: "/review",
          loggedIn: true,
        },
        {
          icon: "mdi-account-check",
          title: "Overview",
          to: "/overview",
          loggedIn: true,
        },
        {
          icon: "mdi-login",
          title: "Login",
          to: "/login",
          loggedIn: false,
        },
      ],
      miniVariant: false,
      right: true,
      rightDrawer: false,
      title: "Camp Mangement System",
    };
  },
  methods: {
    logout() {
      this.$auth.logout().then(() => {
        this.$router.push("/login");
      });
    },
    filtered_item: function () {
      console.log(this.$auth.$loggedIn)
      return this.items.filter((item) => item.loggedIn !== !this.$auth.loggedIn);
    },
    reload() {
      this.render = false;
      this.$nextTick(() => {
        this.render = true;
      });
    }
  },
  watch: {
    '$auth.loggedIn': function (loggedIn) {
      console.log("Logged");
      this.$forceUpdate();
    }
  }
};
</script>
