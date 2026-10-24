// LucarioNet Service Worker – macht die App offline-fähig und installierbar.
// Bei Updates die Version unten erhöhen (z. B. v3), damit der Cache erneuert wird.
const V = 'lucarionet-v45';
const FILES = ['./', 'index.html', 'manifest.webmanifest', 'icon.svg', 'icon-192.png', 'icon-512.png', 'skin-hw.jpg', 'skin-xm.jpg', 'skin-sv.jpg', 'skin-hw-s.jpg', 'skin-xm-s.jpg', 'skin-sv-s.jpg', 'skh-hw.jpg', 'skh-xm.jpg', 'skh-sv.jpg'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(V).then(c => c.addAll(FILES)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k !== V).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  const u = new URL(e.request.url);
  // Fremde Seiten (Internet-Test, KI-Server) und die lokale API nie aus dem Cache bedienen
  if (u.origin !== location.origin || u.pathname.startsWith('/api/')) return;
  // Netzwerk zuerst (immer die neueste Version), Cache nur als Offline-Reserve
  e.respondWith(
    fetch(e.request, {cache: 'no-cache'}).then(r => {
      if (r && r.ok) { const copy = r.clone(); caches.open(V).then(c => c.put(e.request, copy)); }
      return r;
    }).catch(() => caches.match(e.request).then(r => r || (e.request.mode === 'navigate' ? caches.match('index.html') : Response.error())))
  );
});
