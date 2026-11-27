-- PARISFIT — brouillon de schéma PostgreSQL portable
-- DOCUMENTATION / PROTOTYPE UNIQUEMENT : non exécuté sur une base.
-- Les politiques RLS et l'intégration au fournisseur d'authentification
-- seront ajoutées après sélection et tests du backend.

BEGIN;

CREATE TABLE app_users (
  id UUID PRIMARY KEY,
  auth_issuer TEXT NOT NULL,
  auth_subject TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  deleted_at TIMESTAMPTZ,
  CONSTRAINT app_users_auth_identity_unique UNIQUE (auth_issuer, auth_subject)
);

CREATE TABLE profiles (
  user_id UUID PRIMARY KEY REFERENCES app_users(id) ON DELETE CASCADE,
  display_name VARCHAR(80),
  locale VARCHAR(16) NOT NULL DEFAULT 'fr-FR',
  timezone VARCHAR(64) NOT NULL DEFAULT 'Europe/Paris',
  unit_system VARCHAR(8) NOT NULL DEFAULT 'metric'
    CHECK (unit_system IN ('metric', 'imperial')),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE consent_events (
  id UUID PRIMARY KEY,
  user_id UUID NOT NULL REFERENCES app_users(id) ON DELETE CASCADE,
  purpose VARCHAR(40) NOT NULL
    CHECK (purpose IN ('health_data', 'camera_analysis', 'ai_personalization',
                       'nonessential_notifications', 'optional_location')),
  policy_version VARCHAR(40) NOT NULL,
  granted BOOLEAN NOT NULL,
  recorded_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX consent_events_user_purpose_time_idx
  ON consent_events (user_id, purpose, recorded_at DESC);

CREATE TABLE goals (
  id UUID PRIMARY KEY,
  user_id UUID NOT NULL REFERENCES app_users(id) ON DELETE CASCADE,
  title VARCHAR(160) NOT NULL,
  description TEXT,
  target_date DATE,
  status VARCHAR(16) NOT NULL DEFAULT 'active'
    CHECK (status IN ('active', 'paused', 'completed', 'archived')),
  version INTEGER NOT NULL DEFAULT 1 CHECK (version > 0),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  deleted_at TIMESTAMPTZ
);
CREATE INDEX goals_user_updated_idx ON goals (user_id, updated_at DESC);

CREATE TABLE tasks (
  id UUID PRIMARY KEY,
  user_id UUID NOT NULL REFERENCES app_users(id) ON DELETE CASCADE,
  goal_id UUID REFERENCES goals(id) ON DELETE SET NULL,
  title VARCHAR(200) NOT NULL,
  description TEXT,
  category VARCHAR(40) NOT NULL DEFAULT 'personal',
  priority SMALLINT NOT NULL DEFAULT 2 CHECK (priority BETWEEN 1 AND 4),
  estimated_minutes INTEGER CHECK (estimated_minutes BETWEEN 1 AND 1440),
  due_at TIMESTAMPTZ,
  recurrence_rule TEXT,
  status VARCHAR(16) NOT NULL DEFAULT 'todo'
    CHECK (status IN ('todo', 'in_progress', 'done', 'cancelled')),
  version INTEGER NOT NULL DEFAULT 1 CHECK (version > 0),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  deleted_at TIMESTAMPTZ
);
CREATE INDEX tasks_user_status_due_idx ON tasks (user_id, status, due_at);

CREATE TABLE habits (
  id UUID PRIMARY KEY,
  user_id UUID NOT NULL REFERENCES app_users(id) ON DELETE CASCADE,
  title VARCHAR(160) NOT NULL,
  trigger_description TEXT,
  routine_description TEXT,
  frequency_rule TEXT,
  status VARCHAR(16) NOT NULL DEFAULT 'active'
    CHECK (status IN ('active', 'paused', 'archived')),
  version INTEGER NOT NULL DEFAULT 1 CHECK (version > 0),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  deleted_at TIMESTAMPTZ
);
CREATE INDEX habits_user_status_idx ON habits (user_id, status);

CREATE TABLE habit_logs (
  id UUID PRIMARY KEY,
  user_id UUID NOT NULL REFERENCES app_users(id) ON DELETE CASCADE,
  habit_id UUID NOT NULL REFERENCES habits(id) ON DELETE CASCADE,
  local_date DATE NOT NULL,
  timezone VARCHAR(64) NOT NULL,
  outcome VARCHAR(16) NOT NULL
    CHECK (outcome IN ('completed', 'partial', 'skipped', 'rest')),
  note TEXT,
  client_mutation_id UUID NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  CONSTRAINT habit_logs_user_mutation_unique UNIQUE (user_id, client_mutation_id)
);
CREATE INDEX habit_logs_user_date_idx ON habit_logs (user_id, local_date DESC);
CREATE INDEX habit_logs_habit_date_idx ON habit_logs (habit_id, local_date DESC);

CREATE TABLE sync_mutations (
  id UUID PRIMARY KEY,
  user_id UUID NOT NULL REFERENCES app_users(id) ON DELETE CASCADE,
  client_mutation_id UUID NOT NULL,
  entity_type VARCHAR(40) NOT NULL,
  entity_id UUID NOT NULL,
  outcome VARCHAR(16) NOT NULL DEFAULT 'accepted'
    CHECK (outcome IN ('accepted', 'rejected', 'conflict')),
  server_version INTEGER,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  CONSTRAINT sync_mutations_idempotency_unique UNIQUE (user_id, client_mutation_id)
);
CREATE INDEX sync_mutations_user_created_idx
  ON sync_mutations (user_id, created_at DESC);

COMMIT;

-- Obligatoire avant toute utilisation réelle :
-- 1. Ajouter des politiques RLS et les tests d'isolation pour le fournisseur retenu.
-- 2. Vérifier la cohérence user_id/habit_id et user_id/goal_id dans les écritures API.
-- 3. Définir les règles de purge, sauvegarde, export et suppression.
-- 4. Ajouter les tables métier restantes après validation du modèle.
-- 5. Tester la migration sur une base jetable et documenter le rollback.
