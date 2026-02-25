#!/usr/bin/env python3
"""
Simple HTTP Server to test the contact form locally
Run this script and open http://localhost:8000 in your browser
"""

import utils.transport
import utils.session
import http.server
import socketserver
import os

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers to allow form submission
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def run_server():
    handler = MyHTTPRequestHandler
    
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"✓ Server running at http://localhost:{PORT}")
        print(f"✓ Open http://localhost:{PORT}/contact-form-updated.html in your browser")
        print(f"✓ Press Ctrl+C to stop the server")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n✓ Server stopped")

if __name__ == "__main__":
    run_server()
