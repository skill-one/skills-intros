"""Names shared by the upstream snapshot and the generated artifact tree.

`skills.jsonl` is the same file name on both sides of the pipeline (upstream
index in, profile index out) and `skills/` the same per-skill directory; keeping
them in one place means a rename cannot leave the reader and the writer apart.
"""

INDEX_NAME = "skills.jsonl"
SKILLS_SUBDIR = "skills"
MD_SUBDIR = "md"
