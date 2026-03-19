# PeerPulse — Frontend Flask

Réseau social décentralisé P2P · Frontend de présentation (mock).

## Structure

```
p2p_social/
├── app.py              ← Application Flask principale
├── requirements.txt    ← Flask uniquement
└── templates/
    ├── base.html       ← Template de base (navbar, design system)
    ├── index.html      ← Feed principal (stories, posts, compose)
    ├── explore.html    ← Exploration / recherche / trending
    ├── wallet.html     ← Wallet Bitcoin mock
    ├── network.html    ← Visualisation topologie réseau
    └── profile.html    ← Profil utilisateur
```

## Déploiement sur PythonAnywhere

1. Créer un compte sur pythonanywhere.com
2. Ouvrir un Bash console
3. Cloner / uploader les fichiers :
   ```bash
   mkdir ~/mysite && cd ~/mysite
   # uploader les fichiers via Files tab ou git clone
   pip install flask
   ```
4. Dans l'onglet **Web** :
   - Add a new web app → Manual configuration → Python 3.10
   - WSGI file : remplacer le contenu par :
     ```python
     import sys
     sys.path.insert(0, '/home/VOTRE_USERNAME/mysite')
     from app import app as application
     ```
   - Working directory : `/home/VOTRE_USERNAME/mysite`
   - Cliquer **Reload**
5. Accéder à `VOTRE_USERNAME.pythonanywhere.com` 🎉

## Routes

| Route      | Description                        |
|------------|------------------------------------|
| `/`        | Feed principal avec stories & posts|
| `/explore` | Exploration trending & pairs       |
| `/wallet`  | Wallet Bitcoin (mock)              |
| `/network` | Topologie réseau P2P               |
| `/profile` | Profil utilisateur                 |

## Design

- Police : Syne (display) + DM Sans (corps) + JetBrains Mono
- Thème : Dark avec accents Rouge/Violet/Teal/Or
- Inspiré des apps sociales chinoises (addictivité, flux, stories)
- 100% CSS + JS vanilla, aucune dépendance frontend
# zeta_front
