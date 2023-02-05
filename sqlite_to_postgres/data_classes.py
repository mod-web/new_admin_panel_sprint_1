from dataclasses import dataclass, asdict


@dataclass
class CommonTable:

    @property
    def get_values(self):
        return '\t'.join([str(x) for x in asdict(self).values()])


@dataclass
class Filmwork(CommonTable):
    __slots__ = (
        'id', 'title', 'description', 'creation_date',
        'certificate', 'file_path', 'rating', 'type',
        'created', 'modified'
    )
    id: str
    title: str
    description: str
    creation_date: str
    certificate: str
    type: str
    file_path: str
    rating: float
    created: str
    modified: str


@dataclass
class Genre(CommonTable):
    __slots__ = (
        'id', 'name', 'description', 'created', 'modified'
    )
    id: str
    name: str
    description: str
    created: str
    modified: str


@dataclass
class Person(CommonTable):
    __slots__ = (
        'id', 'full_name', 'created', 'modified'
    )
    id: str
    full_name: str
    created: str
    modified: str


@dataclass
class GenreFilmWork(CommonTable):
    __slots__ = (
        'id', 'film_work_id', 'genre_id', 'created'
    )
    id: str
    film_work_id: str
    genre_id: str
    created: str


@dataclass
class PersonFilmWork(CommonTable):
    __slots__ = (
        'id', 'film_work_id', 'person_id', 'role', 'created'
    )
    id: str
    film_work_id: str
    person_id: str
    role: str
    created: str
