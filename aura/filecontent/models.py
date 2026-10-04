from __future__ import annotations

from datetime import datetime
from typing import List

from sqlalchemy import DateTime, ForeignKey, String, Text, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class FileContent(Base):
    """Deduplicated textual payload addressed by SHA-256."""

    __tablename__ = "file_contents"

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    files: Mapped[List["File"]] = relationship(
        back_populates="content", cascade="save-update", lazy="raise"
    )


class File(Base):
    """File metadata pointing to one deduplicated FileContent row."""

    __tablename__ = "files"

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    name: Mapped[str] = mapped_column(String(512), nullable=False)
    content_id: Mapped[str] = mapped_column(
        ForeignKey("file_contents.id", ondelete="RESTRICT"), nullable=False, index=True
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )

    content: Mapped[FileContent] = relationship(
        back_populates="files", lazy="raise"
    )
