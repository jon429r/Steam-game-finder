let toggle = () => {
    let element2 = document.getElementById("LinkList");
    element2.toggleAttribute("hidden");
}

function showResults() {
    let element = document.getElementById("Result_Table");
    element.style.display = "table";
}

function likeGame(gameId) {
    fetch(`/like/${gameId}/`)
        .then(response => response.json())
        .then(data => {
            updateCount(gameId, 'like', data.likes);
        });
}

function dislikeGame(gameId) {
    fetch(`/dislike/${gameId}/`)
        .then(response => response.json())
        .then(data => {
            updateCount(gameId, 'dislike', data.dislikes);
        });
}

function updateCount(gameId, action, count) {
    document.getElementById(`likes_${gameId}`).innerText = (action === 'like') ? count : document.getElementById(`likes_${gameId}`).innerText;
    document.getElementById(`dislikes_${gameId}`).innerText = (action === 'dislike') ? count : document.getElementById(`dislikes_${gameId}`).innerText;
}