from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Url(Base):

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    original_url: Mapped[str]
    short_url: Mapped[str]

    def __str__(self):
        return f'{self.__class__.__name__} (id={self.id}, orig_url={self.original_url}, short_url={self.short_url})'

    def __repr__(self):
        return str(self)
