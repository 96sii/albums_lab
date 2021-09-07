import pdb
from models.album import Album
from models.artist import Artist

import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

album_repository.delete_all()
artist_repository.delete_all()

artist1 = Artist("U2")
artist_repository.save(artist1)
artist2 = Artist("Led Zeppelin")
artist_repository.save(artist2)

artist3 = Artist("Take That")
artist_repository.save(artist3)


album_1 = Album("Achtung Baby", artist1, 1991, 2)
album_repository.save(album_1)

album_2 = Album("Zooropa", artist1, 1993, 12)
album_repository.save(album_2)

album_3 = Album("Take That and Party", artist3, 1992, 10)
album_repository.save(album_3)

album_4 = Album("Physical Graffiti", artist2, 1970, 10)
album_repository.save(album_4)


pdb.set_trace()
