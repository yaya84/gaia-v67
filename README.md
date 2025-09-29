# 🌍 GAIA v6.7 - Système de Monitoring Intelligent

**GAIA v6.7** est un système de monitoring intelligent conçu pour surveiller les performances système en temps réel avec une approche cognitive avancée.

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-green.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 Fonctionnalités

- **API REST moderne** avec FastAPI pour l'intégration facile
- **Monitoring temps réel** des métriques système (CPU, mémoire, réseau)
- **Endpoint de santé** pour vérifier l'état du système
- **Métriques Prometheus** pour l'observabilité et le monitoring
- **Architecture modulaire** pour une extensibilité future

## 📋 Prérequis

- Python 3.9 ou supérieur
- pip pour la gestion des dépendances

## 🛠️ Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/yaya84/gaia-v67.git
cd gaia-v67
```

### 2. Créer un environnement virtuel

```bash
python3 -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

## 🚀 Démarrage Rapide

### Lancer l'API

```bash
uvicorn gaia_api:app --reload
```

L'API sera disponible à l'adresse `http://localhost:8000`.

### Accéder à la documentation

- **Documentation interactive (Swagger)** : `http://localhost:8000/docs`
- **Documentation alternative (ReDoc)** : `http://localhost:8000/redoc`

## 📡 Utilisation de l'API

### Vérifier la santé du système

```bash
curl http://localhost:8000/health
```

**Réponse :**
```json
{
  "status": "ok",
  "cycles": 42
}
```

### Soumettre un événement de monitoring

```bash
curl -X POST "http://localhost:8000/event" \
  -H "Content-Type: application/json" \
  -d '{
    "cpu": 0.75,
    "memory": 0.60,
    "network": 0.25
  }'
```

### Obtenir le statut du système

```bash
curl http://localhost:8000/status
```

### Récupérer les métriques Prometheus

```bash
curl http://localhost:8000/metrics
```

## 📊 Métriques Disponibles

Le système expose plusieurs métriques au format Prometheus :

- `gaia_cycles_total` : Nombre total de cycles traités
- `gaia_consciousness` : Niveau de conscience actuel (0-1)
- `gaia_threat_mean` : Moyenne des menaces détectées
- `gaia_latency_ms_last` : Latence du dernier événement en millisecondes

## 🏗️ Architecture

```
gaia-v67/
├── gaia_api.py          # API FastAPI principale
├── requirements.txt     # Dépendances Python
├── README.md           # Documentation
└── .github/
    └── workflows/
        └── test.yml    # CI/CD avec GitHub Actions
```

## 🔧 Configuration

Le système utilise une configuration par défaut optimisée. Pour personnaliser le comportement, modifiez les paramètres dans `gaia_api.py`.

## 🧪 Tests

Les tests automatisés sont configurés avec GitHub Actions. Pour exécuter les tests localement :

```bash
# Installation des dépendances de test
pip install pytest pytest-asyncio

# Exécution des tests
pytest
```

## 🤝 Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Forkez le projet
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/nouvelle-fonctionnalite`)
3. Committez vos changements (`git commit -am 'Ajout d'une nouvelle fonctionnalité'`)
4. Poussez vers la branche (`git push origin feature/nouvelle-fonctionnalite`)
5. Ouvrez une Pull Request

## 📝 Roadmap

- [ ] Intégration avec des bases de données pour la persistance
- [ ] Dashboard web pour la visualisation en temps réel
- [ ] Support pour des alertes configurables
- [ ] Intégration avec des systèmes de notification
- [ ] API WebSocket pour le streaming temps réel

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 🆘 Support

Pour toute question ou problème :

- Ouvrez une [issue](https://github.com/yaya84/gaia-v67/issues) sur GitHub
- Consultez la [documentation](http://localhost:8000/docs) de l'API

---

**GAIA v6.7** - Monitoring intelligent pour un monde connecté 🌍✨
