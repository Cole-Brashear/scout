<p align="center">
  <a href="media/scout-launch.mp4"><img src="media/scout-launch.gif" alt="Scout launch video: a student gives a vague answer, Scout asks a sharper question, writes a profile, finds roles, tailors a resume, fills the form, and the student clicks Submit" width="800"></a>
  <br>
  <a href="media/scout-launch.mp4">Watch with sound</a>
</p>

# Scout

Scout is a Claude skill that runs your job search with you. It starts by interviewing you about your life, what you're into, how you like to work and what you need, reads your resume, and writes a profile of what you're actually looking for. Then every week it finds roles that fit, researches each company, tailors your resume to the story that company wants to hear, drafts your answers and fills in the application. You read it over and click Submit.

Built for college students and new grads.

## How it works

1. **Setup, about 10 minutes.** Scout reads your resume and LinkedIn first, so it only asks what they can't tell it: what you enjoyed most and least, whose job you'd take, how you like to work, and your limits on location, pay and start date. Seven questions, one at a time, and it pushes back on vague answers.
2. **Your profile.** Everything lands in `profile.md`: hard filters, ranked directions, a scoring rubric, and a "reading between the lines" section where Scout writes what your answers say that you didn't, with the evidence. You rate your first batch of roles so it can check its read on you.
3. **Find and vet.** Each week Scout checks your job-alert emails, company job boards, LinkedIn and startup boards, reads every full posting, and keeps only the roles that pass your filters. You confirm the week's batch.
4. **Research.** One brief per role: the story the ideal candidate's resume tells, which signals you're strong or missing on, and the company's own language.
5. **Fill the gaps.** Scout asks about things you've probably done but left off your resume. Nothing goes on a resume until you confirm it.
6. **Tailor.** A one-page resume per role, true line by line, in your own resume's formatting, as .docx and PDF.
7. **Answers.** "Why us" answers built from the company's stated values and your real reasons, in your voice.
8. **Apply.** Scout fills the application in your own Chrome. You add anything personal, tick the legal boxes and submit.
9. **Outreach.** Warm messages to alumni and people tied to the role, asking for a short call, not a referral. You send them.

It keeps a tracker of every role and conversation, and it learns from what you pass on.

## Three rules it never breaks

- **You make every final click.** Scout never submits an application, sends a message or signs anything for you.
- **Nothing made up.** Every resume line and form answer comes from facts you confirmed.
- **You handle passwords and accounts.** Scout never types a password or creates an account.

## Install

You need access to this repo, then download [`dist/scout.skill`](dist/scout.skill).

**Cowork:** drag `scout.skill` into Cowork and click **Save skill**.

**Claude Code:**

```bash
mkdir -p ~/.claude/skills && unzip -o ~/Downloads/scout.skill -d ~/.claude/skills/
```

### What you need

- **Your resume.** A Word file (.docx) is best, since Scout keeps your formatting when it tailors it. A PDF works too.
- **Your LinkedIn profile.** Recommended, not required. It fills in what your resume leaves out.
- **A paid Claude plan** with Cowork or Claude Code.
- **The Claude in Chrome extension,** with you signed in to LinkedIn in Chrome. Scout uses it to read your LinkedIn, search LinkedIn jobs, find alumni and fill applications. No connector can read LinkedIn, so this is the only way in. Without it, save your LinkedIn profile as a PDF (Resources, then Save to PDF), and Scout gives you an answer sheet to paste into applications.
- **Python 3,** which most Macs already have. Scout installs the one library it needs the first time it builds a resume, and turns resumes into PDFs with Pages or Word on a Mac, or LibreOffice anywhere.
- **Optional:** the Gmail connector, so Scout can read your job-alert emails, and a job-search connector like ZipRecruiter for more listings.

## Start

Make a folder for your search (say, `Job Search`), open it in Claude Code or share it with Cowork, and say **"set up Scout"**. Have your resume file and LinkedIn URL ready; Scout asks for them first. After that, open the same folder and say "what's next" whenever you sit down to work on it.

Scout keeps everything in that folder:

| File | What it holds |
|---|---|
| `profile.md` | Who you are and what you want. Every search starts here. |
| `facts.md` | Confirmed facts, numbers, stories and standing form answers. |
| `tracker.md` | Every role and outreach, its stage, and what's next. |
| `resumes/` | Your original resume, untouched, plus one tailored version per role. |
| `research/` | One brief per role, plus your approved answers. |

They're plain text, so you can read and edit all of them.

## Repo layout

| Path | What it is |
|---|---|
| `scout/` | The skill source. Zipped as is, and the folder name is part of the format. |
| `dist/scout.skill` | The built skill. Rebuild with `./build.sh` after any change. |
| `media/` | The launch video (made with /brag) and the GIF version shown above. |

## Status

Private beta, free to testers. Built by Cole Brashear from the process he used for his own new-grad search. Found a bug or a site that breaks it? Open an issue.
