# Incident record: test runs dropped real files into the user's ~/Downloads (example for the cleanup law Alexander will write)

**What happened.** Both suites (tlvphoto and exhibition-engine) drive a real headless Chrome; the
gift ceremony clicks a real `<a download>`. Headless Chrome saves downloads to the real ~/Downloads
by default, so every suite run since the night of 2026-07-09/10 dropped 2–4 image files there —
42 files by the time Alexander saw his Downloads folder and called it a critical bug (2026-07-10
~10:41). Fixed the same hour in both harnesses: CDP `Browser.setDownloadBehavior` routes downloads
into the throwaway Chrome profile dir, which the harness already deletes on close. Junk moved to
Trash. Verified by deed: the gift-winning suite now leaves ~/Downloads untouched.

**Why no test caught it.** Every assertion looks INSIDE the page (DOM, computed style, storage); a
file landing on the host machine is a side effect outside all of them, and the browser saves it
silently. Nothing declared the workshop law "a test run leaves the machine as it found it", so no
row could fail.

**Alexander's word (~10:46):** he will write the test-cleanup law into the live-spec pack himself.
This letter only preserves the incident as the worked example — it does not draft the law.

**Who throws it.** The tlvphoto window.
