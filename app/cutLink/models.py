from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class Base(DeclarativeBase):
    pass

class Link_ORM(Base):
    __tablename__ = 'shortcutlinks'

    id: Mapped[int] = mapped_column(primary_key=True)
    source: Mapped[str] = mapped_column(unique=True)
    short: Mapped[str] = mapped_column()
    count: Mapped[int] = mapped_column()