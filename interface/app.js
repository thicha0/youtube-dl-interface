const API_URL = 'http://localhost:5000';

const urlInput = document.getElementById('urlInput');
const videoBtn = document.getElementById('videoBtn');
const audioBtn = document.getElementById('audioBtn');
const downloadBtn = document.getElementById('downloadBtn');
const btnText = document.getElementById('btnText');
const spinner = document.getElementById('spinner');
const message = document.getElementById('message');

let format = 'video';

videoBtn.addEventListener('click', () => {
    format = 'video';
    videoBtn.classList.add('active');
    audioBtn.classList.remove('active');
});

audioBtn.addEventListener('click', () => {
    format = 'audio';
    audioBtn.classList.add('active');
    videoBtn.classList.remove('active');
});

downloadBtn.addEventListener('click', async () => {
    const url = urlInput.value.trim();

    if (!url) {
        showMessage('Please enter a YouTube URL', 'error');
        return;
    }

    setLoading(true);
    clearMessage();

    try {
        const response = await fetch(`${API_URL}/youtube_dl/q`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ url, format }),
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error || 'Download failed');
        }

        const filename = response.headers.get('x-filename') || 'download';
        const blob = await response.blob();
        downloadBlob(filename, blob);
        showMessage('Download completed!', 'success');
    } catch (error) {
        showMessage(error.message || 'An error occurred', 'error');
    } finally {
        setLoading(false);
    }
});

function downloadBlob(filename, blob) {
    const url = window.URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = decodeURIComponent(escape(filename));
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    window.URL.revokeObjectURL(url);
}

function setLoading(loading) {
    downloadBtn.disabled = loading;
    btnText.textContent = loading ? 'Downloading...' : 'Download';
    spinner.classList.toggle('hidden', !loading);
}

function showMessage(text, type) {
    message.textContent = text;
    message.className = `message ${type}`;
}

function clearMessage() {
    message.textContent = '';
    message.className = 'message';
}

urlInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        downloadBtn.click();
    }
});
