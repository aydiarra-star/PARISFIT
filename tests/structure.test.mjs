import test from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";

const html = readFileSync("index.html", "utf8");
const js = readFileSync("app.js", "utf8");
const manifest = JSON.parse(readFileSync("manifest.webmanifest", "utf8"));

test("les quatre espaces principaux sont présents", () => {
  for (const id of ["view-today", "view-switch", "view-nutrition", "view-mental"]) {
    assert.match(html, new RegExp(`id="${id}"`));
  }
});

test("la navigation mobile et desktop expose les mêmes destinations", () => {
  for (const view of ["today", "switch", "nutrition", "mental"]) {
    assert.match(html, new RegExp(`data-view="${view}"`));
  }
});

test("les actions essentielles ont leurs points d'entrée", () => {
  for (const id of ["settings", "profile", "workout", "sos", "add-habit", "water-add", "meal-ideas", "breath", "journal", "rest"]) {
    assert.match(html, new RegExp(`id="${id}"`));
  }
  for (const action of ["habitDialog", "function breath()", "function settings()", "function render()"]) {
    assert.ok(js.includes(action), `Logique attendue absente : ${action}`);
  }
});

test("le manifeste décrit une application installable", () => {
  assert.equal(manifest.short_name, "PARISFIT");
  assert.ok(manifest.name.startsWith("PARISFIT"));
  assert.ok(manifest.start_url);
  assert.ok(manifest.display);
  assert.ok(Array.isArray(manifest.icons) && manifest.icons.length > 0);
});

test("les aides d’accessibilité clavier et lecteurs d’écran sont présentes", () => {
  assert.match(html, /class="skip-link"/);
  assert.match(html, /id="main-content"/);
  assert.match(html, /aria-label="Navigation principale"/);
  assert.match(html, /aria-label="Navigation mobile"/);
  for (const view of ["today", "switch", "nutrition", "mental"]) assert.match(html, new RegExp(`data-view="${view}" aria-controls="view-${view}"`));
  assert.match(html, /aria-live="polite"/);
  assert.ok(js.includes('button.type="button"'));
  assert.ok(js.includes('$("[data-view]")'));
  assert.ok(js.includes('$(".nav [data-view], .mobile-nav [data-view]")'));
});

test("les identifiants HTML ne sont pas dupliqués", () => {
  const ids = [...html.matchAll(/\bid="([^"]+)"/g)].map((match) => match[1]);
  assert.equal(new Set(ids).size, ids.length);
});
