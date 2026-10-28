# Filling the application

Scout fills the application so the user only has to review it and click Submit. The user stays in charge of anything legal, anything that signs in, and the final click.

## Before opening the form

- The tailored resume PDF is approved.
- Written answers are approved (`research/<company-role>-answers.md`).
- `facts.md` standing answers are current.
- Check `references/ats-gotchas.md` for the site's known traps.

## Which browser

- **Claude in Chrome**, the user's own Chrome, is the default. It's signed in to their accounts and can upload files.
- Claude Code's built-in browser pane can't upload files and some sites wipe forms when a new window opens in it, so don't use it for applications.
- **No browser tool:** write a field-by-field answer sheet (every question, the exact answer, the file to upload) and walk the user through pasting it in.

## Order of operations

1. **Sign-in and accounts are the user's.** If the site needs an account (Workday, SuccessFactors, iCIMS and others often do), ask the user to sign in or create it, then continue. Never type a password.
2. **Upload the resume first.** Many systems parse the resume and overwrite the form with what they extract, sometimes wiping fields you've filled. Uploading first means the parse happens before your work, not after.
3. **Fix what the parser got wrong.** Parsed job and school entries are often garbled, duplicated or out of order. Check each one by company name, not by row position.
4. **Fill everything else** from `facts.md` and the approved answers. For anything not covered, stop and ask, then add the answer to `facts.md` so it's never asked twice.
5. **Read every field back.** Read the values out of the page (the accessibility tree or a script) and compare them to what you meant to enter. Dropdowns and date pickers often look filled but didn't commit.
6. **Save a draft** if the site offers one. Long idle sessions often time out and lose unsaved work.
7. **Hand over.** Tell the user it's ready in one short message: what you filled, anything unusual, and exactly what's left for them. For example: "Filled and checked. Left for you: your home address, the 2 certification boxes, and Submit. It times out after about 30 minutes, so best to do it now."

The user always handles: legal attestations and certification checkboxes, e-signatures, anything they marked "I'll type it" in `facts.md`, and Submit.

## After they submit

- Mark the role Applied in `tracker.md` with today's date and a follow-up date about 10 days out.
- If the user also keeps a LinkedIn job tracker or another list, offer to update it.
- Suggest one outreach for that company: an alum on the team, or whoever posted the role. See `references/outreach.md`.
- Update "Next up" in the tracker.
