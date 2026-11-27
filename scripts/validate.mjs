import { readFileSync, existsSync } from "node:fs";
import assert from "node:assert/strict";

const html = readFileSync("index.html", "utf8");
const js = readFileSync("app.js", "utf8");
const css = readFileSync("styles.css", "utf8");
const manifest = JSON.parse(readFileSync("manifest.webmanifest", "utf8"));

const ids = [...html.matchAll(/\bid="([^"]+)"/g)].map((match) => match[1]);
const duplicates = ids.filter((id, index) => ids.indexOf(id) !== index);
assert.deepEqual([...new Set(duplicates)], [], "Les identifiants HTML doivent être uniques.");

for (const id of ["view-today", "view-switch", "view-nutrition", "view-mental", "modal", "modal-content", "toast", "date"]) {
  assert.ok(ids.includes(id), `Élément HTML requis absent : #${id}`);
}

for (const view of ["today", "switch", "nutrition", "mental"]) {
  assert.ok(html.includes(`data-view="${view}"`), `Navigation absente pour ${view}`);
  assert.ok(html.includes(`id="view-${view}"`), `Vue absente pour ${view}`);
}

for (const file of ["styles.css", "app.js", "service-worker.js", "manifest.webmanifest", "assets/icon.svg"]) {
  assert.ok(existsSync(file), `Fichier requis absent : ${file}`);
}
assert.ok(css.length > 1000, "La feuille de styles semble vide ou incomplète.");
assert.ok(js.includes("function render()"), "Le rendu principal de l'interface est absent.");
assert.equal(manifest.short_name, "PARISFIT");
assert.ok(manifest.name.startsWith("PARISFIT"), "Le nom du manifeste doit conserver la marque PARISFIT.");
assert.ok(manifest.start_url, "Le manifeste doit définir start_url.");
assert.ok(manifest.display, "Le manifeste doit définir display.");

const staticIds = ["settings", "profile", "workout", "sos", "add-habit", "habits", "water-add", "water-reset", "meal-ideas", "breath", "breath2", "journal", "rest"];
for (const id of staticIds) {
  assert.ok(ids.includes(id), `Contrôle attendu absent du HTML : #${id}`);
}

assert.ok(html.includes("Aller au contenu principal"), "Le lien d’évitement doit être présent.");
assert.ok(html.includes('aria-label="Navigation principale"') && html.includes('aria-label="Navigation mobile"'), "Les deux navigations doivent être nommées.");
assert.ok(html.includes('aria-live="polite"'), "Les mises à jour dynamiques doivent être annoncées.");
assert.ok(js.includes('button.type="button"'), "Les boutons de dialogue ne doivent pas soumettre le formulaire.");
assert.ok(css.includes(":focus-visible"), "Un style de focus clavier visible est requis.");
console.log("Validation structurelle PARISFIT réussie.");
