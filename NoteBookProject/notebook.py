import datetime

last_id = 0


class Note:

    def __init__(self, memo, tag=""):
        self.memo = memo
        self.tag = tag
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        """Determine if this note matches the filter
        text. Return True if it matches, False otherwise.
        Search is case sensitive and matches both text and
        tags."""
        if filter in self.memo:
            return filter in self.memo

        return None


class Notebook:
    def __init__(self):
        self.notes = []

    def add_new_note(self, memo, tags=""):
        """adding new note with optional tag"""
        self.notes.append(Note(memo, tags))

    def search_note(self, filter):
        return [note for note in self.notes if note.match(filter)]

    def find_note(self, note_id):
        for note in self.notes:
            if str(note_id) == str(note.id):
                return note
        return None

    def modify_note(self, note_id, memo):
        note = self.find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False

    def modify_tag(self, note_id, tag):
        note = self.find_note(note_id)
        if note:
            note.tag = tag
            return True
        return False

    def delete_note(self, note_id):
        note = self.find_note(note_id)
        if note:
            self.notes.remove(note)
            return True
        return False
