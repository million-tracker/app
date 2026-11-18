# Million — notes for Claude

## Version stamp (always update)
The app shows a version label in Settings: `Million · версия DD.MM · HH:MM`.
It is a hardcoded constant in `index.html`, currently `const Hi="18.11 · 17:04"`
(the variable name may change after a rebuild — search for `a("версия")` to find it).

**On every change pushed to the repository, update this stamp** to the current date
and time in Kyiv (Europe/Kiev), format `DD.MM · HH:MM`. The owner uses it to tell
which version is live.

## Languages
The app supports Russian, Ukrainian and English. The biomechanics screen (template
string containing `<title>Біомеханіка вправи</title>`, plus its nested 3D pages) is
written in Ukrainian and translated at runtime through the `__T()` dictionary
(`__LD.ru` / `__LD.en`). New Ukrainian strings there need ru/en entries added.

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
