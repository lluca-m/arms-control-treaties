# Writer tools for the Notion treaty database

Scripts used on 11 October 2026 to write treaty records into the Notion Disarmament Treaties Database. The coding rules are in `../CODEBOOK.md` (section "Coding specification (SPEC_v3)").

- `hub_blocks.py`: Notion REST helpers; reads the token from the research pipeline's local `api_keys.json` (never stored here).
- `writer3.py`: the current writer. `write3(page_id, record_json, name)` writes properties (null leaves a value; only `clear_fields` erases), upserts provision and event rows, upserts this writer's own Editorial Log entries (matched by title), and regenerates the key-facts table. `write_participation(...)` upserts Participation rows. `resync_all_keyfacts()` refreshes key facts after manual property edits.
- `writer2.py`, `writer.py`: earlier versions that `writer3.py` imports.
- `export_pilot.py`: exports finished records to Markdown in `../pilot_review_2026-10-11/` for review.
- `rerun_test.py`: repeatability check (writes the pilot records twice and compares).

Per-record source files (the agent research output, as corrected) are in `../records/`; `records/pilot2/rows_list.json` maps Record IDs to Notion page IDs. Run the scripts with `../records` as the working directory.

Page bodies were assembled by hand through the Notion connector (linked views for provisions, participation and events inside collapsed toggles); after any full-page rewrite, check that no list item has jumped to the top of the page.
