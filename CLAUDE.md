# Million — notes for Claude

**Before any work, read `PROJECT.md` in the private repository `million-tracker/api`** (project context: state, decisions, open tasks). **At the end of every task, update it there** (a PR in api; a change to `.md` only does not trigger the Worker deploy).

## Version stamp (always update)
The app shows a version label in Settings: `Million · версия DD.MM · HH:MM`.
It is a hardcoded constant in `index.html`, currently `const Hi="27.11 · 17:58"`
(the variable name may change after a rebuild — search for `a("версия")` to find it).

**On every change pushed to the repository, update this stamp** to the current date
and time in Kyiv (Europe/Kiev), format `DD.MM · HH:MM`. The owner uses it to tell
which version is live.

## Product policy (owner, 20.11)
Million is (1) a smart, evidence-based navigator for the first workouts — it helps a beginner start safely
and collect real statistics; it does not replace the person's own judgment or proper technique; and
(2) a full coach ↔ client ecosystem with gym geolocation and deep analytics.
Smart analytics and deviation control: the app logs workouts and nutrition, tracks progress, volume and
calories, and highlights lapses by itself — if someone drops out of the schedule or drifts off their
calories, it pulls the last week and previous periods and shows exactly where the deviation is.
Design every feature and hint in this spirit: guide, measure, explain — never overpromise.

## Tip of the day / praise (Telegram)
The app picks at most one reason a day on the phone (`TipL`: new working weight or more reps at the same
weight in a workout of the last 36 h, a week of planned workouts with no misses, calories within ±10% on
5 of 7 days, weight/waist moving toward the goal) and `TipS` sends one ready line to `/api/tip` for 19:00
local time; with no reason it schedules "N days without a workout" for 3 days after the last workout.
Repeats: the same kind at most once in 7 days (`tb_tip` in localStorage). Opt-out only in the bot: the button under a tip («🔕» / «🔔 back on») or `/tips`; the server keeps `tipOff`
(returned by `/api/status`; the app then stops sending lines). Server side: `million-tracker/api` (cron sends).

## Languages
The app supports Russian, Ukrainian and English. The biomechanics screen (template
string containing `<title>Біомеханіка вправи</title>`, plus its nested 3D pages) is
written in Ukrainian and translated at runtime through the `__T()` dictionary
(`__LD.ru` / `__LD.en`). New Ukrainian strings there need ru/en entries added.

## Health limits in the program generator (evidence, owner 27.11)
Chips `Xu` (back, knee, shoulder, heart, vein, diab) change the plan in `Ec` and the hints in `sh`.
Swaps: `Ju` (generator) and `JuK0` (old knee map, used only when a user reports knee pain on an exercise).
Extra exercises after the compounds (`HX` in `Ec`): back → plank every day; knee → leg extension + hip abduction
on leg days; shoulder → face pull + cable row on upper days; vein → calf raises; heart → wall sit `wsit`
(4 sets, 60→120 s, not with knee). Diabetes → after-cardio ≥20 min and up to 2 cardio days a week.
Sources and the rules behind them: PROJECT.md in `million-tracker/api` («Здоровье: доказательная база»).
Keep hints short, name the source, never promise treatment; always "check with your doctor" for heart/diabetes.

## Simulator figures (biomechanics screen)
Body segments follow anthropometric ratios (Winter / Drillis–Contini). Large side-view figure: torso hip–shoulder 100,
thigh 96, shin ~94, upper arm `UA=64`, elbow–grip `FA=62` (`AR` = full arm). Small standing figure for arm exercises
(`SH`, `sideStand`, `frontStand`): torso 69, thigh 60, shin 60, arm 46+42. Use these constants for new templates and
check bone lengths stay constant over the movement. The view box fits the whole figure automatically (`viewY`).
Technique cues per exercise: `TECH` (uk/ru/en arrays) next to the templates.

## Screenshots of every change (mandatory)
The owner asked to see every change on screenshots. After each change, take screenshots
of every affected screen in Playwright with `devices["iPhone 13"]` (touch on, so the Million
keyboard and press-and-drag work), in the owner's language (uk) unless asked otherwise, and
send them to the owner together with the summary — including intermediate states such as
a drag in progress or an open keyboard.

## Before every push: test every button you touched (mandatory)
The owner has asked for this explicitly. A change is not done until every button
on every screen/sheet affected by the change has been clicked in a real browser.

How to run the app locally (it only starts on its own hostname):
- Use Playwright (`/home/claude/.npm-global/lib/node_modules/playwright` or `npm root -g`).
- Route `https://million-tracker.github.io/**` to the local `index.html` with
  `context.route(...)` → `fulfill`, abort every other host, then `goto` that URL.
- Demo data loads on first start (`localStorage` keys `tb_*`). To get a client plan,
  copy an item of `tb_plans`, set `who:"<name>"` and a date, save, reload.
- Open screens by creating a button with `data-a="<action>" data-x="<arg>"` and
  clicking it (all clicks go through `document` → `G[data-a](data-x, el)`).

Automated audit (use it, then check the NOCHANGE list by hand):
`node tools/button-audit.js index.html en out.json 3` — clicks every button on every tab
and in every sheet it opens; prints ERR (JS error) and NOCHANGE (no visible effect).
Coach mode: add `tools/seed-coach.js` as 5th argument. Long tabs: split with `TAB=train R=0-12`.
The audit restores state on an empty page (`/__blank`) because the app saves its state on unload,
and it counts changed input values / focus as a visible effect (`input`).
Expected NOCHANGE (not bugs): already-selected options, rest-timer buttons while no timer
runs, current tab, "Add" with an empty field (focuses it), external links / Telegram-only
actions (share, privacy, payment) — they need Telegram.

Checklist for each affected screen or sheet:
1. List all `[data-a]` inside it and click each one, for every state that changes
   which buttons appear (today / past / future plan, sent / changed, collapsed / open).
2. After each click check that the result is visible **immediately**: the open
   sheet itself updates (not only the screen under it), or the expected sheet opens.
3. Watch `pageerror` — zero errors.
4. Test in uk, ru and en (`localStorage.tb_lang`).

Known trap: most actions only call `A()`, which re-renders the main screen, not the
open sheet (`#sheetBody`, current sheet key in `Jt`). A sheet that shows live data
must re-render itself after `A()` — see the `pview` sheet (`G.__pvR`, called from `A()`).
