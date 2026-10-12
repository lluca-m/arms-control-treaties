# Review of the five treaty database pilots

11 October 2026. Review of the exported properties, page bodies, provision rows, event rows and internal editorial logs. Source exports and Notion were not changed.

**Decision: approve the page architecture and depth; fix the issues below before the full run.** These should remain substantial reference pages. The structured properties support searching and comparison; the prose explains scope, exceptions, operation and evidence. Reducing the prose would conceal qualifications that the properties cannot carry.

All exported row counts match the reported pilot counts:

| Record | Provisions/commitments | Events |
|---|---:|---:|
| INF | 40 | 23 |
| CCW | 2 | 18 |
| CCW Protocol IV | 3 | 13 |
| HCoC | 12 | 15 |
| FMCT | 0 | 13 |

## Corrections before scaling

### 1. INF: make the summaries as precise as the detailed rows

Locations: INF.md lines 32, 89–100, 186, 190.

- The intermediate-range category is **over 1,000 through 5,500 km**, not an interval including 1,000. The detailed elimination row gets this right; the core-obligations heading does not.
- The permanent-ban summary extends flight-testing to stages and launchers. Distinguish the ban on producing missiles, stages and launchers from the ban on flight-testing missiles; shorter-range missiles also have a launch prohibition.
- The properties describe thirteen years of baseline, closeout and elimination inspections. Attach thirteen years specifically to short-notice inspection and continuous monitoring; the other inspection categories have different triggering events and periods.
- The location summary should preserve the thirty-day start for production-facility/test-range restrictions and the elimination-facility exception to the facility freeze. The detailed rows already do much of this.
- Rows 26 and 30 label the obligations “Some parties (asymmetric)” while describing requirements/rights applying to both parties. Different named missiles or facilities do not by themselves make an obligation legally asymmetric. Use “All parties” unless a specific unequal obligation is identified.

Checked against the [treaty text, especially Articles II, VI, VIII, X and XI](https://nuke.fas.org/control/inf/text/inf.htm). These are summary/coding repairs, not grounds to remove the detailed explanations.

### 2. CCW: date precision still fails in one event

CCW.md line 180 dates “Financial shortfall curtails meetings” **2017-07-01 / Exact day**, while its description explicitly says only the report month is known. Use **July 2017 / Month** for the report, with a title identifying it as reporting on cancellations. Do not silently use publication month as the date the cancellation decision occurred.

The same rule should distinguish event dates, document dates, deadlines and scheduled dates. FMCT's final event, for example, uses a scheduled session-closing date to date a claim about the session's outcome. Keep that basis visible, or obtain the closing record.

### 3. CCW: repair event-level source support

CCW.md lines 178–179 cite an October 2011 “Protocol Status Uncertain” article for the November conference outcome, and a “conference begins” article for the December 2016 final decision. These are suspect source-to-claim matches, not evidence that the outcomes themselves are false. The linked pages could not be retrieved in this check; do not certify them from their titles. Replace or supplement them with the relevant final documents/outcome records.

Protocol IV's review-conference events similarly link to a treaty participation-status page rather than the conference records. Its internal log explicitly says those dates were not rechecked. Reuse verified conference sources across the two records instead of separately generating the same history.

The 2006 compliance-mechanism date is supported by the [Third Review Conference final document, Part I](https://unoda-documents-library.s3.amazonaws.com/Convention_on_Certain_Conventional_Weapons_-_Third_Review_Conference_%282006%29/CCW%2BCONF.III%2B11%2BPART%2BI%2BE.pdf), recording adoption on 17 November. Keep that correction.

### 4. Protocol IV: repair the definition and the verification status of background claims

CCW Protocol IV.md line 28 says visual acuity below 20/200 “in both eyes.” The body correctly says measured with both eyes. Use **“measured using both eyes”** consistently: this should not become a separate-eye threshold. [Protocol IV, Article 4](https://www.icrc.org/sites/default/files/external/doc/en/assets/files/other/icrc_002_0467.pdf).

More importantly, the internal log at lines 252–253 says conference dates and prominent historical claims were based on accounts known to the coder, with the specific background sources not retrieved. They nevertheless appear as settled public facts. Retrieve the cited passages or omit/qualify those claims before publication. “Official text” source quality verifies the instrument, not every historical statement on the page.

I checked the depositary status page: it reports 111 parties and supports the listed Finnish, Hungarian, US and Trinidad and Tobago notification dates. [UN Treaty Collection](https://treaties.un.org/Pages/ViewDetails.aspx?src=TREATY&mtdsg_no=XXVI-2-a&chapter=26&clang=_en).

### 5. HCoC: align history and preserve the qualification on non-assistance

HCoC.md lines 55 and 112 place the replacement of “obligations” with “general measures” at Madrid. Its February 2002 event correctly puts that revision at **Paris**, as does the [official chronology](https://www.hcoc.at/what-is-hcoc/hcoc-chronology.html). Correct the property and narrative together. The property also calls UN resolutions biennial since 2004, although the page itself lists both 2004 and 2005; say “successive General Assembly resolutions.”

The overview abbreviates the non-assistance commitment to programmes in states that may seek WMD. Preserve its qualification concerning contravention of international disarmament/non-proliferation norms and obligations; it is not a blanket prohibition on assistance to every WMD-possessing state. The detailed commitment row has the fuller formulation. [Official Code, section 3(e)](https://www.hcoc.at/what-is-hcoc/text-of-the-hcoc.html).

The 145 subscribers and May 2026 meeting are supported by the [official meeting press release](https://www.hcoc.at/sites/default/files/documents/Adopted%20Press%20Release%2025th%20ARM%202026.pdf).

### 6. FMCT: separate absent treaty text from missing evidence

FMCT.md lines 33 and 101: **“Not found” is the wrong source-quality value.** There is no concluded treaty text to find; there are official mandate and process documents. Use “Not applicable — no concluded treaty text” for treaty-text availability, and retain official-source provenance for the mandate. Likewise, “no agreed text” in Key facts should be “no agreed treaty text.” Keep zero provision rows.

Avoid the categorical “formal negotiations have never begun” without defining it. The 1998 negotiating committee existed and met: its report records two meetings, and the [2000 NPT conference record](https://digitallibrary.un.org/record/424969/files/NPT_CONF.2000_28%28PartIII%29-EN.pdf) describes its exchange of views as a first step in substantive negotiations. Prefer: **“No treaty has been concluded. A negotiating committee met briefly in 1998, but sustained negotiations have not followed.”** This supports “Stalled” without litigating whether a preliminary meeting counts as beginning negotiations.

Change “the five NPT nuclear-weapon States other than China” to “four of the five…” for clarity. Label the assessment that a treaty would “mainly constrain” particular states as analysis contingent on production, verification and scope; converting unilateral restraint into an obligation can matter even without an immediate change in production.

## Shared rules for the writer and public presentation

1. **Preserve evidentiary qualifications in every representation.** Correcting a provision row is insufficient if the property and generated prose retain the broader claim. Recheck all three after a correction.
2. **Make the coding basis visible.** CCW properties describe the original framework text; the page also describes later compliance arrangements. Label the filter/field “Reporting required by instrument text,” or otherwise expose its basis, so a public “not specified” result is not mistaken for a statement about current operation. Protocol IV also inherits some framework procedures. Identify whether a code comes from its own text, an applicable parent instrument, or a later decision.
3. **Use labels appropriate to the instrument.** HCoC already has “Participating states” and “Commitments”; extend that to “Operative,” “Code text” and “Institutional arrangements” rather than “In force,” “Treaty text” and “Treaty body.” INF should display its bilateral signing as “Signed,” not an opening for signature. These can be display mappings rather than wholesale schema changes. “Key Non-Signatories” is also misleading where the field describes non-parties or non-subscribers.
4. **Keep optional access distinguishable from no access.** HCoC has no mandatory inspection, but it contemplates voluntary observer invitations. Its “Inspection & Access: None” should specify the absence of required access and preserve the optional provision for filtering. Do not recode voluntary observation as compulsory verification.
5. **Do not turn an incomplete search into a universal negative.** CCW's “no formal compliance finding has been made” and HCoC's “no formal compliance findings exist” require a defined search basis. Prefer “No formal finding identified in the sources reviewed,” where warranted. HCoC's non-public submissions limit public assessment; they do not establish that implementation cannot be assessed from any official source.
6. **Retain usable citations.** All four instrument Key facts tables contain plain “Treaty text,” without a hyperlink in the export. Check whether the exporter dropped rich-text links or the writer omitted them; either way, public exports need an actual link. Add nearby source links to substantial historical claims, not just an undifferentiated bibliography. Use “reported by” where an event's named actor differs from the publication actually consulted.
7. **Define provision-row granularity.** INF mixes individual prohibitions, grouped notifications and multi-rule inspection procedures; HCoC separates some paired commitments. This is usable for browsing, but the counts are not comparable measures of treaty depth or complexity. Define the inclusion/splitting rule before the full run, preserve qualifications, and do not treat the numeric Value column as a common quantitative limit: it includes deadlines, notice periods, inspection quotas and force ceilings.

## Layout verdict

Keep the overview, compact key facts, substantive explanation, participation/legal operation, attributed history, expandable detailed rows, and sources/coding notes. FMCT's different headings and HCoC's commitments language are appropriate. Keep coding reasons beside the relevant evidence. Retain detail behind expandable sections rather than deleting it.

Move “edit the properties, not this table” into editor-facing guidance. The public facts table should show short values and link readers to fuller explanation. The long properties table is an editorial/data-export view, not a second required public introduction.

Appendix C is correctly marked internal in these review exports. A production exporter must exclude that section and the editorial database; a heading saying “not public” is not itself an access control.

## Scope and completion check

I read all five exports and checked their stated counts. External checks were targeted, including INF treaty clauses, the HCoC text/chronology/2026 release, Protocol IV text and depositary record, and UN records for the CCW mechanism and the 1998 FMCT process. This is not independent verification of every historical statement or every event's source.

The exports cannot demonstrate working Notion filters, mobile rendering, relation targets, access permissions, or safe reruns of the writer. The agent specification and writer were not included in this folder. After the corrections, rerender these five first; verify that generated facts agree with properties, corrected blanks stay clear, row counts do not grow on rerun, and the public view excludes editorial history. Then proceed to the full run. No redesign or additional reduction in page depth is needed.
