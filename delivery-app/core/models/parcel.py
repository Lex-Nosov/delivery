from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class Parcel(Base):
    __tablename__ = "parcels"
    title: Mapped[str] = mapped_column()
    weight: Mapped[float] = mapped_column()
    amount: Mapped[float] = mapped_column()

    type: Mapped[list["TypeParcel"]] = relationship(
        "TypeParcel", back_populates="parcels"
    )


class TypeParcel(Base):
    __tablename__ = "type_parcels"
    title: Mapped[str] = mapped_column()

    parcel: Mapped["Parcel"] = relationship("Parcel", back_populates="type_parcels")
