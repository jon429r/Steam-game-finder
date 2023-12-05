let toggle = () => {
    let element2 = document.getElementById("LinkList");
    element2.toggleAttribute("hidden");
}

function showResults() {
    let element = document.getElementById("Result_Table");
    element.style.display = "table";
}

function likeGame(game_id) {
    fetch(`/like/${game_id}/`)
        .then(response => response.json())
        .then(data => {
            updateCount(game_Id, 'like', data.likes);
            console.log('Liked:', game_id);
        });
}

function dislikeGame(game_id) {
    fetch(`/dislike/${game_id}/`)
        .then(response => response.json())
        .then(data => {
            updateCount(game_id, 'dislike', data.dislikes);
            console.log('Disliked:', game_id);
        });
}

function updateCount(game_id, action, count) {
    document.getElementById(`likes_${game_id}`).innerText = (action === 'like') ? count : document.getElementById(`likes_${game_id}`).innerText;
    document.getElementById(`dislikes_${game_id}`).innerText = (action === 'dislike') ? count : document.getElementById(`dislikes_${game_id}`).innerText;
}

var game_id = 123; 
$.ajax({
    url: '/myapp/like_game/' + game_id + '/',
    method: 'POST',
});