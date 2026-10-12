# Codebook: Disarmament Treaties Database

Single reference for the Notion Disarmament Treaties Database (Instruments) and its linked databases: what each field means, why it exists, and how records are coded. Compiled 11 October 2026 from the property descriptions written into Notion that day, the v2/v3 coding specification, and the project's 2021 research design.

## Databases

- **Instruments** (Disarmament Treaties Database; database `2172b9a41a3080798862e526c0451113`, data source `collection://2172b9a4-1a30-80a0-b0ab-000b95b272ea`): one row per instrument, regime, initiative, negotiation or conference.
- **Treaty Provisions** (`1be0ad26c4134f6da434cc59d7c5e394`): one row per distinct obligation on one activity for one class of party (restriction type, value and unit, bound parties, article).
- **Treaty Events** (`c474dab17e5e4b43bbf3a03f3493da73`, data source `collection://3007b892-e9a6-489e-99b5-1645e9eecf37`): dated events, oldest first; Date Precision and Date as Reported keep month- or year-only dates honest; timelines sort on the numeric Sort Key (YYYYMM00).
- **Treaty Editorial Log (internal)** (`3f62b9a41a3081979f69cb581b3c2b93`): corrections, research notes and old page text; one entry per instrument and type, updated in place; never public.
- **Treaty Participation Database 1**: state-level participation, intended as the authoritative record of parties and dates.
- Cross-referenced: Countries Database, Articles, News Tracker, Military Systems (relation named Strategic Systems), Nuclear Fundamentals.

## How to read the field statuses

Each Instruments property carries a hover description in Notion beginning with its status. **Current (v2)**: coded under the specification below and exported to the website. **Internal**: working flags, not exported. **Legacy (v1)**: hidden in views, never exported, kept only until any unique content is migrated; several record the 2021 research questions behind the project and say so.

## Properties: Current (v2) (57)

| Property | Type | Description |
|---|---|---|
| Record Type | select | Current (v2). Instrument, Regime, Initiative, Negotiation, Conference or Supporting instrument (a related instrument kept as its own record only for structured comparison; hidden from default views and excluded from headline counts). Why: keeps binding agreements apart from export-control regimes, initiatives and unfinished negotiations, so counts compare like with like. |
| Instrument Form | select | Current (v2). Legal form of the text: treaty, protocol, amendment, executive agreement, resolution, code of conduct and so on. Why: form shows how states chose to commit and what approval it required. |
| Legal Character | select | Current (v2). Legally binding, politically binding, contested or not established. Why: binding and political commitments are explained differently, so they must not be pooled. |
| Instrument Status | select | Current (v2). Status now: in force, not yet in force, never entered into force, expired, terminated, superseded or suspended. Why: the basic filter for what still constrains states. |
| Negotiation Status | select | Current (v2). Negotiations only: concluded, ongoing, stalled or abandoned. Why: failed and unfinished efforts matter as much as concluded ones for explaining when states accept limits. |
| Participation Structure | select | Current (v2). Bilateral, plurilateral (closed), multilateral (open) or unilateral. Why: replaces the v1 bilateral/multilateral split, which hid closed great-power arrangements. |
| Date Adopted (When treaty text was finalized/agreed upon, usually at a conference or negotiation) | date | Current (v2). Formal adoption of the text: a conference's adoption act or, where none exists, the signature that concluded it; preparatory approval of wording by a commission is an event. A day only when the source gives one; otherwise leave empty and record the reported date in Treaty Events. Why: anchors the timeline and era. |
| Opened for Signature (for multilateral, often same or shortly after adoption date) | date | Current (v2). Date opened for signature, or signed for bilateral agreements; a day only when the source gives one. Why: separates agreeing a text from committing to it. |
| Date Entered into Force | date | Current (v2). Date of entry into force from the depositary or an official record. Why: separates agreements that bound states from those that never took effect. |
| Expiration Date | date | Current (v2). Date the instrument ended (expiry, termination, supersession). Pairs with End Reason. Why: measures how long agreements lasted. |
| End Reason | select | Current (v2). Why the instrument ended: expiry, withdrawal, supersession, termination and so on. Why: tells apart agreements that ran their course from those that broke down. |
| Weapon Families | multi_select | Current (v2). Weapons covered, from a fixed list of 21. Why: the main filter by technology; replaces the free-form v1 Type of Weapons. |
| Legal Subject Matter | multi_select | Current (v2). Arms limitation, nonproliferation, conduct of hostilities, arms trade, risk reduction, demilitarized zones, testing or nuclear security. Why: separates arms control proper from IHL and export control. |
| Operating Environment | multi_select | Current (v2). Where obligations apply: land, sea, seabed, air, outer space, celestial bodies or not specific. Why: lets domain regimes such as seabed and space be compared. |
| Region | multi_select | Current (v2). Geographic coverage when limited to a region; empty means worldwide. Why: identifies zone and regional agreements. |
| Number of Parties | number | Current (v2). Current states parties on the date in Parties As Of; left blank when present-day participation is unresolved (a historical participant count is then generated from Participation). Why: a dated snapshot of reach; the Participation database is to hold the authoritative record. |
| Number of Signatories | number | Current (v2). Signatories on the date in Parties As Of. |
| Parties As Of | date | Current (v2). Date of the party and signatory counts. Why: counts change, so every count carries its date. |
| Key Non-Signatories | text | Current (v2). States whose absence matters, such as nuclear-armed states outside the TPNW. Why: who stays out often says more about an agreement than who joins. |
| Information Provisions | multi_select | Current (v2). Declarations and data exchange, notifications, periodic reports, or none. Why: transparency obligations, coded to compare with Vaynman's information categories. |
| Inspection & Access | multi_select | Current (v2). Routine or challenge inspection, continuous monitoring, observation flights, fact-finding, voluntary observation (optional access, never coded as inspection), or none. Why: how intrusive verification is, central to Paper 2's comparison of detection and acceptance. |
| Monitoring Means Specified | multi_select | Current (v2). National technical means, non-interference with them, an international monitoring system, cooperative measures, or none specified. Why: separates self-help verification from international verification. |
| Institutional Oversight | select | Current (v2). International organization, treaty body or commission, depositary only, or none. Why: institutional design is a standing explanation of compliance. |
| Consultation Mechanism | select | Current (v2). Standing commission, consultative meetings, review conferences only, diplomatic channels only, or none. Why: how parties raise compliance concerns short of withdrawal. |
| Reporting Requirements | select | Current (v2). Yes if parties must submit declarations, data or periodic reports to another party, a body or the depositary. Values: Yes, No, Not specified in text, Not applicable, Not yet checked. |
| Enforcement Mechanisms (Sanctions/What happens if caught) | select | Current (v2). Yes if the text sets consequences beyond consultation: sanctions, suspension of rights, referral to the UN Security Council. Why: tests whether enforcement design affects compliance. |
| Dispute Resolution Mechanism | select | Current (v2). Yes if the text specifies a procedure for disputes over interpretation or application: a standing body, consultation, arbitration or the ICJ. |
| National authority requirements | select | Current (v2). Yes if each party must designate, establish or use a national body, focal point or centre for implementation or communication. |
| Technical cooperation provisions | select | Current (v2). Yes if the text provides for assistance or the exchange of technology or expertise among parties. Why: such benefits can explain why weaker states join. |
| Third party roles specified | select | Current (v2). Yes if the text gives functions to a non-party: an international organization, the UN Secretary-General beyond custody, observers, basing states. |
| Reservations allowed/prohibited | select | Current (v2). Whether reservations are allowed, prohibited, limited or not specified. |
| Duration Type | select | Current (v2). Indefinite, fixed term, fixed term (renewable), until obligations met, or not specified. Why: compares how long states committed; replaces v1 Duration. |
| Duration (years) | number | Current (v2). Length of a fixed term in years. |
| Extension Type | select | Current (v2). How the term can be extended: none stated, automatic, by agreement of parties, by review conference, other. |
| Extension Clause | text | Current (v2). The text's extension wording, article cited. |
| Withdrawal Type | select | Current (v2). None stated, notice, supreme interests (with notice), mutual consent only, other. Why: exit terms shape both the cost of joining and the credibility of commitment. |
| Withdrawal Notice (months) | number | Current (v2). Notice required before a withdrawal takes effect, in months. |
| Withdrawal Clause | text | Current (v2). The text's withdrawal wording, article cited. |
| Amendment Procedure | select | Current (v2). Consensus, unanimity, two-thirds majority, simple majority, none stated, other. |
| Amendment Clause | text | Current (v2). The text's amendment wording, article cited. |
| Review Conferences | select | Current (v2). None, periodic, or ad hoc / on request. |
| Review Interval (years) | number | Current (v2). Years between periodic review conferences. |
| Number of review conferences held | number | Current (v2). Formal review conferences held to date, not meetings of states parties. |
| Entry into force requirements | text | Current (v2). Conditions for entry into force: number or list of ratifications, named states. Why: demanding conditions, such as the CTBT's Annex 2, explain agreements that never take effect. |
| Number of Articles | number | Current (v2). Articles in the text; the counting basis is in the coding notes. |
| Word Count | number | Current (v2). Words in the text, counted on the basis stated in the coding notes. Why: a rough measure of how much an agreement specifies. |
| Weapons/Systems Limited | text | Current (v2). One or two sentences on what the instrument limits. |
| Key Provisions | text | Current (v2). Main obligations, concise and article-cited; each restriction is a row in Treaty Provisions. |
| Behavior Change Required | text | Current (v2). Whether parties had to change existing forces or practices or only forgo future ones. Why: from the 2021 design; separates real constraint from codified restraint, central to Paper 2. |
| Historical Background & Motivation (Preamble) | text | Current (v2). Three to five sentences on origins and stated purpose. Why: context for why states agreed, the 2021 design's reason-for-agreeing question. |
| Signed at: | text | Current (v2). Place of signature. |
| Depository | text | Current (v2). Depositary government or organization. |
| Treaty URL | url | Current (v2). Link to the official text; Source Quality grades it. |
| Treaty Name (Abbreviation/ Common Name) | text | Current (v2). Short or common name used in lists and on the website. |
| file | file | Current (v2). Attached official text or depositary documents. Attachments are not searchable; key text belongs in the page body. |
| Duration Clause | text | Current (v2). The treaty's own wording on duration, quoted or closely paraphrased with the article cited. Pairs with Duration Type and Duration (years). Why: lets readers check the coded category against the text. |
| Treaty complexity (word count, number of articles, annex/appendix/protocol) | text | Current (v2). Count basis: which text, language and parts (annexes, protocols, notes) the Number of Articles and Word Count were counted from, and how. Why: without the basis the counts are not comparable across records. (The writer fills it from count_basis; the name is the v1 name.) |

## Properties: Internal (8)

| Property | Type | Description |
|---|---|---|
| Source Quality | select | Internal. Whether the linked text is an official text, a reproduction, secondary only or not found; negotiations without a concluded text are not applicable. |
| Last Verified | date | Internal. Date the record was last checked against sources. |
| In Paper 2 Appendix | checkbox | Internal. Ticked for the agreements in Paper 2's appendix survey. Not exported. |
| Vaynman Code | text | Internal. The agreement's code in Vaynman's Adversarial Agreements Dataset, for matching. |
| Vaynman Dataset Version | text | Internal. Version of Vaynman's dataset used for the match. |
| Vaynman Information Category | select | Internal. Vaynman's information-provision category, used in Paper 2's appendix table. |
| Vaynman Value Source | select | Internal. Whether the Vaynman value comes from her dataset or was coded here by her rules. |
| Content Complete | checkbox | Internal. Ticked when the record has been researched, checked against sources, written, reviewed and has its participation rows. Why: tracks the one-by-one run and tells the website export which records are ready. |

## Properties: Legacy (v1) (25)

| Property | Type | Description |
|---|---|---|
| Status | select | Legacy (v1), hidden, not exported. Old combined status; replaced by Instrument Status and Negotiation Status. |
| Legal Form | select | Legacy (v1), hidden, not exported. Replaced by Instrument Form and Legal Character. |
| Type of Weapons | multi_select | Legacy (v1), hidden, not exported. Free list of weapon types; replaced by Weapon Families. |
| Type of Limitation (Use/Development/Stockpiling) | multi_select | Legacy (v1), hidden. From the 2021 question whether agreements limited use, development or stockpiling, or precursors. Why: bans on use and on capability differ. Now restriction types in Treaty Provisions. |
| Quantitative Limits (Zero/Specific Level) | select | Legacy (v1), hidden. From the 2021 question whether arms were limited to zero or to a level. Why: a ban and a ceiling pose different cheating problems. Now value and unit in Treaty Provisions. |
| Verification Mechanism | multi_select | Legacy (v1), hidden. From the 2021 question whether the sides could monitor compliance. Replaced by Information Provisions, Inspection & Access and Monitoring Means Specified. |
| Compliance History | text | Legacy (v1), hidden. From the 2021 question whether agreements were adhered to and had a positive effect. Replaced by attributed compliance events in Treaty Events. |
| Duration | select | Legacy (v1), hidden, not exported. Replaced by Duration Type, Duration (years) and Duration Clause. |
| Extension provisions | select | Legacy (v1), hidden, not exported. Replaced by Extension Type and Extension Clause. |
| Withdrawal Provisions | multi_select | Legacy (v1), hidden, not exported. Replaced by Withdrawal Type, Withdrawal Notice (months) and Withdrawal Clause. |
| Review Conference Schedule | multi_select | Legacy (v1), hidden, not exported. Replaced by Review Conferences, Review Interval (years) and Number of review conferences held. |
| Sunset clauses | select | Legacy (v1), hidden, not exported. Captured by Duration Type and Expiration Date. |
| Date Ratified (Country Specific) | text | Legacy (v1), hidden, not exported. Country-specific dates belong in the Participation database. |
| Date Signed (for bilateral usually same as date adopted, for multilateral country specific) | text | Legacy (v1), hidden, not exported. Country-specific dates belong in the Participation database; the instrument's date is Opened for Signature. |
| Did the states agree to change current behavior or just not take actions that they might have considered in the future? | text | Legacy (v1), hidden. The 2021 question whether states changed current behaviour or only forwent future actions; origin of Paper 2's focus on what states give up. Replaced by Behavior Change Required. |
| For US; President + Party at the time | text | Legacy (v1), hidden. From the 2021 question whether agreements were signed by governments of the left or right: a domestic-politics explanation. Not carried into v2; belongs in the Participation database. |
| Type (Bilateral vs Multilateral) | select | Legacy (v1), hidden, not exported. Replaced by Participation Structure. |
| Type (Conventional, WMD, Nuclear, Chemical, Biological, IHL, Conduct in War) | multi_select | Legacy (v1), hidden, not exported. Replaced by Weapon Families and Legal Subject Matter. |
| Geographic Scope | select | Legacy (v1), hidden, not exported. Replaced by Region and Operating Environment. |
| Great-Power Parties | multi_select | Legacy (v1), hidden. From the 2021 questions on great-power pressure to join and who lost out. Why: whether great powers were inside an agreement. Not in v2; derivable from the Participation database. |
| Signatories & Dates | text | Legacy (v1), hidden, not exported. Free-text participation list; belongs in the Participation database. |
| Notable Withdrawals/Suspensions | text | Legacy (v1), hidden, not exported. Replaced by withdrawal and suspension events in Treaty Events. |
| Treaty ID | text | Legacy (v1), hidden, not exported. Old identifier; replaced by Record ID. |
| Adopted at: | multi_select | Legacy (v1), hidden, not exported. Place of adoption stored as select options; the place goes in the events and the page text. |
| References to other treaties/international law | text | Legacy (v1), hidden. Replaced by the relations Protocol To, Amends, Replaces and Negotiated Alongside. |

## Relations, formulas and identifiers (no hover description in Notion)

These cannot be given descriptions safely through the Notion connector, because redefining a relation or formula could break it; they are documented here instead.

- **Provisions.** Rows in Treaty Provisions belonging to this instrument.
- **Events.** Rows in Treaty Events belonging to this instrument.
- **Editorial Log.** Internal log entries for this instrument; never exported.
- **Protocol To / Has Protocols.** Links a protocol to its parent instrument; coded on the later (protocol) record only.
- **Amends / Amended By.** Links an amendment to the instrument it amends; coded on the later record only.
- **Interprets / Interpreted By.** Links an agreed interpretation to the instrument it interprets, following the parties' own characterization; coded on the later record only.
- **Replaces / Replaced By.** Links an instrument to its predecessor; coded on the later record only.
- **Negotiated Alongside / Negotiated Alongside (reverse).** Instruments concluded together at the same conference or in the same package (for example the Washington Conference treaties).
- **Produced / Produced By.** Links a conference or negotiation record to the instrument it produced.
- **Treaty Participation Database 1.** State-level participation rows.
- **Countries Database.** Countries associated with the instrument.
- **Articles.** Articles database entries discussing the instrument.
- **News Tracker.** News items about the instrument.
- **Strategic Systems.** Military Systems rows the instrument limits or bans (the relation keeps its old name).
- **Nuclear Fundamentals.** Nuclear Fundamentals rows that explain or cite the instrument.
- **Year Adopted (formula).** Year taken from Date Adopted; used in the Browse view and the website.
- **Era (formula).** Period grouping. Its definition could not be read through the connector on 11 October 2026; check the formula in Notion before relying on it.
- **Slug (formula).** Web address segment for the public page.
- **Record ID (auto ID).** Stable identifier (AC-n) used for relations in coding; never reused.
- **Treaty Name (Full) (title).** Official full title of the instrument.
- **Amendment procedures (legacy select).** Legacy (v1), hidden, not exported; replaced by Amendment Procedure and Amendment Clause. Left without a hover description because one option is a pasted paragraph containing a line break, and re-listing the options could detach rows that use it.

## Origin: the 2021 research design

The project began in July 2021 as a spreadsheet with Robert Trager coding about 78 agreements. Its questions, several of which survive as legacy fields and as the motivation for current ones: what arms were limited; whether the agreement limited use, development or stockpiling, and precursor technologies or materials; whether limits were to zero or to a level; whether states changed current behaviour or only forwent future actions; who agreed when; whether agreements were signed by governments of the left or right; whether the sides could monitor compliance; whether agreements were adhered to, and whether they had a positive effect even if not fully observed; the reason for agreeing (fear that rivals would build if they built, pressure from larger powers, or something else); whether events that harmed several sides triggered the agreement or it was adopted prospectively; whether larger powers pressured others to join, and their protégés in particular; who lost out most, and whether larger powers' interests were preserved; and whether, if one side complied and the other did not, the balance of power would shift enough that the complier would be less likely to survive a conflict or face much higher costs, judged from contemporaries' views or from the existence of substitutes. The last question is the origin of Paper 2's condition. On 11 October 2026 every row of the sheet (78 agreements, including Robert Trager's comment on the St Petersburg Declaration) was migrated verbatim into the Treaty Editorial Log as "Earlier notes (unchecked)" entries, one per instrument, with the text in the page body; the sheet itself was then deleted. The analytical answers are unsourced working notes: treat them as leads, never as sources. The writer updates only log-entry properties, so these bodies survive reruns.

## Known gaps (11 October 2026)

- The database-level description in Notion could not be set through the connector (the call returned normally and saved nothing, twice); this file is the database description.
- The Era formula's definition is unrecorded (above).
- The 13 September 2026 issues list (`2026-09-13 - Treaty Database Issues to Fix.md`) still applies to v1 property names that carry instructions in parentheses; renaming them would be a schema change for the v2 rebuild.

## Coding specification (SPEC_v3)

Verbatim copy of the agents' coding specification as of 2026-10-11 21:37. The working file lives in the pilot session's temporary scratchpad; this copy is the durable one.

---

# Coding spec v2: one arms-control record

You research ONE record and write ONE JSON file. Do not write to Notion. Read the record's current Notion page first (Notion fetch tool) to see what is recorded, then verify and correct.

## Evidence rules
- Every value must rest on the treaty text, the depositary record, an official document, or (for history only) a reputable scholarly or institutional source. Prefer primary sources.
- If you cannot verify a value, use null and list it in `unverified` with the reason. Never guess. Missing evidence is never a "No".
- For Yes/No fields use: "Yes", "No", "Not specified in text", "Not applicable", or "Not yet checked". Use "No" only when the text clearly excludes it.
- Prose: formal register, plain English, no em dashes, no hype. Cite articles ("Art. 5(2)"). Text fields under 1,900 characters.
- Compliance: record events with attribution ("The United States alleged...", "Russia denied..."); never give an unqualified verdict of your own.
- Use ONLY the allowed values listed below.

## Output: write the JSON to the path given in your task, then reply with one line: "saved: <path>"

```
{
 "instrument": {
  "full_name", "short_name",
  "record_type": Instrument | Regime | Initiative | Negotiation | Conference,
  "instrument_form": Treaty/Convention | Protocol | Amendment | Exchange of Notes | Executive Agreement | Memorandum of Understanding | Concluding Act | UN Security Council Resolution | UN General Assembly Resolution | Declaration | Code of Conduct | Guidelines | Not applicable,
  "legal_character": Legally binding | Politically binding | Contested | Not established,
  "instrument_status": In force | Not yet in force | Never entered into force | Expired | Terminated | Superseded | Suspended (whole instrument) | Not applicable,
  "negotiation_status": Concluded | Ongoing | Stalled | Abandoned | Not applicable,
  "date_adopted", "opened_for_signature", "entry_into_force", "date_ended"  (YYYY-MM-DD or null),
  "participation_structure": Bilateral | Plurilateral (closed) | Multilateral (open) | Unilateral,
  "geographic_coverage": subset of [Europe, North America, Latin America & Caribbean, Africa, Middle East, Asia, Pacific, Arctic, Antarctica] ([] if worldwide),
  "operating_environment": subset of [Land, Sea, Seabed, Air, Outer space, Celestial bodies, Not specific],
  "weapon_families": subset of [Nuclear weapons, Fissile material, Chemical weapons, Biological weapons, Missiles & delivery systems, Missile defence, Naval forces, Ground forces & equipment, Air forces, Military personnel, Small arms & light weapons, Landmines, Cluster munitions, Incendiary weapons, Blinding lasers, Non-detectable fragments, Explosive remnants of war, Space & orbital weapons, Autonomous weapons, Fortifications & bases, All weapons (zone)],
  "legal_subject_matter": subset of [Arms limitation & disarmament, Nonproliferation, Conduct of hostilities (IHL), Arms trade & transfer control, Risk reduction & CBMs, Demilitarization & zones, Testing, Nuclear security],
  "signed_at", "adopted_at", "depositary",
  "number_of_parties", "number_of_signatories", "parties_as_of" (date of the count; counts are a snapshot, the authoritative record will be the Participation database),
  "key_non_parties" (text),
  "information_provisions": subset of [Declarations & data exchange, Notifications, Periodic reports, None],
  "inspection_access": subset of [Routine on-site inspection, Challenge inspection, Continuous monitoring, Observation flights, Fact-finding mission, None],
  "monitoring_means_specified": subset of [National technical means, Non-interference with NTM, International monitoring system, Cooperative measures, None specified],
  "institutional_oversight": International organization | Treaty body or commission | Depositary only | None,
  "consultation_mechanism": Standing commission | Consultative meetings | Review conferences only | Diplomatic channels only | None,
  "reporting_requirements", "enforcement", "dispute_resolution", "national_authority", "technical_cooperation", "third_party_roles": Yes/No values above,
  "reservations": Allowed | Prohibited | Limited | Not Specified,
  "duration_type": Indefinite | Fixed term | Fixed term (renewable) | Until obligations met | Not specified, "duration_years", "duration_clause",
  "extension_type": None stated | Automatic | By agreement of parties | By review conference | Other, "extension_clause",
  "withdrawal_type": None stated | Notice | Supreme interests (with notice) | Mutual consent only | Other, "withdrawal_notice_months", "withdrawal_clause",
  "amendment_procedure": None stated | Consensus | Unanimity | Two-thirds majority | Simple majority | Other, "amendment_clause",
  "review_conferences": None | Periodic | Ad hoc / on request, "review_interval_years", "review_conferences_held" (integer: formal review conferences only, not meetings of states parties),
  "entry_into_force_requirements",
  "number_of_articles", "word_count", "count_basis" (text: which text/language/annexes and how counted),
  "weapons_systems_limited" (1-2 sentences), "key_provisions" (concise, article-cited),
  "behavior_change" (text), "historical_background" (3-5 sentences),
  "treaty_url" (official text), "source_quality": Official text | Reproduction | Secondary only | Not found,
  "related": list of {"relation": protocol_to | amends | replaces | negotiated_alongside | produced_by, "target": "name of the other instrument"}
 },
 "provisions": [ one object per distinct restriction:
   {"provision": short label, "article", "weapon_activity": [weapon_families values],
    "restriction_type": Prohibit use | Prohibit development | Prohibit production | Prohibit acquisition or possession | Prohibit stockpiling | Prohibit testing | Prohibit deployment or stationing | Prohibit transfer | Numerical ceiling | Reduction or elimination | Freeze | Demilitarized zone or area | Notification or transparency | Other,
    "value" (number or null), "unit", "bound_parties": All parties | Some parties (asymmetric) | Specific named party, "bound_parties_detail",
    "geographic_scope", "exceptions", "effective_from", "effective_until", "text_or_paraphrase", "source_url", "locator"} ],
 "events": [ dated events, oldest first:
   {"event": short label, "date", "effective_date",
    "event_type": Adoption | Opening for signature | Entry into force | Withdrawal notice | Withdrawal effective | Suspension by a party | Suspension of instrument | Denunciation | Termination | Expiry | Superseded | Amendment adopted | Amendment in force | Review conference | Negotiation round | Compliance allegation | Compliance response | Institutional finding | Acknowledged breach | Remedy or resolution | Other,
    "actors", "attribution" (who reports or asserts it), "description", "source_url", "locator"} ],
 "section_provisions_md": Markdown (no top heading) for "Provisions and obligations", 300-700 words, ### subheads and bullets,
 "section_history_md": Markdown (no top heading) for "History, compliance and sources", 300-700 words, ending with a ### Sources list of Markdown links,
 "unverified": [ {"field", "reason"} ],
 "corrections": [ text notes on errors found in the existing Notion row or page ]
}
```

Guidance: a provision is one restriction on one activity (e.g. "Prohibit testing of nuclear weapons in the atmosphere"). Events should include adoption, opening for signature, entry into force, withdrawals and suspensions (notice and effective dates separately), amendments, review conferences, and attributed compliance events. For negotiations, use "Negotiation round" events for key sessions and mandates. For political arrangements, legal_character is "Politically binding" and there is no entry into force.

# v3 additions (after the five-record pilot, 11 Oct 2026)

## Codebook definitions for the Yes/No fields
- reporting_requirements: Yes if parties must submit declarations, data or periodic reports to another party, a body or the depositary.
- enforcement: Yes if the text provides consequences for non-compliance beyond consultation (sanctions, suspension of rights, referral to the UN Security Council).
- dispute_resolution: Yes if the text specifies a procedure for disputes over interpretation or application (a standing body, consultation procedure, arbitration or the ICJ).
- national_authority: Yes if the text requires each party to designate, establish or use a national body, focal point or centre for implementation or communication.
- technical_cooperation: Yes if the text provides for assistance or the exchange of technology or expertise among parties.
- third_party_roles: Yes if the text assigns functions to a non-party (an international organization, the UN Secretary-General beyond custody, observers, basing states, non-parties that may accept the instrument).
Every Yes or No that is not obvious from a single article gets a coding note naming the article and the definition it meets.

## Dates
- Use YYYY-MM-DD only when the source gives the day. If only a month or year is known, set "date": null, "date_precision": "Month" or "Year", and "date_as_reported": "October 2000". If unknown, "date_precision": "Date unknown". Never fill in a day to make a date sortable.
- Every count (parties, signatories) carries the date it was counted, and coding notes state how succession or special statuses were treated.

## Related instruments
Use the attached rows list (Record ID, title, abbreviation, aliases). Give "target_id": the Record ID (e.g. "AC-44"). If the related instrument has no row, set "target_id": null and "missing": "<full name>"; it goes to the missing-instruments list, not into prose as if linked. Direction: protocol_to, amends and replaces are coded on the later instrument only.

## Explicit nulls
If you return null for a field that the current Notion row has populated, say why in corrections; the writer clears it.

## Page sections (Markdown, no top heading), replacing section_provisions_md / section_history_md
- overview_md: one paragraph (what it does, who is covered, status, significance).
- provisions_md: obligations grouped by subject, article-cited, with exceptions and bound parties. Rename the section where the instrument warrants it ("Commitments" for political instruments; "The negotiating mandate" and "Open questions" for negotiations).
- participation_md: how states join, entry into force, duration (including any shorter duration of particular rights), withdrawal, amendment, review, depositary.
- history_md: narrative; compliance events attributed and labelled as allegation, response, finding, suspension or withdrawal.
- sources_md: Markdown links.
- coding_notes: list of {"field", "note"} for substantive public explanations only.
- research_notes: process items (blocked sites, inferred page numbers); internal only.
Key facts are generated from properties by the writer; do not write them.

## Editorial material
corrections, research_notes and the old page text go to the Treaty Editorial Log (internal) database, never into the public page body.

## Writer behaviour (tested on the five pilots, 11 Oct 2026)
- null or omitted = leave the existing value. Only entries in "clear_fields": [{"field", "reason"}] erase a value; the reason is logged.
- Provision rows are matched on (provision, article) and event rows on (event, exact date); matches are updated in place, new ones created, and only rows absent from the new output are archived. Relations are written as whole lists. Log entries are one per instrument and type, updated in place. Reruns therefore create no duplicates.
- Key facts are regenerated on every write; resync_all_keyfacts() refreshes them after manual property edits.
- Counts always carry "Parties As Of".

## Website export allowlist
Public: the v2 properties shown in the "All Treaties" view (plus Parties As Of, Year Adopted, Slug), the page body, and the Treaty Provisions and Treaty Events rows (excluding Locator if desired).
Never exported: the Treaty Editorial Log database and the "Editorial Log" relation; all v1 properties (Status, Legal Form, Type of Weapons, Type of Limitation, Quantitative Limits, Verification Mechanism, Compliance History, Duration, Extension provisions, Withdrawal Provisions, Amendment procedures, Review Conference Schedule, Sunset clauses, Date Ratified, Date Signed, Did the states agree..., For US; President..., Type (Bilateral vs Multilateral), Type (Conventional...), Geographic Scope, Great-Power Parties, Signatories & Dates, Notable Withdrawals/Suspensions, Treaty ID, Adopted at:); internal flags (In Paper 2 Appendix, Vaynman fields, Last Verified, Source Quality optional).

## Rules added after Codex's pilot review (REVIEW.md, 11 Oct 2026)
1. Keep qualifications in every representation. After any correction, recheck the property, the generated key facts, the page prose and the rows.
2. Coding basis. For each Yes/No and final-clause field, state in coding_notes whether the code comes from the instrument's own text, an applicable parent instrument (e.g. CCW articles for a Protocol), or a later decision of the parties. Public filters read "required by instrument text".
3. Display labels by instrument (the writer maps these; the schema is unchanged): bilateral treaties show "Signed"; politically binding instruments show "Operative", "Participating states", "Code text" and "Institutional arrangements"; negotiations show "no agreed treaty text".
4. Optional access is not compulsory access: code voluntary observation as "Voluntary observation", never as inspection.
5. No universal negatives from an incomplete search: write "no formal finding was identified in the sources reviewed".
6. Every substantial historical claim carries a nearby source link; use "reported by" when the publication consulted differs from the actor. Claims based on sources the agent did not retrieve are omitted or explicitly qualified, never stated as settled.
7. Provision granularity: one row per distinct obligation on one activity for one class of party (split paired commitments only when they bind differently). Rows are a browsing aid, not a measure of treaty depth; the Value column holds heterogeneous quantities (ceilings, deadlines, quotas, notice periods) and its Unit must always say which.
8. Dates: distinguish event dates, document dates, deadlines and scheduled dates; when a date is only a scheduled or publication date, say so in "date_as_reported" rather than presenting it as the event date.
9. Bound parties: "Some parties (asymmetric)" only for a legally unequal obligation; different named systems or facilities under the same obligation are "All parties".
10. Source quality for negotiations without text: "Not applicable (no concluded treaty text)".
11. Editor guidance stays off the public page (the "edit the properties" note is gone); key facts are still regenerated on every write.

## Related instruments: main entry first (revised 11 Oct 2026 after Codex's second ruling)
- The main unit is the agreement readers recognize. One main record per agreement explains its original restrictions and how it was later interpreted, amended or applied.
- An exchange or instrument that interprets, applies or adjusts an existing agreement is recorded on the parent: events for each exchange (dated, sourced) plus a "Later interpretations" (or "Later amendments") passage giving dates, who agreed what, sources and what each changed.
- A separate supporting record is created only when structured comparison actually needs it (for example its own provisions must be filterable). It gets Record Type "Supporting instrument", the relation to its parent (interprets, amends, protocol_to), and is excluded from the default views and from headline treaty counts.
- Instruments with their own parties, ratifications and obligations (e.g. CCW Protocols) remain main records, related to the framework by protocol_to.
- An exchange of notes is never split into one record per note. Form ("Exchange of Notes") and relationship ("interprets", "amends") stay separate; follow the parties' own characterization.
- Code the parent's provisions against its original text; describe later changes in prose and events (or on the supporting record, if one exists).
- Counting rule: headline counts exclude Record Type "Supporting instrument" and count related instruments separately from independent agreements.

## Participation and publication (decided 11 Oct 2026)
- Participation is the authoritative country relationship: one row per state per instrument, with Date Signed kept apart from Entry into Force (becoming bound). Unknown dates stay blank and are explained in Notes; a blank end date with no Current Status means "not established", never "still participating". Succession is described in Notes; a succession act, date or method is coded only when documented, never inferred from independence milestones. Every row carries its sources and a short qualification.
- The direct Instruments-to-Countries link is not filled for new records; existing direct links are preserved until migrated to Participation.
- Publication: Notion is the editorial workspace; the public site is built from a website export with an explicit field list. Public provenance may include Source Quality, Last Verified and dataset crosswalks (Vaynman code and category); the Editorial Log, its relation and the In Paper 2 Appendix flag stay internal. Working pages are not published directly through Notion.
- Content Complete (internal checkbox) is ticked only after the record is researched, checked, written, reviewed and has its participation rows; the website export publishes only ticked records.

## Rules added after the St Petersburg review (11 Oct 2026)
- Date Adopted is formal adoption of the text: a conference's adoption act or, where none exists, the signature that concluded the instrument. Preparatory approval of wording by a commission or committee is an event, not adoption.
- The key-facts signature label follows the recorded events: "Opened for signature" only when an Opening for signature event exists; otherwise "Signed". Never infer the label from adoption and signature sharing a date.
- Counts: Number of Parties is a current-party count and is left blank when present-day participation is unresolved; a historical participant count (signatories plus accessions, with the date the list was checked) is generated from the Participation rows and labelled as historical.
- Accessions are typed: Method of Consent "Accession", Participation Type "Non-Signatory Party", Date of Accession set; never put an accession in Date Signed or invent a separate entry-into-force date. "Acceded" is an action, not a current-status assessment.
- Thresholds stay exact in every representation ("less than 400 grammes"; "excludes 400 grammes or more"); coverage defined by weight or contents is not restated as a weapon category.
- Historical entities: add or reuse historical Countries entries (Status Inactive/Historical, no successor coded) for real historical states and link them. Historical names (e.g. Persia), composite representation labels (e.g. Prussia and the North German Confederation) and historical unions (e.g. Sweden and Norway) keep their source label on the Participation row, are counted once, are not forced into a country record, and may stay unlinked.
