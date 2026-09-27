// LOCK IN 30 service worker: makes the app open offline once it has been visited.
// Progress is NOT stored here (it lives in localStorage); this only caches the app's files.
// Bump VERSION after changing any file so phones pick up the new copy.
const VERSION = "lockin30-v1";
const SHELL = [
  "./", "index.html", "manifest.webmanifest",
  "fonts/Anton-Regular.ttf", "fonts/Spectral-Regular.ttf", "fonts/Spectral-Italic.ttf", "fonts/JetBrainsMono-Variable.ttf",
  "sounds/lock.wav", "sounds/chime.wav", "sounds/pop.wav",
  "icons/icon-180.png", "icons/icon-192.png", "icons/icon-512.png",
];

self.addEventListener("install", (e) => {
  e.waitUntil(caches.open(VERSION).then((c) => c.addAll(SHELL)).then(() => self.skipWaiting()));
});

self.addEventListener("activate", (e) => {
  e.waitUntil(caches.keys().then((keys) => Promise.all(keys.filter((k) => k !== VERSION).map((k) => caches.delete(k))))
    .then(() => self.clients.claim()));
});

self.addEventListener("fetch", (e) => {
  const req = e.request;
  if (req.method !== "GET" || new URL(req.url).origin !== location.origin) return;
  // The page itself: network first, so edits reach people; cached copy when offline.
  if (req.mode === "navigate") {
    e.respondWith(fetch(req).then((res) => {
      const copy = res.clone(); caches.open(VERSION).then((c) => c.put("index.html", copy)); return res;
    }).catch(() => caches.match("index.html")));
    return;
  }
  // Fonts, sounds, icons: cache first.
  e.respondWith(caches.match(req).then((hit) => hit || fetch(req)));
});
