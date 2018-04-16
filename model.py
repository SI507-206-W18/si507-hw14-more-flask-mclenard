import json
from datetime import datetime


GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []
try:
    idnum = int(entries[0]['id']) + 1
except:
    idnum = 0

def init(app):
    global entries
    try:
        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        f.close()
    except:
        print('Couldn\'t open', GUESTBOOK_ENTRIES_FILE)
        entries = []

def get_entries():
    global entries
    return entries

def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE, idnum
    now = datetime.now()
    #time_string = now.strftime("%b %d, %Y %-I:%M %p")
    time_string = str(now)
    entry = {"author": name, "text": text, "timestamp": time_string, "id": idnum}
    idnum += 1
    entries.insert(0, entry) ## add to front of list
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")

def delete_entry(id):
    global entries, GUESTBOOK_ENTRIES_FILE
    for ent in entries:
        try:
            if ent["id"] == int(id):
                entries.remove(ent)
                print("Entry removed.")
        except:
            print("This entry does not have an ID number.")
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not open guestbook file to delete entry.")
