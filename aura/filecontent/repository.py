from __future__ import annotations

import hashlib

from sqlalchemy import delete, exists, select
from sqlalchemy.orm import Session

from .models import File, FileContent


class ContentRepository:
    """Create/reuse content rows and clean unreferenced content safely."""

    @staticmethod
    def digest(content: str) -> str:
        return hashlib.sha256(content.encode("utf-8")).hexdigest()

    def put(self, session: Session, *, file_id: str, name: str, content: str) -> File:
        content_id = self.digest(content)
        row = session.get(FileContent, content_id)
        if row is None:
            row = FileContent(id=content_id, content=content)
            session.add(row)
            session.flush()

        file = session.get(File, file_id)
        if file is None:
            file = File(id=file_id, name=name, content_id=content_id)
            session.add(file)
        else:
            file.name = name
            file.content_id = content_id
        return file

    def delete_orphans(self, session: Session) -> int:
        referenced = exists(select(File.id).where(File.content_id == FileContent.id))
        result = session.execute(delete(FileContent).where(~referenced))
        return int(result.rowcount or 0)
