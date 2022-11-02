from dataclasses import dataclass

import Notes


@dataclass
class NoteTimeStamped:
    note: Notes.Note
    start_time: int
    finish_time: int = 0
