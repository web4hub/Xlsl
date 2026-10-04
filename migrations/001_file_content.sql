-- Aura/Xlsl content-addressed persistence.
CREATE TABLE IF NOT EXISTS file_contents (
    id VARCHAR(64) PRIMARY KEY,
    content TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

ALTER TABLE files
    ADD COLUMN IF NOT EXISTS content_id VARCHAR(64);

DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM pg_constraint
        WHERE conname = 'files_content_id_fkey'
          AND conrelid = 'files'::regclass
    ) THEN
        ALTER TABLE files
            ADD CONSTRAINT files_content_id_fkey
            FOREIGN KEY (content_id) REFERENCES file_contents(id) ON DELETE RESTRICT;
    END IF;
END $$;

CREATE INDEX IF NOT EXISTS ix_files_content_id ON files(content_id);

-- Existing rows must be backfilled before making content_id NOT NULL.
-- After backfill:
-- ALTER TABLE files ALTER COLUMN content_id SET NOT NULL;

-- NULL-safe orphan cleanup: NOT EXISTS avoids NOT IN / NULL semantics.
DELETE FROM file_contents fc
WHERE NOT EXISTS (
    SELECT 1 FROM files f WHERE f.content_id = fc.id
);
