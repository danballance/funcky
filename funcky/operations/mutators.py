"""
Mutators can only modify existing notes in a part, they cannot insert.
"""
from funcky.sequences import NoteSequence


def scale(seq: NoteSequence) -> NoteSequence:
    total_iterations = 96
    for i in range(total_iterations):
        if seq[i] is not None:
            if i in [0, 12]:  # 1,2 - 8ths
                seq[i].note=60  # middle C
            elif i in [24, 36]:  # 3,4 - 8ths
                seq[i].note=63  # middle Eb
            elif i in [48, 60]:  # 5,6 - 8ths
                seq[i].note=67  # middle G
            elif i in [72, 84]:  # 7,8 - 8ths
                seq[i].note=70  # middle Bb
    return seq
