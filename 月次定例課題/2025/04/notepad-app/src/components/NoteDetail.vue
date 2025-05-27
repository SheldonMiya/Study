<template>
  <v-card>
    <v-card-title>
      {{ note.title }}
    </v-card-title>

    <v-card-text>
      <div v-html="formattedContent"></div>
    </v-card-text>

    <v-card-text>
      期限: {{ formatDate(note.dueDate) }}
    </v-card-text>

    <v-card-actions>
      <v-btn
        color="primary"
        @click="editNote"
      >
        編集
      </v-btn>
      <v-btn
        color="error"
        @click="deleteNote"
      >
        削除
      </v-btn>
      <v-btn
        @click="goBack"
      >
        戻る
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: {
    note: {
      type: Object,
      required: true,
    },
  },
  computed: {
  formattedContent() {
    // 改行を<br>に変換し、XSS対策でエスケープも行う
    if (!this.note.content) return '';
    return this.note.content
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/\n/g, '<br>');
    }
  },
  methods: {
    editNote() {
      this.$emit('edit', this.note);
    },
    deleteNote() {
      this.$emit('delete', this.note.id);
    },
    goBack() {
      this.$emit('back');
    },
    formatDate(dateString) {
      if (!dateString) return '';
      const date = new Date(dateString);
      const year = date.getFullYear();
      const month = String(date.getMonth() + 1).padStart(2, '0');
      const day = String(date.getDate()).padStart(2, '0');
      return `${year}-${month}-${day}`;
    },
  },
};
</script>
