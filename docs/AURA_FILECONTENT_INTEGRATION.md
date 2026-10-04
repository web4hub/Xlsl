# Aura/Xlsl FileContent integration

The persistence layer sits beneath the semantic `.qs` / `.dm` material described by this repository. A workbook or other textual artifact is ingested once, hashed with SHA-256, and stored as `FileContent`; file metadata references that content by `content_id`.

```text
Aura/Xlsl artifact
      |
      v
 File ingestion
      |
      v
 SHA-256 content identity
      |
      v
 FileContent <---- File metadata
      |
      +---- semantic (.qs/.dm) pipelines
      +---- AI / quantum pipelines
```

The FileContent layer deliberately does not couple to the Xlsl runtime: it provides stable content persistence beneath it.

## Validation boundary

Automated validation covers ORM relationships, content deduplication, and orphan cleanup. PostgreSQL migration execution against a live PostgreSQL server is not claimed unless a server is available.
