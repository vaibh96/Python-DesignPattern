
import sys
from notebook import Notebook


class Menu(object):
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_notes,
            "4": self.modify_notes,
            "5": self.quite,
            "6": self.delete_note,
        }

    def display_menu(self):
        print("""
        Notebook Menu
        1. Show 
        2. Search
        3. Add 
        4. Modify
        5. Quit
        6. DeleteNote
        """)

    def run(self):
        print("In run")
        """Display Menu According to choice"""
        while True:
            self.display_menu()
            choice = input("Enter the option :")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice ".format(choice))

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{0}: {1}\n{2}".format(note.id, note.memo, note.tag))

    def search_notes(self):
        filter = input("Enter search filter")
        note = self.notebook.search_note(filter)
        self.show_notes(note)

    def add_notes(self):
        memo = input("Enter the note")
        self.notebook.add_new_note(memo)
        print("Your note has been added successfully !!")

    def modify_notes(self):
        note_id = input("Enter the note id")
        memo = input("Enter the memo")
        tag = input("Enter the tag")
        if memo:
            self.notebook.modify_note(note_id, memo)
        if tag:
            self.notebook.modify_tag(note_id, tag)

    def delete_note(self):
        """deleting note based on note id"""
        note_id = input("Enter Note ID")
        if note_id:
            self.notebook.delete_note(note_id)
            print("Note has been deleted successfully !!")

    def quite(self):
        print("Exiting the program !!")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
