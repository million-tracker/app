# Million — notes for Claude

## Version stamp (always update)
The app shows a version label in Settings: `Million · версия DD.MM · HH:MM`.
It is a hardcoded constant in `index.html`, currently `const Hi="18.11 · 16:47"`
(the variable name may change after a rebuild — search for `a("версия")` to find it).

**On every change pushed to the repository, update this stamp** to the current date
and time in Kyiv (Europe/Kiev), format `DD.MM · HH:MM`. The owner uses it to tell
which version is live.

## Languages
The app supports Russian, Ukrainian and English. The biomechanics screen (template
string containing `<title>Біомеханіка вправи</title>`, plus its nested 3D pages) is
written in Ukrainian and translated at runtime through the `__T()` dictionary
(`__LD.ru` / `__LD.en`). New Ukrainian strings there need ru/en entries added.
