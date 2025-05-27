<template>
  <v-app>
    <v-app-bar app>
      <v-toolbar-title>メモ帳</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        color="primary"
        class="ma-2"
        @click="createNote"
      >
        メモを作成
      </v-btn>
    </v-app-bar>

    <v-main>
      <v-container>
        <NoteList ref="noteList" @create-note="createNote" />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import NoteList from './components/NoteList.vue';

export default {
  components: {
    NoteList
  },
  methods: {
    createNote() {
      this.$refs.noteList.createNote();
    }
  }
}
</script>
