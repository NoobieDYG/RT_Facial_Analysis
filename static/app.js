
let statsInterval = null;

function startLive() {
    document.getElementById('video-feed').src = '/video_feed';
    resetStatsUpdater();
}

function startDemo() {
    document.getElementById('video-feed').src = '/demo_feed';
    resetStatsUpdater();
}

function downloadLogs(format) {
    window.location.href = `/download_logs?format=${format}`;
}

function resetStatsUpdater() {
    if (statsInterval) {
        clearInterval(statsInterval);
    }
    updateStats(); // fetch immediately
    statsInterval = setInterval(updateStats, 2000);
}

function updateStats() {
    fetch('/get_stats')
        .then(res => res.json())
        .then(data => {
            const statsDiv = document.getElementById('stats');
            statsDiv.innerHTML = '';

            if (data.length === 0) {
                statsDiv.innerHTML = "<p>No recent detections.</p>";
                return;
            }

            const latest = data[data.length - 1]; // 👈 only the last entry
            statsDiv.innerHTML = `
                <div class="stat-entry">
                    <b>Live Detection</b><br>
                    Gender: ${latest.gender}<br>
                    Age: ${latest.age}<br>
                    Emotion: ${latest.emotion}<br>
                    <small>${new Date(latest.timestamp).toLocaleTimeString()}</small>
                </div>`;
        })
        .catch(err => {
            console.error("Stats update failed:", err);
        });
}
