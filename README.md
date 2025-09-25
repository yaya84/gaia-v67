# 🌌 GAIA v6.7 – Digital Immune System

**GAIA v6.7** est un système immunitaire numérique **evidence-based**, conçu pour l’IoT et l’edge computing.
Il combine **auto-apprentissage**, **self-healing**, **monitoring temps réel**, et une intégration complète avec **Prometheus + Grafana**.

---

## ✨ Fonctionnalités

* 🔐 **Détection & Auto-Healing** : Circuit breaker + resets autonomes.
* 📊 **Monitoring** : Métriques exposées en Prometheus + dashboards Grafana.
* ⚡ **Performance** : Latence p95 < 3ms, throughput > 500 events/s (optimisé RPi).
* 🧪 **Tests & Benchmarks** : Modes intégrés (`--mode test`, `--mode benchmark`).
* 🐳 **Docker-Ready** : Déploiement complet en 1 commande (`docker-compose up`).
* ☁️ **CI/CD GitHub Actions** : Tests automatiques et benchmarks à chaque commit.

---

## 📦 Installation

### 1. Cloner le projet

```bash
git clone https://github.com/yaya84/gaia-v67.git
cd gaia-v67
```

### 2. Dépendances locales

```bash
pip install -r requirements.txt
```

### 3. Lancer GAIA en mode test

```bash
python gaia_v67.py --mode test
```

---

## 🐳 Déploiement Docker

### 1. Construire et lancer

```bash
docker-compose up -d
```

### 2. Accéder aux services

* API FastAPI → [http://localhost:8000](http://localhost:8000)
* Prometheus → [http://localhost:9090](http://localhost:9090)
* Grafana (admin / gaia123) → [http://localhost:3000](http://localhost:3000)

### 3. Arrêter

```bash
docker-compose down
```

---

## 🔧 Makefile (raccourcis utiles)

```bash
make build       # Construire l'image
make run         # Lancer la stack
make stop        # Stopper les services
make test        # Exécuter les tests
make benchmark   # Lancer un benchmark 1000 cycles
make deploy      # Déploiement complet
```

---

## 📊 Monitoring

GAIA expose ses métriques sur `/metrics` :

* `gaia_latency_p95_ms` → latence 95e percentile
* `gaia_threat_mean` → moyenne du score de menace
* `gaia_emergence` → score d’émergence du système
* `gaia_memory_mb` → mémoire utilisée

Dashboard Grafana inclus (port 3000).

---

## ⚙️ Modes disponibles

```bash
python gaia_v67.py --mode test
python gaia_v67.py --mode benchmark --cycles 1000
python gaia_v67.py --mode monitor
```

* **test** → Vérifie que toutes les contraintes RPi sont respectées.
* **benchmark** → Mesure latence, throughput, mémoire.
* **monitor** → Lancement avec affichage temps réel.

---

## 🤖 CI/CD GitHub Actions

* Workflow `.github/workflows/ci.yml` :

  * Tests unitaires
  * Benchmarks (500 cycles)
  * Artifacts upload (résultats)

Résultats visibles dans l’onglet **Actions** du repo.

---

## 📜 Licence

Projet GAIA v6.7 – (c) Arkab Family.
Libre pour expérimentation, protégé pour usage commercial.