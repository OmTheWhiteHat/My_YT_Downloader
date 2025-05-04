from flask import Flask, render_template, request, send_file, jsonify, after_this_request
import os
import yt_dlp
import platform
from pathlib import Path
import re
import tempfile

app = Flask(__name__, template_folder='template', static_folder='static')


@app.route('/', methods=['GET', 'POST'])
def index():
    thumbnail_url = None
    title = None
    filename = None
    format_choice = None
    resolution = None
    url = None

    if request.method == 'POST':
        url = request.form['url']
        format_choice = request.form['format']
        resolution = request.form.get('resolution')

        try:
            ydl_opts = {
                'quiet': True,
                'skip_download': True,
                'extract_flat': False
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                title = info.get('title', 'Untitled')
                thumbnail_url = info.get('thumbnail', None)
                ext = 'mp3' if format_choice == 'mp3' else 'mp4'
                filename = f"{title.replace(' ', '_').replace('/', '_')}.{ext}"

            return render_template(
                'index.html',
                thumbnail_url=thumbnail_url,
                title=title,
                filename=filename,
                url=url,
                format_choice=format_choice,
                resolution=resolution
            )
        except Exception as e:
            return f"Error fetching video info: {e}"

    return render_template(
        'index.html',
        thumbnail_url=thumbnail_url,
        title=title,
        filename=filename,
        url=url,
        format_choice=format_choice,
        resolution=resolution
    )


@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    format_choice = request.form['format']
    resolution = request.form.get('resolution') if format_choice == 'mp4' else None
    title = request.form.get('title', 'Untitled')

    safe_title = title.replace(' ', '_').replace('/', '_')

    temp_dir = tempfile.mkdtemp()
    outtmpl = os.path.join(temp_dir, f"{safe_title}.%(ext)s")

    ydl_opts = {
        'outtmpl': outtmpl,
        'quiet': True,
        'noplaylist': True,
        'prefer_ffmpeg': True
    }

    if format_choice == 'mp3':
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
    else:
        ydl_opts.update({
            'format': f'bestvideo[height={resolution}]+bestaudio/best' if resolution else 'bestvideo+bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }],
            'merge_output_format': 'mp4',
            'keepvideo': False
        })

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)

            downloaded_path = None
            if 'requested_downloads' in info:
                for item in info['requested_downloads']:
                    if 'filepath' in item:
                        downloaded_path = item['filepath']
                        break

            if not downloaded_path or not os.path.isfile(downloaded_path):
                return "Error: File not found after download."

        # Schedule cleanup after response is sent
        @after_this_request
        def cleanup(response):
            try:
                os.remove(downloaded_path)
                os.rmdir(temp_dir)
            except Exception as cleanup_error:
                print(f"Cleanup error: {cleanup_error}")
            return response

        return send_file(downloaded_path, as_attachment=True)

    except Exception as e:
        return f"Error during download: {e}"

@app.route('/resolutions', methods=['POST'])
def get_resolutions():
    try:
        data = request.get_json(force=True)
        raw_url = data.get('url')

        if not raw_url:
            return jsonify({'error': 'No URL provided'}), 400

        ydl_opts = {
            'quiet': True,
            'skip_download': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(raw_url, download=False)
            resolutions = list({f"{f['height']}" for f in info['formats'] if f.get('vcodec') != 'none' and f.get('height')})

            resolutions = sorted(resolutions, key=lambda x: int(x), reverse=True)
            return jsonify({'resolutions': resolutions})

    except Exception as e:
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)
