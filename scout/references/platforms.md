# Platforms

Scout is written in the open skill format (a `SKILL.md` plus reference files) that several AI agents read. The workflow is the same everywhere. What changes is where the user's files live, which browser Scout can drive, and whether research can run in parallel. Find the section for where you're running and follow it.

## What Scout needs, and what to do without it

| Capability | Used for | If it's missing |
|---|---|---|
| A folder you can read and write | `profile.md`, `facts.md`, `tracker.md`, resumes, research | Use the ChatGPT Project mode below |
| Web search and page fetch | Finding roles, researching companies | Ask the user to paste postings |
| Running Python with internet access | `jobs.py` (job boards), `resume.py` (resumes) | Search the web instead of `jobs.py`; give the user the .docx to save as PDF |
| A browser tool that drives the user's own signed-in browser | Reading their LinkedIn, searching LinkedIn jobs and alumni, filling applications and uploading the resume | LinkedIn: the user saves their profile as a PDF (Resources or More, then Save to PDF). Applications: an answer sheet they paste from |
| Parallel helpers (subagents) | One research brief per role, all at once | Do the briefs one at a time |
| An email connector (optional) | Reading job-alert emails | Skip it |
| A job-search connector (optional) | More listings | Skip it |

No connector on any platform can read a LinkedIn profile or search LinkedIn jobs, so LinkedIn always goes through a browser the user is signed in to, or the PDF.

## Claude Code

- **Files:** the current working directory.
- **Browser:** Claude in Chrome. The desktop app's built-in browser pane can't upload files, and some application sites wipe the form when it opens a new window, so don't fill applications there.
- **Parallel research:** subagents.
- **Install:** unzip `scout.skill` into `~/.claude/skills/`.

## Cowork

- **Files:** the folder the user shared with Cowork.
- **Browser:** Claude in Chrome.
- **Parallel research:** subagents.
- **Install:** drag `scout.skill` into Cowork and click Save skill.

## Codex

- **Files:** the current working directory.
- **Browser:** only if a browser tool that controls the user's Chrome is connected (an MCP server). Otherwise use the fallbacks in the table.
- **Parallel research:** use helpers if Codex offers them; otherwise one brief at a time.
- **Install:** unzip `scout.skill` into `~/.agents/skills/` (every project) or into `.agents/skills/` inside the job-search folder. The user starts it by saying "set up Scout" or typing `$scout`.

## ChatGPT: Project mode

ChatGPT can't keep files in a folder between chats, so a ChatGPT Project stands in for the job-search folder. The project files are Scout's memory.

**Setup** (the README has the exact steps): a Project named "Job Search" holding `scout-chatgpt.md` (this whole playbook in one file) and `resume.py` as project files, plus short project instructions. If the user's plan has ChatGPT Skills, the skill can be installed there instead, but the Project is still where their files live.

**Files.** `profile.md`, `facts.md` and `tracker.md` live as project files, along with the user's original resume. ChatGPT can read project files but can't change them, so:

- At the start of every chat, read them. Each one's "Last updated" line shows whether the user replaced it after the last session; if something they told you before seems missing, ask.
- During onboarding, write all three with the code tool so they can be downloaded, and tell the user to add them to the Project.
- After that, keep working normally. When the user says they're stopping, or the session has run long, give them the full updated version of every file that changed as a download, and say exactly which project files to replace. Never send a partial file or a list of edits to apply by hand.
- Tailored resumes, research briefs and answer sheets are downloads the user keeps on their own computer. Save what matters from them to `facts.md` and `tracker.md`.

**Scripts.** Run `resume.py` in the code tool (python-docx is usually there; if not, use whatever .docx library is available). If the PDF export fails, give the user the .docx and ask them to save it as PDF. The code tool has no internet, so `jobs.py` can't reach job boards: use web search to find roles instead.

**Browser.** ChatGPT's agent mode runs its own browser, so the user signs in there when it asks. It can read LinkedIn and fill applications; the user still makes the final click. Without agent mode, use the LinkedIn PDF and answer sheets.

**Research.** One brief at a time, summarized in chat.
