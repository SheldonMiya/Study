const STORAGE_KEY = 'notepad-notes';

export default {
  getNotes() {
    const notes = localStorage.getItem(STORAGE_KEY);
    return notes ? JSON.parse(notes) : [];
  },
  saveNotes(notes) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(notes));
  },
};
