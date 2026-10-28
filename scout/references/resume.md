# Tailoring the resume

Each tailored resume tells the story from the research brief (section A) using only facts from `facts.md`. Rewriting freely is fine: reorder sections, rewrite or cut bullets, rename section headings, as long as every line stays true.

## Rules

- **Every line traces to `facts.md`** or to something the user confirmed in chat this session (save it to `facts.md` right away). No invented numbers, tools or titles. If they asked to keep something general, write it without numbers.
- **Lead with the strongest proof for this role.** The top third of the page is what a recruiter reads in their first few seconds.
- **Mirror the posting's language where it's honest** (brief section C). Applicant tracking systems and recruiters both scan for the posting's own words.
- **One page** for students and new grads.
- **No summary or objective line** unless the user wants one. For new grads it usually takes space that proof should fill.
- **Strong bullets:** start with a verb, say what changed, include the number. "Ran 12 events for 40-80 attendees" beats "Responsible for event planning".
- **Never edit the base resume** in `resumes/base/`. Every tailored version is a new file.
- **Name files for the recruiter:** `First-Last-Resume-Company-Role.pdf`. They see the filename.

## Building it

`scripts/resume.py` has two modes.

**Clone mode** keeps the user's own formatting. Use it whenever the base resume is a .docx laid out in normal paragraphs.

1. Inspect the base once:

   ```bash
   python3 <skill-dir>/scripts/resume.py dump resumes/base/Jane-Doe-Resume.docx
   ```

   It prints every paragraph with its index, style and runs (stretches of text with the same formatting), and warns if the layout uses tables or text boxes, which clone mode can't rebuild. Pick one example paragraph for each kind of line: section heading, entry line (organization, location, dates), title line, bullet, skills line. Note this map in `resumes/specs/README.md` so later sessions don't redo it.

2. Write a spec at `resumes/specs/<Company-Role>.json`:

   ```json
   {
     "base": "resumes/base/Jane-Doe-Resume.docx",
     "out": "resumes/Jane-Doe-Resume-Acme-Analyst.docx",
     "keep": 2,
     "like": {"section": 2, "entry": 3, "title": 4, "bullet": 5, "skills": 30},
     "blocks": [
       ["section", "EDUCATION"],
       ["entry", "University of Somewhere", ", Denver, CO", "\tMay 2027"],
       ["title", "B.A. Economics, GPA 3.7"],
       ["bullet", "Dean's List (2024-2026)"],
       ["section", "EXPERIENCE"],
       ["entry", "Acme Corp", ", Remote", "\tJune 2026 - August 2026"],
       ["title", "Operations Intern"],
       ["bullet", "Cut weekly reporting time from 6 hours to 1 by automating the inventory sheet"],
       ["skills", "Tools: ", "Excel, SQL, Tableau"]
     ]
   }
   ```

   - `keep`: how many paragraphs at the top to keep untouched (usually name and contact lines).
   - `like`: which base paragraph each kind of line copies its formatting from. A block can also name an index directly, like `[12]`.
   - Each block is `[kind, run 1 text, run 2 text, ...]`, matching the runs `dump` showed for that example paragraph. In the example above, the entry paragraph's runs are a bold organization, the location, and a tab plus the dates. A block with no text keeps the example's text as-is, which is handy for spacer lines.

3. Build and export:

   ```bash
   python3 <skill-dir>/scripts/resume.py build resumes/specs/Acme-Analyst.json
   python3 <skill-dir>/scripts/resume.py pdf resumes/Jane-Doe-Resume-Acme-Analyst.docx
   ```

   `pdf` tries LibreOffice, then Pages or Word on a Mac, and reports the page count. If nothing can convert, ask the user to open the .docx and save it as PDF.

**Fresh mode** builds a clean, single-column, ATS-friendly layout from scratch. Use it when the base is a PDF or Google Doc, uses tables or columns, or the user wants a new look. Same spec, with `"mode": "fresh"` and no `base`, `keep` or `like`:

```json
{
  "mode": "fresh",
  "out": "resumes/Jane-Doe-Resume-Acme-Analyst.docx",
  "blocks": [
    ["name", "Jane Doe"],
    ["contact", "Denver, CO | jane@email.com | (555) 555-0100 | linkedin.com/in/janedoe"],
    ["section", "Education"],
    ["entry", "University of Somewhere, Denver, CO", "May 2027"],
    ["title", "B.A. Economics, GPA 3.7"],
    ["bullet", "Dean's List (2024-2026)"],
    ["skills", "Tools: ", "Excel, SQL, Tableau"]
  ]
}
```

Optional keys: `font` (default Calibri), `size` (default 10.5), `margin` in inches (default 0.6).

## Check before showing the user

- Exactly one page. If it runs over, cut the weakest bullet before shrinking fonts or margins.
- Render the PDF to an image and look at it (on a Mac, `sips -s format png file.pdf --out file.png`). Check for orphaned lines, broken tabs and leftover text from the base.
- Read every line against `facts.md` one last time.

Then send the user the PDF with 2-3 sentences on what changed and why, tied to the story. Wait for their OK before using it. Mark the role "Resume ready" in the tracker.
