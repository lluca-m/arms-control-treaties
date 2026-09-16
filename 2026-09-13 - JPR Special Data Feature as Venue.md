# JPR Special Data Feature as a venue for the treaty dataset

Noted 13 September 2026, while reviewing *Journal of Peace Research* 63(5) from the journal monitor.

## Scope decision (Laura, 13 September 2026)

The first release is a clean version of the **objective treaty properties** only. Strategic substitutability is not part of it and will be discussed separately. The current `README.md` still lists substitutability and frames the dataset around Paper 2; it needs rewriting before release.

## The venue

JPR runs a dedicated article type, the **Special Data Feature**, for new datasets or major revisions of existing ones. From the author guidelines (https://academic.oup.com/jpr/pages/author-guidelines):

- Maximum 6,000 words including everything; 200–300 word abstract; 2–6 keywords.
- Less theoretical and empirical demand than a regular article, but it must show "how the new data can make a genuine contribution to the study of conflict and peace."
- Back matter: acknowledgements, CRediT author contributions, conflicts of interest, funding, data availability statement, AI usage declaration.
- Replication materials go to PRIO (https://www.prio.org/journals/jpr/replicationdata) at conditional acceptance: data in original format and CSV, annotated analysis scripts, codebook, software output, and a readme. Additional hosting (Dataverse, GitHub) is allowed.

Other venues that publish dataset articles, not yet checked against this project: *Conflict Management and Peace Science*, *International Interactions*.

## The two models from JPR 63(5), September 2026

Both PDFs were queued for the research pipeline on 13 September 2026 and will have Articles pages.

1. **Cadorin, Nina M.** "Introducing the Coercive Recruitment of Adults Dataset (CROAD), 1990–2021." *JPR* 63(5): 1009–1017. https://doi.org/10.1093/jopres/xjag026. Open access, CC BY 4.0.
   - Structure: why the dataset is needed (with a table comparing it to the two existing datasets) → the project (data collection, variable description, descriptive patterns) → application → conclusion.
   - Coding: named sources with systematic search strings; a practice is recorded only if reported by at least two sources; coded missing when little is known about a group. Every observation carries **coder confidence** and **source certainty** variables so users can drop weak observations.
   - No intercoder reliability statistic reported; one additional coder acknowledged.
   - Linkage: built on UCDP dyad identifiers, so it merges directly with UCDP data.
   - Application: replicates Cohen's published study of wartime rape with the new variable.
   - Release: dataset, codebook, R analysis files and online appendix deposited with PRIO.
2. **Ryckman, Kirssa Cline, and Chaelin Kwon.** "Introducing the War-Related Protests data." *JPR* 63(5): 1018–1027. https://doi.org/10.1093/jopres/xjag035. Paywalled.
   - Africa 1990–2017; a typology of protester demands, targets and repressing actors; collection procedures; descriptives; an illustrative application on protest size. Full structure to be read from the PDF.

A third model with dual hosting: van Baalen and Höglund, "Introducing the MAVERICK dataset," *JPR* 63(1): 98–106 (https://doi.org/10.1093/jopres/xjaf012), deposited at PRIO and on Harvard Dataverse (https://doi.org/10.7910/DVN/GRXTTZ).

## Gaps between the Notion treaty database and a data feature (13 September 2026)

Measured on the Disarmament Treaties Database in Notion (110 treaties, 55 properties):

- **Thin core coding.** Verification Mechanism is filled on 32 treaties, Type of Limitation on 36, Compliance History on 35, Treaty ID on 2.
- **Free text stored as select options.** Amendment procedures, Duration, Extension provisions, Withdrawal Provisions and Review Conference Schedule hold treaty-specific wording as dropdown values; Quantitative Limits has a stray option "5". These need a categorical variable plus a separate text note before export.
- **No standard identifiers.** Nothing links treaties or parties to existing data (country codes, UN treaty registration numbers, existing treaty datasets such as Vaynman's).
- **No provenance or confidence per value.** CROAD's coder-confidence and source-certainty variables are the model; for treaties the natural source field is the article of the treaty text.
- **No reliability check.** Five coders are recorded (Laura, Tilda, Jaden, Katherine, Jeremy); a double-coded subsample with an agreement statistic would answer the obvious reviewer question.
- **Application and comparison still to choose.** A data feature needs a demonstration (a published finding re-estimated with the treaty variables) and a comparison table against existing treaty datasets.

## The benchmark: Vaynman's Adversarial Agreements Dataset (checked 13 September 2026)

**Published and complete.** Vaynman, Jane. 2026. "Replication Data for: Enemies in Agreement: Political Volatility and the Design of Arms Control." Harvard Dataverse, V1, released 5 February 2026, CC0. https://doi.org/10.7910/DVN/EUFGGL. Cited in Chapter 3 of *Enemies in Agreement* (Cambridge UP, 2026); the online appendix is also at cambridge.org/vaynman.

Files in the deposit: `AAD_fulldata_vars_Nov2025` (dyad-year analysis file, 236.6 MB), `treaty_info.tab` (225 rows: code, year, number of countries, monitoring level only, no treaty names), `Vaynman_Appendix_final.pdf` (75 pages; Part III, Table 1 lists every agreement by code, year and name with its information-provision code), and two Stata do-files. No standalone codebook; coding rules are in Appendix Part II.

**Her design choices (Appendix Part II, pp. B3–B5):**

- Universe: "any formal agreement that limits a security-related capability or behavior of states", recorded in writing, surveyed 1700–2010; 225 agreements, 1817–2010. Explicitly includes war termination and ceasefire agreements with arms provisions and confidence-building measures; excludes pure border agreements.
- Sources: Goldblat's *Arms Control: The New Guide to Negotiations and Agreements*, the UN Treaty Series, NGO sources, foreign ministry and UK parliamentary records, the Russian MFA treaty archive (several Russian-only agreements included).
- One coded outcome: information provisions from the treaty text: none, reporting and notification, observation or monitoring, verification; aggregated into low (137) and high (88). Coded from a detailed textual codebook, then checked against expert assessments in the literature. No intercoder reliability reported.
- Date is the signature date, not ratification. Multilateral treaties with more than ten parties keep only the ten most powerful parties by CINC score as "designers". Built as dyad-years to merge with COW and EUGene.

**Overlap with the Notion treaty database** (110 rows; matched by year and title, every pair adjudicated by reading both titles; mapping in `Vaynman 2026 comparison/notion_vs_vaynman_mapping.csv`):

- 65 Notion rows correspond to a Vaynman agreement (60 same instrument, 3 partial, 2 ambiguous as to version); 3 more are duplicate Notion rows; 42 have no counterpart.
- Notion covers 72 of her 225 codes.
- What Notion has and she does not: instruments after 2010 (ATT, TPNW, UNGA 77/41); 1864–1907 laws-of-war instruments outside her set; export-control and nonproliferation regimes and initiatives (Australia Group, PSI, G-7 Global Partnership, GICNT); US CTR assistance agreements; counter-terrorism conventions; negotiations never concluded (FMCT, PAROS); several CCW protocols she codes only through the 1981 framework convention.
- What she has and Notion does not (rough grouping of 153): about 33 peace settlements and armistices with arms clauses, about 37 CBM, incident-at-sea and notification agreements (many bilateral: India-Pakistan, Russia-China, USSR INCSEA agreements), about 24 declarations, statements and guidelines, 12 UN or organizational instruments, and about 46 other treaties.
- The two datasets rest on different universes: hers is adversarial agreements built for dyadic analysis of monitoring; this one is arms control and disarmament instruments coded along many design dimensions and continuing past 2010. The comparison table in a data feature should state that difference directly, and the inclusion criteria for this dataset need writing down before the gap on CBMs and war-termination agreements can be defended or closed.

**Data problems surfaced by the matching** (duplicates, wrong dates and statuses, bad abbreviations, bundled rows, inclusion questions) are listed row by row, with Notion links, in `2026-09-13 - Treaty Database Issues to Fix.md`.

## Positioning: is there still room to publish? (discussion, 13 September 2026)

Not as another list of arms control agreements. Vaynman's dataset is now the public universe for 1817–2010, and a thinner list of the same treaties invites "why not extend Vaynman?"

The room is in three places:

1. **Design breadth.** Vaynman codes one outcome (information provisions). This dataset's fields cover what she does not: the stage limited (use, development, production, stockpiling, transfer, testing, deployment), the form of the limit, duration, withdrawal, amendment, review conferences, enforcement and national implementation. Koremenos's *Continent of International Law* codes design, but on a random sample across issue areas rather than arms control specifically.
2. **Lifecycle after 2010.** Her data ends before the post-Cold War architecture came apart (INF and Open Skies withdrawals, CFE, New START expiry). Status, withdrawal and termination fields carry the question the field is asking now.
3. **Instrument type.** Legally binding treaties, political commitments, supplier regimes and failed negotiations, coded as such on purpose.

Framing: complementary to Vaynman, with a published crosswalk to her codes so users can join a treaty-level design dataset to her dyad-year data.

The bottleneck is coding, not venue: core fields filled for about a third of rows, duplicates and wrong statuses, and no written inclusion criteria. Candidate application for a data feature: whether treaties with particular design features (withdrawal provisions, fixed duration, verification) survived the post-2010 period better, which only this dataset's fields can test.

Open decision: design breadth or post-2010 survival as the lead contribution. Returning to this later.
