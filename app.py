from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

MOCK_POSTS = [
    {
        "id": 1,
        "user": "cryptonova_88",
        "avatar": "CN",
        "avatar_color": "#FF3B5C",
        "fingerprint": "a3f8c1d2",
        "verified": True,
        "time": "2m",
        "content": "Le réseau décentralisé ne ment jamais. Vos données, votre liberté. Rejoignez le mouvement P2P 🔐",
        "likes": 2841,
        "comments": 143,
        "reposts": 89,
        "tags": ["#P2P", "#Décentralisé", "#Crypto"],
        "media": None,
        "btc": "1A2B3C4D5E6F",
    },
    {
        "id": 2,
        "user": "zerochain_labs",
        "avatar": "ZL",
        "avatar_color": "#7B2FFF",
        "fingerprint": "b91e44fa",
        "verified": True,
        "time": "8m",
        "content": "Notre nœud vient de relayer 14 000 messages en 1h sans aucun serveur central. La révolution est silencieuse. ⚡",
        "likes": 5102,
        "comments": 312,
        "reposts": 204,
        "tags": ["#Node", "#Relay", "#Web3"],
        "media": "network",
        "btc": None,
    },
    {
        "id": 3,
        "user": "alice_phantom",
        "avatar": "AP",
        "avatar_color": "#00C9A7",
        "fingerprint": "f44c9b01",
        "verified": False,
        "time": "15m",
        "content": "Envoyé 500 sats à un inconnu en Corée. Transaction confirmée en 3 secondes. Aucune banque. Aucun intermédiaire. Juste nous deux. 🌐💸",
        "likes": 9873,
        "comments": 761,
        "reposts": 1023,
        "tags": ["#Bitcoin", "#Liberté", "#P2P"],
        "media": None,
        "btc": "1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2",
    },
    {
        "id": 4,
        "user": "mesh_weaver",
        "avatar": "MW",
        "avatar_color": "#FF6B35",
        "fingerprint": "2c7d8e9a",
        "verified": True,
        "time": "1h",
        "content": "Votre IP ne vous définit pas. Votre fingerprint si. Nouvelle identité cryptographique disponible sur le réseau 🎭",
        "likes": 3456,
        "comments": 234,
        "reposts": 178,
        "tags": ["#Anonymat", "#Identité", "#Crypto"],
        "media": "code",
        "btc": None,
    },
    {
        "id": 5,
        "user": "satoshi_heir",
        "avatar": "SH",
        "avatar_color": "#F7B731",
        "fingerprint": "9e1b2c3d",
        "verified": False,
        "time": "2h",
        "content": "Topologie du réseau ce matin : 847 nœuds actifs, 23 relays opérationnels, latence moyenne 42ms. On scale 🚀",
        "likes": 7234,
        "comments": 489,
        "reposts": 345,
        "tags": ["#Stats", "#Network", "#Topology"],
        "media": "stats",
        "btc": "3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc5",
    },
]

STORIES = [
    {"user": "vous", "avatar": "+", "avatar_color": "#FF3B5C", "active": False, "is_self": True},
    {"user": "cryptonova", "avatar": "CN", "avatar_color": "#FF3B5C", "active": True, "is_self": False},
    {"user": "zerochain", "avatar": "ZL", "avatar_color": "#7B2FFF", "active": True, "is_self": False},
    {"user": "alice_p", "avatar": "AP", "avatar_color": "#00C9A7", "active": False, "is_self": False},
    {"user": "mesh_w", "avatar": "MW", "avatar_color": "#FF6B35", "active": True, "is_self": False},
    {"user": "satoshi", "avatar": "SH", "avatar_color": "#F7B731", "active": False, "is_self": False},
    {"user": "node_42", "avatar": "N4", "avatar_color": "#E91E63", "active": True, "is_self": False},
]

TRENDING = [
    {"tag": "#P2P", "posts": "42.1K"},
    {"tag": "#Bitcoin", "posts": "128.4K"},
    {"tag": "#Décentralisé", "posts": "18.9K"},
    {"tag": "#Mesh", "posts": "7.2K"},
    {"tag": "#Relay", "posts": "5.8K"},
]

@app.route('/')
def index():
    return render_template('index.html', posts=MOCK_POSTS, stories=STORIES, trending=TRENDING)

@app.route('/explore')
def explore():
    return render_template('explore.html', trending=TRENDING)

@app.route('/wallet')
def wallet():
    return render_template('wallet.html')

@app.route('/network')
def network():
    return render_template('network.html')

@app.route('/profile')
def profile():
    return render_template('profile.html', posts=MOCK_POSTS[:3])

@app.route('/notifications')
def notifications():
    return render_template('notifications.html')

@app.route('/messages')
def messages():
    return render_template('messages.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

if __name__ == '__main__':
    app.run(debug=True)
