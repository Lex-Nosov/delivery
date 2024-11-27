from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class Parcel(Base):
    __tablename__ = "parcels"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)  # Добавляем первичный ключ
    title: Mapped[str] = mapped_column()
    weight: Mapped[float] = mapped_column()
    amount: Mapped[float] = mapped_column()
    type_id: Mapped[int] = mapped_column(ForeignKey("type_parcels.id"))  # Внешний ключ

    # Связь "многие к одному"
    type: Mapped["TypeParcel"] = relationship("TypeParcel", back_populates="parcels")


class TypeParcel(Base):
    __tablename__ = "type_parcels"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)  # Добавляем первичный ключ
    title: Mapped[str] = mapped_column()

    # Связь "один ко многим"
    parcels: Mapped[list["Parcel"]] = relationship("Parcel", back_populates="type")
