# LOCK IN 30: the buyers' game

A small web app that ships with the LOCK IN book. It turns the book's 30-day challenge into a game. Buyers unlock it with a code from their copy.

- **Sessions:** a 20-minute lock-in timer. A "phone in another room" check earns +5 XP. On-screen lines coach the three ugly minutes ("That is minute two.").
- **Campaign:** 30 tiles, one for each day locked in. The campaign can't be failed; it ends on the 30th day locked in, however long that takes.
- **Chain:** follows the book's rule, *never miss twice*. One missed day costs nothing. Two in a row reset the chain. Coming back after a miss earns a bonus.
- **Rewards:** XP, 10 levels (Scrolling → Legend) and 10 badges.
- **Doors:** when someone stops early, they name the door (Bored, Stuck, Anxious, Tired). The Doors tab shows where their sessions leak and gives the fix for their top door.
- **Chat:** the "copy my day count" button produces a line to post in the Lock In chat.

It is one static folder with no server and no accounts. It works offline after the first visit and can be added to the home screen like an app.

## Deploy (5 minutes, free)
1. Go to **app.netlify.com/drop**, the same Netlify account as the quiz.
2. Drag the whole `lock-in-30` folder onto the page.
3. In **Site configuration → Change site name**, pick something like `lockin-30`. The link becomes `https://lockin-30.netlify.app`.
4. Put the link and the unlock code where buyers will see them after paying:
   - the book's first pages
   - the Whop product's delivery or welcome message
   - a pinned message in the Lock In chat

**Keep the address fixed once buyers start.** Progress is saved per web address. If the link changes, people have to move their progress over with a backup code.

To update the app, edit the files and drag the folder onto the site's **Deploys** page. If you changed anything besides `index.html`, bump `VERSION` in `sw.js` so installed copies refresh.

## Settings you can change
Everything is in the `CONFIG` block at the top of the script in `index.html`:

| Setting | What it does |
|---|---|
| `unlockCode` | The code buyers type. Case, spaces and dashes are ignored. **Change it from the default `LOCKIN30` before launch.** |
| `bookUrl` | The "Get the book" button on the lock screen (currently the Whop checkout). |
| `quizUrl` | The "Take the free quiz" link. |
| `fixes` | The fix shown for each door. Only Stuck is filled in. Paste the quiz's result text for Bored, Anxious and Tired. |
| `missions` | Optional. One line per day from the book's 30-day challenge, e.g. `["Phone in another room for one block", ...]`. |
| `sessionMinutes`, `blocksPerDay`, `campaignDays` | Defaults: 20 minutes, 3 blocks, 30 days. Players can change minutes and blocks (1–3) in Me → Settings. |

**The code is a soft lock.** Anyone who reads the page source can find it, which is fine for a $15 bonus. If sharing ever becomes a problem, the next step is a Whop-login version. That needs a small server.

## Will people lose their progress?
Progress is saved on the player's phone, in the browser's storage for this site. The app also asks the browser to keep that storage permanently.

| Situation | Progress |
|---|---|
| Closing the app, locking the phone, restarting it | **kept** |
| Leaving mid-session (phone really in another room) | **kept**: the timer runs on the clock, so the session is waiting when they come back |
| Adding the app to the home screen and opening it from there | **kept**: this is the safest way to use it |
| Clearing browser data, private/incognito tabs, a new phone | **lost** unless they restore a backup |

Backups live in **Me**:
- **Copy backup code** puts a `LOCKIN1:` code on the clipboard to keep in Notes.
- **Save backup file** downloads a `.json` file.
- **Restore** takes either one and works on any phone.

## Files
- `index.html`: the whole app
- `manifest.webmanifest`, `sw.js`: install to home screen and offline support
- `fonts/`: Anton, Spectral and JetBrains Mono, under the SIL Open Font License (licences included)
- `sounds/`: the LOCK IN sound kit (lock, chime, pop)
- `icons/`: made from the profile avatar
