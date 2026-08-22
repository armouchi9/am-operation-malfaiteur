# AM Opération Malfaiteur — Site vitrine

## Problème / Contexte
Site vitrine mono-fichier HTML pour une entreprise de dératisation/désinsectisation
(Île-de-France). Univers créatif combiné : scène de crime / ruban de sécurité +
radar/viseur militaire + dossier d'enquête "WANTED". Palette rouge sang / noir.
Règle métier : jamais de tarif fixe — devis gratuit après diagnostic.

## Architecture
- **Front** : fichier autonome unique `/app/frontend/public/index.html`
  (CSS + JS vanilla inline, GSAP + ScrollTrigger + Lenis via CDN). React (`App.js`)
  rend `null` — le contenu vit dans `index.html` (div `#root` vide requis).
  NOTE: toute modif de `public/index.html` exige `sudo supervisorctl restart frontend`
  (le template HtmlWebpackPlugin est mis en cache).
- **Back** : FastAPI `/app/backend/server.py`, endpoint `POST /api/contact`
  (stocke dans Mongo `contacts` + envoie un email au propriétaire via Resend managé).
- **Email** : intégration Resend managée (`EMERGENT_EMAIL_KEY`, `EMAIL_FROM_NAME`),
  destinataire = `OWNER_EMAIL` (operationmalfaiteur@gmail.com). Gate `_assert_safe_email`.

## Implémenté (2026-06)
- Hero kinétique : reveal ligne par ligne (GSAP), gyrophare rotatif, grille radar,
  rubalise, statut de disponibilité, 3 CTA (appel / WhatsApp / devis), stats.
- Sections : Services (fiches WANTED), Engagements (manifeste numéroté), Zone IDF
  (carte radar géographique 8 départements), Espace pros (dossier CLASSIFIÉ + rubalise),
  bloc anti-tarif, avis (placeholders), FAQ accordéon, contact (form + directs), footer.
- Curseur réticule, tilt 3D sur cartes, marquees rubalise, `prefers-reduced-motion`.
- Logo client intégré (header + footer, `mix-blend-mode:screen`).
- Formulaire → `/api/contact` (email réel testé OK, HTTP 200).

## Implémenté (2026-08)
- Formulaire indépendant d'Emergent : hand-off WhatsApp (wa.me/33766760246) par défaut,
  option email Web3Forms (WEB3FORMS_KEY vide = branche WhatsApp). Aucun backend requis.
- Favicon/onglet = logo. Réseaux sociaux dans footer (Instagram + TikTok) + JSON-LD sameAs.
- **Site 100% autonome** : logo téléchargé et optimisé en local `public/logo.png` (506x512, 376Ko).
  Les 6 références (favicon, apple-touch-icon, og:image, twitter:image, JSON-LD image,
  logos header/footer) pointent désormais vers `logo.png` relatif — plus aucune URL d'assets
  Emergent dans le HTML. Prêt pour hébergement statique (Netlify/Cloudflare/OVH…).

## Backlog / À adapter par le client
- Remplacer les 3 avis "PLACEHOLDER" par de vrais avis.
- Brancher un vrai domaine : FAIT (operationmalfaiteur.com). Canonical, og:url, og:image,
  twitter:image et JSON-LD (image + url) pointent vers https://operationmalfaiteur.com/.
  Le logo/favicon restent en chemin relatif logo.png (résolus une fois le site hébergé sur le domaine).
- SEO avancé (optionnel) : robots.txt + sitemap.xml, image OG dédiée 1200×630, FAQ schema,
  Google Business Profile + Search Console.
- P2 : page mentions légales, tracking analytics.
