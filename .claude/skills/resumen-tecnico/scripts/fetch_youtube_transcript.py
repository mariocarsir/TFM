#!/usr/bin/env python3
"""
Extrae la transcripción de un vídeo de YouTube.
Soporta español e inglés; falla explícitamente si no hay transcripción disponible.
"""

import sys
import json
from urllib.parse import urlparse, parse_qs

try:
    from youtube_transcript_api import YouTubeTranscriptApi
except ImportError:
    YouTubeTranscriptApi = None


def extract_video_id(url: str) -> str:
    """
    Extrae el ID de vídeo de una URL de YouTube.
    Soporta: youtube.com/watch?v=ID, youtu.be/ID, youtube.com/embed/ID
    """
    # youtu.be/ID
    if 'youtu.be/' in url:
        return url.split('youtu.be/')[-1].split('?')[0].split('&')[0]

    # youtube.com/watch?v=ID
    if 'youtube.com' in url:
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        if 'v' in params:
            return params['v'][0]
        # youtube.com/embed/ID
        if '/embed/' in url:
            return url.split('/embed/')[-1].split('?')[0]

    return None


def fetch_transcript(url: str) -> dict:
    """
    Extrae la transcripción de YouTube.

    Retorna:
        {
            'video_id': str,
            'title': str,
            'language': str,
            'text': str,
            'timestamp_entries': list[dict],  # {'time': str, 'text': str}
            'error': str or None
        }
    """
    if YouTubeTranscriptApi is None:
        return {
            'video_id': '',
            'title': url,
            'language': '',
            'text': '',
            'timestamp_entries': [],
            'error': 'youtube-transcript-api no está instalado. Instala con: pip install youtube-transcript-api'
        }

    video_id = extract_video_id(url)
    if not video_id:
        return {
            'video_id': '',
            'title': url,
            'language': '',
            'text': '',
            'timestamp_entries': [],
            'error': 'No se pudo extraer el ID de vídeo de la URL'
        }

    try:
        # Intenta en español primero, luego inglés
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['es'])
            language = 'es'
        except:
            try:
                transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
                language = 'en'
            except:
                # Intenta con cualquier idioma disponible
                transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
                available = transcript_list.get_available_transcripts()
                if available:
                    transcript = available[0].fetch()
                    language = available[0].language
                else:
                    return {
                        'video_id': video_id,
                        'title': url,
                        'language': '',
                        'text': '',
                        'timestamp_entries': [],
                        'error': 'Este vídeo no tiene transcripciones disponibles habilitadas'
                    }

        # Formatea la transcripción
        text_parts = [entry['text'] for entry in transcript]
        full_text = ' '.join(text_parts)

        # Convierte tiempos a formato legible (HH:MM:SS)
        timestamp_entries = []
        for entry in transcript:
            seconds = int(entry['start'])
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            secs = seconds % 60
            time_str = f"{hours:02d}:{minutes:02d}:{secs:02d}" if hours > 0 else f"{minutes:02d}:{secs:02d}"
            timestamp_entries.append({
                'time': time_str,
                'text': entry['text']
            })

        return {
            'video_id': video_id,
            'title': url,
            'language': language,
            'text': full_text,
            'timestamp_entries': timestamp_entries,
            'error': None
        }

    except Exception as e:
        return {
            'video_id': video_id,
            'title': url,
            'language': '',
            'text': '',
            'timestamp_entries': [],
            'error': f'Error al extraer transcripción: {str(e)}'
        }


def format_for_markdown(extracted: dict) -> str:
    """
    Formatea la transcripción como Markdown con marcas de tiempo.
    """
    if extracted['error']:
        return f"# Error\n\n{extracted['error']}\n\nURL: {extracted['title']}"

    output = [
        f"# Transcripción de vídeo\n",
        f"**Vídeo:** {extracted['title']}",
        f"**ID:** {extracted['video_id']}",
        f"**Idioma:** {extracted['language']}\n",
        "## Transcripción con tiempos\n"
    ]

    for entry in extracted['timestamp_entries']:
        output.append(f"**{entry['time']}** — {entry['text']}")

    return '\n'.join(output)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(json.dumps({
            'error': 'Uso: fetch_youtube_transcript.py <url-youtube>',
            'video_id': '',
            'title': '',
            'language': '',
            'text': '',
            'timestamp_entries': []
        }))
        sys.exit(1)

    url = sys.argv[1]
    result = fetch_transcript(url)

    if '--json' in sys.argv:
        print(json.dumps(result))
    else:
        print(format_for_markdown(result))
