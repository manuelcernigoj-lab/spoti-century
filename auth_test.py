import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()

auth_manager = SpotifyClientCredentials(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
)
sp = spotipy.Spotify(auth_manager=auth_manager)

# --- TEST DI CONNESSIONE ---
def test_connessione():
    print("🔍 Test in corso...")
    try:
        # Cerchiamo un brano famosissimo invece di una playlist
        risultato = sp.search(q="Albachiara", type="track", limit=1)
        
        # Verifichiamo se abbiamo ottenuto qualcosa
        tracks = risultato.get("tracks", {}).get("items", [])
        
        if tracks:
            canzone = tracks[0]
            print(f"✅ Connessione riuscita!")
            print(f"🎵 Brano trovato: {canzone['name']} - Artista: {canzone['artists'][0]['name']}")
        else:
            print("⚠️ Connesso, ma nessun brano trovato. Controlla i permessi sulla Dashboard.")
            
    except Exception as e:
        print(f"❌ Errore durante il test: {e}")

if __name__ == "__main__":
    test_connessione()