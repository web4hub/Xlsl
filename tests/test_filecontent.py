from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session, selectinload

from aura.filecontent import Base, ContentRepository, File, FileContent


def test_same_payload_is_deduplicated():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    repo = ContentRepository()

    with Session(engine) as session:
        repo.put(session, file_id="f1", name="a.txt", content="hello")
        repo.put(session, file_id="f2", name="b.txt", content="hello")
        session.commit()

        contents = session.scalars(select(FileContent)).all()
        files = session.scalars(select(File)).all()
        assert len(contents) == 1
        assert len(files) == 2
        assert files[0].content_id == files[1].content_id


def test_relationship_round_trip():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    repo = ContentRepository()

    with Session(engine) as session:
        repo.put(session, file_id="f1", name="a.txt", content="hello")
        session.commit()
        file = session.execute(
            select(File).options(selectinload(File.content)).where(File.id == "f1")
        ).scalar_one()
        assert file.content.content == "hello"


def test_orphan_cleanup_uses_references():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    repo = ContentRepository()

    with Session(engine) as session:
        repo.put(session, file_id="f1", name="a.txt", content="kept")
        session.add(FileContent(id="orphan", content="unused"))
        session.commit()
        assert repo.delete_orphans(session) == 1
        session.commit()
        assert session.get(FileContent, "orphan") is None
        assert session.get(FileContent, repo.digest("kept")) is not None
