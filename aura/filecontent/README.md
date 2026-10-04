# Aura/Xlsl FileContent integration

`File` owns metadata and points at a deduplicated `FileContent` row through `content_id`.
The content ID is the SHA-256 digest of UTF-8 encoded textual content.

The ORM relationship is intentionally `lazy="raise"` so callers must explicitly load content rather than accidentally pulling payloads into unrelated queries.

Orphan cleanup uses `NOT EXISTS`, avoiding PostgreSQL `NOT IN` + `NULL` behavior.
