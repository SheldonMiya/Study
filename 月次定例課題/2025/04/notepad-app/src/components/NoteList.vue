<template>
  <v-container fluid>
    <v-list>
      <v-list-item
        v-for="note in notes"
        :key="note.id"
        @click="showNoteDetail(note)"
      >
        <v-list-item-title>{{ note.title }}</v-list-item-title>
      </v-list-item>
    </v-list>

    <NoteEditor
      v-if="isEditing"
      :note="editingNote"
      @save="saveNote"
      @cancel="cancelEdit"
    />

    <NoteDetail
      v-if="isDetail"
      :note="selectedNote"
      @edit="editNote"
      @back="goBackToList"
      @delete="deleteNote"
    />
  </v-container>
</template>

<script>
import NoteService from '../services/NoteService';
import NoteEditor from './NoteEditor.vue';
import NoteDetail from './NoteDetail.vue';

export default {
  components: {
    NoteEditor,
    NoteDetail
  },
  data() {
    return {
      notes: [],
      isEditing: false,
      editingNote: null,
      isDetail: false,
      selectedNote: null,
    };
  },
  mounted() {
    this.loadNotes();
  },
  methods: {
    loadNotes() {
      this.notes = NoteService.getNotes();
    },
    createNote() {
      this.isEditing = true;
      this.editingNote = { title: '', content: '', dueDate: null }; // idを付与しない
    },
    editNote(note) {
      this.isEditing = true;
      this.isDetail = false;
      this.editingNote = { ...note };
    },
    saveNote(note) {
      if (typeof note.id !== 'undefined') {
        const index = this.notes.findIndex(n => n.id === note.id);
        if (index !== -1) {
          this.notes = [
            ...this.notes.slice(0, index),
            note,
            ...this.notes.slice(index + 1)
          ];
        }
      } else {
        note.id = Date.now();
        this.notes.push(note);
      }
      NoteService.saveNotes(this.notes);
      this.loadNotes();
      this.cancelEdit();
    },
    cancelEdit() {
      this.isEditing = false;
      this.isDetail = false;
      this.editingNote = null;
    },
    showNoteDetail(note) {
      this.isDetail = true;
      this.selectedNote = note;
    },
    goBackToList() {
      this.isDetail = false;
      this.selectedNote = null;
    },
    deleteNote(id) {
      this.notes = this.notes.filter(note => note.id !== id);
      NoteService.saveNotes(this.notes);
      this.loadNotes();
      this.goBackToList();
    },
  },
};
</script>
