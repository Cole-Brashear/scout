# Onboarding

Goal: in about 10 minutes, a `profile.md` good enough to pick the first batch of jobs. The resume and LinkedIn answer "what have you done", so the interview only asks what documents can't: what the user enjoyed, what they want, and their limits. Everything else (the numbers behind each bullet, form answers, who they know, their writing voice) gets asked later, at the moment it's needed. A short setup gets people to their first applications; a long one gets abandoned.

## Step 1: Say what you need

Open with this, in your own words:

> I'll get you set up in about 10 minutes. I need two things from you:
>
> 1. **Your resume.** Drag the file in or give me its path. A Word file (.docx) is best, because I can keep your formatting when I tailor it. A PDF works too.
> 2. **Your LinkedIn.** Paste your profile URL. [If Claude in Chrome is available:] I'll read it in your Chrome, so make sure you're signed in to LinkedIn there. [If not:] On your LinkedIn profile, click Resources (or More), then Save to PDF, and drop that file in.
>
> No LinkedIn yet? That's fine, the resume is enough. After I read them, I'll ask about 7 quick questions. Everything I learn is saved to files in this folder, so you can read and edit it.

Check which tools you have before sending it. If Claude in Chrome isn't available, add one line: Scout uses it later to search LinkedIn jobs and fill applications, and onboarding works fine without it for now.

Create `profile.md` from `assets/profile-template.md` and `facts.md` from `assets/facts-template.md`, and update the status line as you go so a stopped session can pick up where it left off.

## Step 2: Read before asking

- Save the resume to `resumes/base/` and never edit it.
- **LinkedIn in Chrome:** open their profile URL, scroll so every section loads, and open "Show all" on Experience, Skills and Licenses & certifications. Read only: never click Connect, Message, Follow or Edit. If LinkedIn shows a sign-in wall, ask them to sign in to LinkedIn in Chrome, or use Save to PDF instead.
- **Fill `facts.md`** from both documents: education, every role with its dates, skills, certifications, languages, awards, links. These are the user's own documents, so their claims count as confirmed. Note anything that conflicts between the two (different dates, a job on one but not the other) and ask about it in Step 3.
- **Writing voice:** their LinkedIn About section and any posts are a sample of how they write. Note it in the profile's "Writing voice" section. Their chat messages count too.
- **Make notes for yourself:** what they seem to be aiming at, their strongest proof, what's missing or unclear. These decide which questions need asking and how to word them.

## Step 3: Seven questions, one at a time

Ask one question per message. Tie each one to their resume where you can. Skip any the documents already answer.

Allow **one follow-up** per question, only when the answer is vague ("I like helping people", "something in business", "I want impact"). Ask for the last specific time: "When did that last happen? What were you actually doing?" Then move on. Most of the useful signal is in that one specific story.

1. **Direction.** "What are you hoping to land? A rough idea is fine, and so is 'no idea.' Any deadlines or offers already in play?"
   If it's vague or "no idea", follow up with: "When did you last lose track of time doing something? What were you doing?"
2. **The best part of your resume.** "Of everything here, which did you enjoy most, and what were you actually doing day to day?" This shows the kind of work that fits them better than any interest list.
3. **The worst part.** "Which would you not want to do again, and why?" The reason usually shows a value or a dealbreaker.
4. **The envy test.** "Whose job would you take tomorrow? Someone real: an alum, a family friend, someone you follow. Which part of it?" This turns vague wants into concrete targets.
5. **How you like to work.** "Pick your top 2 and your bottom 1:
   - **Build:** make things, like products, code or content.
   - **Operate:** run and improve how things work, like teams, processes, logistics.
   - **Analyze:** find the answer in data or research.
   - **Advise:** help others decide, like consulting or strategy.
   - **Sell:** win people over, like sales, partnerships, fundraising.
   - **Create:** design, write, tell stories.
   - **Care:** help people grow or get better, like coaching, health, education.

   And would you rather be at a big company with training, a mid-size one, or a startup where you wear many hats?"
6. **Your limits.** Ask these together, since short answers are fine:
   - Where would you live? Places you'd love, places you'd be fine with, places that are a no.
   - The lowest base salary you'd take, and what's driving that number. If they don't know, suggest one from rent and loan payments in their target cities.
   - Your earliest start date.
   - Do you need visa sponsorship, now or later? If yes, note the visa type, since it changes which employers to target.
   - Anything that's a no: industries, commission-heavy pay, heavy travel, fully remote.
7. **What's missing.** "Anything you're proud of that isn't on your resume or LinkedIn?" Add confirmed answers to `facts.md`.

If they say they're short on time, ask 1 and 6 now and the rest during the first search.

## Step 4: Play it back

Write the full `profile.md`, then show them a short version:

- The "In one paragraph" portrait.
- The top 3 directions, each with a sentence on why it fits, tied to something they said. Include at least one they didn't name but their answers point to, with real titles they may not know exist: Business Operations Associate, Implementation Consultant, Solutions Engineer, Customer Success Manager, Program Coordinator, Associate Product Manager, rotational leadership programs.
- The hard filters.

Ask: "What's wrong or missing?" Fix it, set the status line to `Onboarding: complete (YYYY-MM-DD)`, and create `tracker.md` from `assets/tracker-template.md` with the default weekly goal (3 applications and 2 outreach messages; tell them they can change it).

Then offer to find their first batch. **The first batch doubles as calibration:** ask them to rate each role 1-5 with a few words why, and update "Learned from reactions" in the profile. Reactions to real postings are more honest than answers to abstract questions.

## Asked later, when it matters

| What | When | Where it's handled |
|---|---|---|
| The numbers behind each resume bullet | When a role's research brief says a number would help | `references/research-brief.md` |
| Standing form answers (work authorization, self-ID, salary answer, contact details) | Before the first application | `references/apply.md` |
| Who they know | Before the first outreach | `references/outreach.md` |
| A writing sample | Before the first "why us" answer, only if LinkedIn and chat gave too little | `references/why-us.md` |
| Stories (led something, failed and recovered, a conflict) | When an application or interview asks | `references/why-us.md`, `references/interview.md` |

## Reading between the lines

This section of the profile is what lets Scout find roles the user wouldn't have searched for. Write each inference with its evidence and a way to test it, so it can be confirmed or dropped.

- **Look for patterns across the resume and answers.** Which verbs keep coming up: organizing, teaching, fixing, persuading, analyzing, building?
- **Separate "should" from "want."** Prestige words, parents' hopes and "everyone says" mark borrowed goals. Things they describe in detail without being asked mark real ones.
- **Trust energy over labels.** Someone who says finance but lights up describing how they ran a club's events is telling you something.
- **Translate patterns into titles they don't know exist.** Most students can name about ten job titles.
- **Notice limits they didn't say out loud.** A student supporting family can't take a low-paid "dream" role.
- **Mark confidence** high, medium or low. Low-confidence inferences are things to test with the first batch, not conclusions.

| Inference | Evidence | Confidence | How to test |
|---|---|---|---|
| Wants to run things more than advise on them | Enjoyed running the club's events most; called the consulting internship "making slides about other people's problems" | High | Put operations roles beside consulting roles in the first batch |
| The pull toward banking is borrowed | Named it as the direction, but every story was about people, not markets | Medium | Ask directly; include one banking analyst role and watch the rating |
