window.onload = function() {
    var startButton = document.getElementById('start-button');
    var shipLanding = document.getElementById('ship-landing');
    var staticShip = document.getElementById('static-ship');

    console.log('Page loaded. Ready to start sequence.');

    // Start sequence when the start button is clicked
    startButton.onclick = function() {
        console.log('Start button clicked.');
        startButton.innerText = "Signal received...";

        // Change the text after 1.5 seconds
        setTimeout(function() {
            startButton.innerText = "Warping to coordinates...";
            console.log('Text changed to warping sequence.');

            // Start the landing sequence after another 1.5 seconds
            setTimeout(function() {
                startButton.style.display = 'none'; // Hide the button
                shipLanding.style.display = 'block'; // Show the ship landing gif
                console.log('Ship landing sequence started.');

                // Continue with the rest of the sequence after the gif finishes
                setTimeout(function() {
                    shipLanding.style.display = 'none';
                    console.log('Ship landing sequence finished.');
                    staticShip.style.display = 'block'; // Show the static ship image
                    document.getElementById('character').style.display = 'block'; // Make the character visible
                }, 5000); // Adjust this to the length of your gif
            }, 1500);
        }, 1500);
    };
};

function activateCharacterMovement() {
    document.addEventListener('keydown', function(event) {
        const characterElement = document.getElementById('character');
        let bottom = parseInt(window.getComputedStyle(characterElement).bottom);
        let left = parseInt(window.getComputedStyle(characterElement).left);

        switch(event.key) {
            case 'ArrowUp':
                characterElement.style.bottom = `${bottom + 5}px`; // Move up
                break;
            case 'ArrowDown':
                characterElement.style.bottom = `${bottom - 5}px`; // Move down
                break;
            case 'ArrowLeft':
                characterElement.style.left = `${left - 5}px`; // Move left
                break;
            case 'ArrowRight':
                characterElement.style.left = `${left + 5}px`; // Move right
                break;
        }
    });
}

// Call this function at the end of your game start sequence
activateCharacterMovement();