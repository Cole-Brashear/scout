# Application site traps

An ATS (applicant tracking system) is the software behind a company's application form. Each one has its own traps. Entries marked **field-tested** were confirmed on real applications; the rest are general knowledge to verify. When you hit a new trap, add a line to "Site notes" at the bottom of the user's `tracker.md` so the next session knows.

## General

- Before any risky step (an upload, a page change, a long pause), read every field value out with a script so a wipe can be refilled exactly. **Field-tested.**
- Some browser tools block script output that looks like cookies or query strings. Strip ids and punctuation from what you print. **Field-tested.**
- Opening a new window from inside the built-in browser pane can replace the tab and wipe the form. Use Claude in Chrome. **Field-tested.**

## Greenhouse (job-boards.greenhouse.io, boards.greenhouse.io)

- Upload on the Resume "Attach" input works and doesn't overwrite other fields. **Field-tested.**
- Single-select dropdowns: click, type, wait a moment, press Return. Some options need a direct click on the option. **Field-tested.**
- Multi-selects (like locations) close after each pick: click, type one value, Return, Escape, repeat. **Field-tested.**
- The phone country picker displays as "+1". **Field-tested.**
- A long idle can reload the whole form. Check it's still filled before handing over. **Field-tested.**

## Ashby (jobs.ashbyhq.com)

- No account needed. Yes/No questions are buttons; checkboxes and radios are normal. **Field-tested.**
- Upload on the Resume input works. **Field-tested.**

## Lever (jobs.lever.co)

- No account needed. One page. Resume upload may autofill name, email and phone; check them after.
- "Additional information" is a free-text box; a short, specific note beats a pasted cover letter.

## Workday (myworkdayjobs.com)

- Needs a separate account for every company. The user creates it.
- "Autofill with resume" fills the My Experience page and often garbles it: split or merged jobs, wrong dates, descriptions dumped into the wrong field. Check every entry.
- Dropdowns are searchable: type, then pick the option from the list. Many date fields want MM/YYYY typed in.
- Several pages, each with its own Save and Continue. Errors only show when you try to continue.

## SAP SuccessFactors (career*.successfactors.com)

- Needs an account; the user signs in. **Field-tested.**
- To upload, click the small "+" under the Resume tile (not the tile itself), then upload on the input it reveals. **Field-tested.**
- **Uploading a resume re-runs a parser that wipes the whole form**: education details, certifications, languages, relocation answers and every job-specific answer. It rebuilds the job rows and re-sorts them by date, so verify by company name, not row order. Upload first, fill after. **Field-tested.**
- Dropdowns don't commit on type plus Enter. What works: click the input, type a filter, then dispatch mouseover, mousedown, mouseup and click on the visible option with exact text, then read the value back. Retry after 2 seconds if no option appears. **Field-tested.**
- **Sessions expire after about 30 minutes idle** and lose everything unsaved. Click "Keep Working" whenever it pops up, and have the user submit right after filling. **Field-tested.**
- The resume in "My Documents" is shared across every application on that company's site. Finish and submit one application before swapping in another role's resume. **Field-tested.**

## Avature (*.avature.net)

- Some company domains for Avature boards serve broken certificates. The same board is usually reachable at `<company>.avature.net/en_US/careers/SearchJobs/<keywords>`. **Field-tested.**

## iCIMS (*.icims.com)

- Usually needs an account. The form often runs inside a frame, so read and fill inside that frame.
- Resume parsing fills fields; check each one.

## LinkedIn

- Filtered `/jobs/search/` URLs redirect to AI search. Use `/jobs/search-results/?keywords=<natural-language query including location>`. **Field-tested.**
- Descriptions lazy-load only after a real scroll. **Field-tested.**
- Job pages show "People you can reach out to" (alumni and connections). **Field-tested.**
- The job tracker is at linkedin.com/jobs-tracker; change a stage with the card's ⋯ menu, then Change stage. **Field-tested.**
- Easy Apply sends the profile and resume on file. Make sure the tailored resume is selected before the user submits.

## Handshake

- The user signs in through their school. Many employers there recruit only at specific schools, so its listings are often less crowded.

## Resume PDFs on a Mac

- Pages and Word scripting can fail to export from inside ~/Desktop or ~/Documents (sandbox errors). `resume.py pdf` works around this by converting in a temporary folder and copying the PDF back. **Field-tested.**
