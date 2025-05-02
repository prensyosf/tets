document.addEventListener('DOMContentLoaded', () => {
    const screamSound = document.getElementById("scream-sound");
    document.querySelectorAll('button, a').forEach(el => {
        el.addEventListener('click', () => {
            screamSound.currentTime = 0;
            screamSound.play(play);
        });
    });
});
