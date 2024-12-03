from funcky.named_constants import TICKS_PER_BAR
from funcky.parts.mono_part import MonoPart

from funcky.songs.simple_song import SimpleSong
from tracks.hello_world.tracks import track_one


song = SimpleSong(
    tracks=[
        MonoPart(
            generator=track_one,
            ticks_per_bar=TICKS_PER_BAR,
        )
    ]
)
