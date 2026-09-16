# Treaty database: issues to fix

Surfaced 13 September 2026 while comparing the Notion **Disarmament Treaties Database** (110 rows, 55 properties; data source `collection://2172b9a4-1a30-80a0-b0ab-000b95b272ea`) against Vaynman's Adversarial Agreements Dataset. Nothing below has been changed in Notion yet. Row-by-row matching evidence is in `Vaynman 2026 comparison/notion_vs_vaynman_mapping.csv`; the venue discussion is in `2026-09-13 - JPR Special Data Feature as Venue.md`.

How these were found: exact reading of the Notion properties, and title-by-title adjudication of every candidate pair against Vaynman's appendix table. Status and date errors are either internal contradictions within a row or contradict well-documented treaty histories; check each against the treaty text or depositary record when fixing.

## 1. Duplicate rows

Merge each pair into one row, keeping whichever carries more coding, then archive the other. Check relations (Articles, News Tracker, Countries, Strategic Systems, Treaty Participation) before archiving.

- [ ] **ENMOD**: [Convention on the Prohibition of Military or any other Hostile Use of Environmental Modification Techniques](https://app.notion.com/2572b9a41a308122b2a4c64d1d131296) and [Convention on Environmental Modification Techniques](https://app.notion.com/25c2b9a41a3081bbbfedd525565c66cf)
- [ ] **CPPNM**: [Convention on the Physical Protection of Nuclear Material](https://app.notion.com/25c2b9a41a30819db423c4fcf49c1c19) (dated) and [Nuclear Material Convention](https://app.notion.com/2572b9a41a308193bac8fbae971e4d4e) (undated)
- [ ] **Nuclear Terrorism Convention**: [International Convention for the Suppression of Acts of Nuclear Terrorism](https://app.notion.com/2572b9a41a3081be87e0dfbe07705f0d) and [Suppression of Nuclear Terrorism](https://app.notion.com/2572b9a41a3081ba9f81cf441b0846da)
- [ ] **Ballistic missile code of conduct**: [Hague Code of Conduct Against Ballistic Missile Proliferation (HCoC)](https://app.notion.com/2572b9a41a308167b43eda865adf4835) and [International Code of Conduct against Ballistic Missile Proliferation (ICOC)](https://app.notion.com/25c2b9a41a3081e78d5bdcd0f50b6a32). ICOC was the draft name; adopted at The Hague on 25 November 2002 as HCoC.
- [ ] **Washington 1922**: [Washington Conference on the Limitation of Armament (1921-1922)](https://app.notion.com/2362b9a41a3080639101de36c94a44d4) and [Washington Naval Treaty](https://app.notion.com/2572b9a41a30819b82bfd726d06a1401). The conference produced several instruments; decide whether the dataset records conferences or instruments (see section 4), then keep one.

## 2. Wrong or contradictory dates and statuses

- [ ] [CWC](https://app.notion.com/2572b9a41a308157943ae2f6a1171880): Date Adopted and Date Entered into Force are both 1997-04-29. That is the entry-into-force date; the convention was opened for signature in January 1993.
- [ ] [CPPNM](https://app.notion.com/25c2b9a41a30819db423c4fcf49c1c19): entry into force 1979-02-08 precedes adoption 1980-03-03. The dates are swapped or one is wrong.
- [ ] [CCW Protocol II](https://app.notion.com/2572b9a41a30810e93e5ddc12e80f17f): dated 1996-05-03 (adopted) and 1998-12-03 (in force), which are the Amended Protocol II dates. The original Protocol II is 1980. A separate [CCW Amended Protocol II](https://app.notion.com/2572b9a41a308185ac57d07aa9d4ab4f) row exists with no dates.
- [ ] [START I](https://app.notion.com/25c2b9a41a3081be8eeac9c890cf51dd): Status "Never Entered into Force" contradicts its own entry-into-force date (1994-12-05). It entered into force and expired in December 2009.
- [ ] [SALT I](https://app.notion.com/25c2b9a41a30819dbfc2d3cac021987b): Status "In Force". The Interim Agreement expired in October 1977.
- [ ] [New START](https://app.notion.com/2572b9a41a3081b991c3e36ef64f1335): Status "In Force". Its entry-into-force date (2011-02-05) is recorded; the treaty expired on 5 February 2026.
- [ ] [START II](https://app.notion.com/2572b9a41a3081bcbab1eb7931fe5883): Status "Expired". It never entered into force.
- [ ] [ABM Treaty](https://app.notion.com/2572b9a41a3081f28a9ff18539cda8c2): no entry-into-force date (3 October 1972).
- [ ] [Moon Agreement](https://app.notion.com/2572b9a41a30815eb971ff628afb7f35): Status "In Force" with no entry-into-force date.
- [ ] 67 of 110 rows have no Date Adopted at all.
- [ ] Status vocabulary does not fit non-binding instruments: [ICOC/HCoC](https://app.notion.com/25c2b9a41a3081e78d5bdcd0f50b6a32) and [Zangger Committee](https://app.notion.com/25c2b9a41a3081fcbd86d50c65d41156) are coded "In Force".

## 3. Names and abbreviations

- [ ] [Agreed Framework](https://app.notion.com/25c2b9a41a3081c4b4c0c175f629e318): abbreviation reads "US - ROK"; it is US–DPRK.
- [ ] [Washington Conference](https://app.notion.com/2362b9a41a3080639101de36c94a44d4): the abbreviation field holds a URL (history.state.gov). Move it to Treaty URL.
- [ ] Years used as abbreviations: [Geneva Convention of 1949](https://app.notion.com/2c62b9a41a30806cb47ac195cacd68ae) ("1949"), [Additional Protocol I](https://app.notion.com/25c2b9a41a3081afa001dd7198c5a036) and [Additional Protocol II](https://app.notion.com/25c2b9a41a3081e783d0cbbedbc8c844) (both "1977"), [Additional Protocol III](https://app.notion.com/25c2b9a41a308160a681f8597cac92b6) ("2005").
- [ ] [PCASED](https://app.notion.com/2572b9a41a3081349137d522dc266791): typo "forSecurity" in the full name.
- [ ] Rows with no abbreviation: [G-7 Global Partnership](https://app.notion.com/25c2b9a41a308111b50ee9904be8b164), [UN Firearms Protocol](https://app.notion.com/25c2b9a41a3081328a64fc2777989fa5), [PSI](https://app.notion.com/25c2b9a41a30818dae0ec4256da99481), [GICNT](https://app.notion.com/25c2b9a41a3081f5b642d01b3dd8f6bb), [UN Programme of Action on SALW](https://app.notion.com/25c2b9a41a3081fe95a5fbefe2c3b9a6), [Rush-Bagot](https://app.notion.com/28d2b9a41a30809f8e39cc46922d634e), [US–Norway 1984 atomic energy agreement](https://app.notion.com/25d2b9a41a30808fa3b9fdf74665d82b).
- [ ] Treaty ID is filled on only 2 rows. A stable identifier is needed before any export.

## 4. Unit of observation: bundled, conflated or unclear rows

The dataset needs a written rule on whether a row is a conference, a treaty, or each separate instrument (protocols, amendments, versions). These rows break any single rule:

- [ ] [ABM Treaty](https://app.notion.com/2572b9a41a3081f28a9ff18539cda8c2) bundles the 1974 Protocol in one row; Vaynman codes the protocol separately. START I omits the 1992 Lisbon Protocol; TTBT omits its 1990 Protocol.
- [ ] [Nuclear Suppliers Group - Zangger Committee](https://app.notion.com/25c2b9a41a3081fcbd86d50c65d41156) conflates two distinct supplier regimes.
- [ ] [Shanghai Agreement](https://app.notion.com/2572b9a41a30815e995ccc9d304f2266): the full name ("Mutual Reduction of Military Forces in the Border Areas") is the 1997 Moscow agreement; the abbreviation is the 1996 Shanghai confidence-building agreement. Two instruments in one row.
- [ ] [Vienna Document](https://app.notion.com/2572b9a41a3081288e4adfc18bca9cbc): no version stated (1990, 1992, 1994, 1999, 2011 all exist).
- [ ] [Geneva Convention of 1949](https://app.notion.com/2c62b9a41a30806cb47ac195cacd68ae): four conventions in one row.
- [ ] Conference rows alongside their instruments: [Hague I Peace Conference of 1899](https://app.notion.com/2572b9a41a308122970ce69c7eca2016) with separate rows for its conventions and declarations; [Hague II Peace Conference of 1907](https://app.notion.com/2572b9a41a3081c28fc2eea2a988edf9) likewise.
- [ ] [Mongolia NWFZ](https://app.notion.com/2572b9a41a308130bc44f81ac19c65b0): a single-state status established by national law, a UNGA resolution and P5 declarations, not a treaty. Needs an instrument-type field if kept.

## 5. Inclusion criteria: rows to justify or drop

No written definition of what counts as an arms control instrument exists yet. These rows will force the decision:

- [ ] Initiatives and partnerships, not agreements: [PSI](https://app.notion.com/25c2b9a41a30818dae0ec4256da99481), [GICNT](https://app.notion.com/25c2b9a41a3081f5b642d01b3dd8f6bb), [G-7 Global Partnership](https://app.notion.com/25c2b9a41a308111b50ee9904be8b164), [PCASED](https://app.notion.com/2572b9a41a3081349137d522dc266791).
- [ ] Negotiations never concluded: [FMCT](https://app.notion.com/2572b9a41a3081e9890ff84f7ec55f24) (Status "Under Negotiation"), [PAROS](https://app.notion.com/2572b9a41a3081eaa26fdefd4dfa0c47).
- [ ] Peaceful-use cooperation rather than arms limitation: [US–Norway 1984 atomic energy agreement](https://app.notion.com/25d2b9a41a30808fa3b9fdf74665d82b).
- [ ] Humanitarian law without a weapons limitation: [Additional Protocol III](https://app.notion.com/25c2b9a41a308160a681f8597cac92b6) (distinctive emblem), [Hague 1899 Convention I](https://app.notion.com/2572b9a41a3081bf86cee99df94d9108) (pacific settlement of disputes).
- [ ] Counter-terrorism conventions: Nuclear Terrorism Convention (two rows, see section 1), [Inter-American Convention against Terrorism](https://app.notion.com/2572b9a41a30813c8d8ff2da353b08dc).
- [ ] Coverage decision against Vaynman's universe: she includes about 33 peace settlements and armistices with arms clauses and about 37 confidence-building, incidents-at-sea and notification agreements that are absent here. Either state why they are out of scope or add them.

## 6. Coding completeness

- [ ] Verification Mechanism filled on 32 of 110 rows; Type of Limitation on 36; Compliance History on 35.
- [ ] Strategic substitutability is not in the release scope (decision 13 September 2026), but the README still lists it.

## 7. Schema problems to resolve before export

- [ ] Free text stored as select or multi-select options: Amendment procedures (one option is a full paragraph of treaty text), Duration (16 date-specific options), Extension provisions, Withdrawal Provisions, Review Conference Schedule, Adopted at. Each needs a categorical variable plus a separate text note.
- [ ] Quantitative Limits has a stray option "5".
- [ ] No per-value source (treaty article) or coder confidence. CROAD's certainty and confidence variables are the model.
- [ ] No standard identifiers for linking: country codes for parties, UN treaty registration numbers, and a crosswalk to Vaynman's codes (the mapping CSV is the start of one).
- [ ] Five coders recorded in "Done by" (Laura, Tilda, Jaden, Katherine, Jeremy); no double-coded subsample or agreement statistic.
- [ ] Property names carry instructions in parentheses (e.g. "Date Adopted (When treaty text was finalized/agreed upon, usually at a conference or negotiation)"); rename to short variable names and move the definitions into a codebook.

## 8. Repository

- [ ] `README.md` frames the dataset around Paper 2 and lists strategic substitutability; rewrite to the objective-properties scope.
- [ ] This file, the venue note and `Vaynman 2026 comparison/` are untracked in git.
