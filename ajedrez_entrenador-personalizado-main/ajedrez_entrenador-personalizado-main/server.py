#!/usr/bin/env python3
"""
Simple HTTP server to run Chess Openings Trainer locally.
Can be started with:
    python3 server.py
"""

import http.server
import socketserver
import webbrowser
import os
import sys
import json
import subprocess

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))
PROFILE_FILE = os.path.join(DIRECTORY, 'perfil_jugador.json')

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Desactivar cache para archivos JSON y endpoints de API
        if self.path.endswith('.json') or self.path.startswith('/api/'):
            self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Expires', '0')
        # Habilitar CORS para peticiones locales
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        clean_path = self.path.split('?')[0]
        if clean_path in ('/api/profile', '/api/get-profile'):
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            if os.path.exists(PROFILE_FILE):
                with open(PROFILE_FILE, 'rb') as f:
                    self.wfile.write(f.read())
            else:
                default_data = {
                    "name": "Jugador",
                    "elo": 1200,
                    "gamesPlayed": 0,
                    "wins": 0,
                    "losses": 0,
                    "draws": 0,
                    "history": [],
                    "openingStats": {},
                    "practiceStats": {},
                    "lastUpdated": ""
                }
                self.wfile.write(json.dumps(default_data, indent=2, ensure_ascii=False).encode('utf-8'))
            return

        super().do_GET()

    def do_POST(self):
        clean_path = self.path.split('?')[0]
        if clean_path == '/api/git-push':
            try:
                subprocess.run(['git', 'add', 'perfil_jugador.json'], check=True, capture_output=True)
                res_commit = subprocess.run(['git', 'commit', '-m', 'Auto-guardado: Actualizar ELO e historial'], capture_output=True)
                res_push = subprocess.run(['git', 'push'], check=True, capture_output=True)
                
                msg = "Progreso subido a Git correctamente."
                if res_commit.returncode != 0 and b"nothing to commit" in res_commit.stdout:
                    msg = "No hay cambios nuevos para subir, ya está actualizado."

                response_bytes = json.dumps({"status": "ok", "message": msg}).encode('utf-8')
                self.send_response(200)
            except subprocess.CalledProcessError as e:
                err_msg = e.stderr.decode('utf-8', errors='replace') if e.stderr else str(e)
                response_bytes = json.dumps({"status": "error", "message": f"Error de Git: {err_msg}"}).encode('utf-8')
                self.send_response(500)
            except Exception as e:
                response_bytes = json.dumps({"status": "error", "message": str(e)}).encode('utf-8')
                self.send_response(500)

            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Content-Length', str(len(response_bytes)))
            self.end_headers()
            self.wfile.write(response_bytes)
            return

        if clean_path in ('/api/save-profile', '/api/profile', '/save-profile'):
            try:
                content_length = int(self.headers.get('Content-Length', 0))
                post_data = self.rfile.read(content_length)
                data = json.loads(post_data.decode('utf-8'))

                # Guardar de forma segura en perfil_jugador.json
                with open(PROFILE_FILE, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)

                response_bytes = json.dumps({
                    "status": "ok",
                    "message": "Perfil guardado correctamente en perfil_jugador.json"
                }).encode('utf-8')

                self.send_response(200)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.send_header('Content-Length', str(len(response_bytes)))
                self.end_headers()
                self.wfile.write(response_bytes)
            except Exception as e:
                err_bytes = json.dumps({"status": "error", "message": str(e)}).encode('utf-8')
                self.send_response(500)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.send_header('Content-Length', str(len(err_bytes)))
                self.end_headers()
                self.wfile.write(err_bytes)
            return

        self.send_response(404)
        self.end_headers()

    def log_message(self, format, *args):
        # Mantener limpia la consola
        sys.stderr.write(f"[{self.log_date_time_string()}] {format % args}\n")

def run():
    os.chdir(DIRECTORY)
    port = PORT
    socketserver.TCPServer.allow_reuse_address = True
    for attempt in range(10):
        try:
            with socketserver.TCPServer(("", port), Handler) as httpd:
                url = f"http://localhost:{port}"
                print("=" * 60)
                print("♟️  ENTRENADOR DE APERTURAS DE AJEDREZ - INICIADO")
                print("=" * 60)
                print(f" Servidor disponible en: {url}")
                print(f" Carpeta del proyecto:   {DIRECTORY}")
                print(f" Archivo de ELO y perfil: {PROFILE_FILE}")
                print(" Presiona Ctrl+C para detener el servidor.")
                print("=" * 60)

                httpd.serve_forever()
                break
        except OSError:
            port += 1

if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        print("\nServidor detenido.")
