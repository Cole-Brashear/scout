# Finding and vetting roles

The job is a short list of roles the user would actually be glad to get, not a long list of everything with "analyst" in the title. Every role in the tracker costs them attention, so only add keepers.

## 1. Turn the profile into searches

Read `profile.md`: the hard filters, the ranked directions, the search plan and "Learned from reactions". Then build searches from role family × title variants × locations.

Go beyond the titles the user named. Each direction goes by many titles, and new-grad postings often hide behind odd ones. A user who wants to "run things" might fit Business Operations Associate, Strategy & Operations Analyst, Program Coordinator, Implementation Consultant, Customer Success Associate, Rotational Leadership Program, Chief of Staff Associate or Founder's Associate. Add 2-3 variants per direction.

## 2. Check the sources

Roughly in order of signal:

1. **Job-alert emails** (when a Gmail connector is available). Search the past 7 days for alerts from LinkedIn, Handshake, Indeed and company career sites ("new jobs", "job alert", "jobs for you"). Open the roles they point to; don't trust the email's summary.
2. **Target companies' own job boards.** Many companies post through Greenhouse, Ashby or Lever, which publish a live, dated list of open roles. Use the script:

   ```bash
   python3 <skill-dir>/scripts/jobs.py greenhouse:stripe ashby:ramp lever:palantir -k "new grad" -k analyst -l Denver
   python3 <skill-dir>/scripts/jobs.py detect https://jobs.ashbyhq.com/ramp   # find the ATS and board name from a URL
   ```

   The board name is the slug in the company's job links (`job-boards.greenhouse.io/<board>`, `jobs.ashbyhq.com/<board>`, `jobs.lever.co/<board>`). A 404 means the wrong board name or the wrong ATS, not "no openings". Lever dates are when a posting was first created, so evergreen roles can show dates years old while still open; filter Lever results by title, not `--days`. Workday and in-house career sites don't publish a list like this, so read their pages directly. Record each target's `ats:board` in the profile's search plan once found.
3. **LinkedIn Jobs** (needs Claude in Chrome, with the user signed in to LinkedIn in Chrome; no connector can search LinkedIn jobs). Filtered search URLs tend to redirect to LinkedIn's AI search, so use a natural-language query instead: `https://www.linkedin.com/jobs/search-results/?keywords=<entry level operations analyst jobs in Denver>`. Descriptions load only after scrolling the page. A posting's "People you can reach out to" box lists alumni and connections, which feeds outreach.
4. **Web search**, which works without a browser: `site:jobs.lever.co "new grad" analyst Denver`, `site:job-boards.greenhouse.io "2027" "early career"`, `"rotational program" 2027 operations`.
5. **Handshake** and the school's career site (the user signs in). Employers there are already recruiting at their school.
6. **Startups:** Y Combinator's Work at a Startup (workatastartup.com) and Wellfound. Startups hire closer to the start date and rarely run formal new-grad programs, so "0-2 years" roles at seed to Series B companies are fair game.
7. **New-grad programs:** rotational, leadership-development and analyst programs at large companies. Search "<company> new grad program 2027" or "<industry> rotational program".
8. **Job-search connectors,** if the user has one connected (ZipRecruiter has one, for example). Treat results like any listing: open the original posting before trusting it.

## 3. Vet each posting

Read the full posting, not the title. "Entry level" often means 2-5 years.

- **Experience:** 0-2 years, or "new grad", "early career", "university graduate", "class of [year]". Read the requirements section; drop roles that require more years or a degree the user doesn't have, unless the posting says "or equivalent experience".
- **Hard filters:** pay (many states, including California, Colorado, Washington, New York and Illinois, require posted pay ranges), location, arrangement, sponsorship, dealbreakers.
- **Still open:** confirm on the company's own page or with `jobs.py`. Note any deadline. A role reposted for months may be a ghost listing.
- **Red flags:** pay mostly commission ("OTE", "uncapped earnings") unless the user wants that; vague staffing-agency postings with no company named; unpaid roles; "rockstar" postings with no real description; any line aimed at AI applicants (show it to the user).
- **Score it** with the rubric in `profile.md`. Write one line on why it fits, citing the profile ("operate > advise; Denver; $85K over the $70K floor").

## 4. Propose the batch

Bring the user the week's batch (their weekly goal, usually 3) plus 2-3 alternates. Mix it: mostly strong fits, one reach, and at most one safer pick. For each: company, title, location, pay, score, the one-line why, and the deadline. Lead with your pick order.

**The first batch after onboarding is also calibration.** Show 5-6 roles across the profile's directions, including one stretch and one that matches what they said but not what their answers suggest, and ask them to rate each 1-5 with a few words why. Update the profile from the ratings, especially where a rating contradicts something they said, then pick the week's applications from the ones they rated highest.

When they confirm, add the batch to `tracker.md` (stage Vetted). When they reject a role, ask why in a few words, then update "Learned from reactions" in the profile. Roles the user saved but you rejected on vetting go under "Passed on" with the reason, so they don't come back.

## Recruiting calendar for new grads (US)

Timing is half the game, and most students learn it too late.

- **August to October of senior year:** big-company new-grad programs open and fill: consulting, banking, big tech, most rotational and leadership programs. Many close by November.
- **November to January:** quieter. A second wave of programs and reopened postings appears in January.
- **February to May:** most regular entry-level roles for a summer start post now, usually 1-3 months before the start date. Most hiring happens here outside the big programs.
- **Startups and small companies:** hire year-round, close to the start date. Relationships built in the fall turn into offers in the spring.
- **Internships for juniors:** follow the same calendar a year earlier, and many convert to return offers.

Use this to set expectations: in October, a quiet search for regular roles is normal, and fall time is best spent on programs with fall deadlines and on outreach that pays off in spring.
