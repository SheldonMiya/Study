<template>
  <v-card>
    <v-card-title>
      <v-text-field
        v-model="title"
        label="タイトル"
      ></v-text-field>
    </v-card-title>

    <v-card-text>
      <v-textarea
        v-model="content"
        label="内容"
      ></v-textarea>

      <v-date-picker
        v-model="dueDate"
        label="期限"
      ></v-date-picker>
    </v-card-text>

    <v-card-actions>
      <v-btn
        color="primary"
        @click="saveNote"
      >
        保存
      </v-btn>
      <v-btn
        @click="cancelEdit"
      >
        キャンセル
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  props: {
    note: {
      type: Object,
      default: () => ({ title: '', content: '', dueDate: null }) // idを含めない
    }
  },
  data() {
    return {
      title: this.note.title,
      content: this.note.content,
      dueDate: this.note.dueDate,
      id: this.note.id
    };
  },
  methods: {
    saveNote() {
      this.$emit('save', { id: this.id, title: this.title, content: this.content, dueDate: this.dueDate });
    },
    cancelEdit() {
      this.$emit('cancel');
    },
  },
  watch: {
    note: {
      handler(newNote) {
        this.title = newNote.title;
        this.content = newNote.content;
        this.dueDate = newNote.dueDate;
        this.id = newNote.id;
      },
      immediate: true
    }
  }
};
</script>
