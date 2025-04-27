function startCanvas() {
    fetch('/start_canvas', { method: 'POST' })
        .then(response => {
            // Handle the response, if needed
        })
        .catch(error => {
            console.error('Error:', error);
        });
}
