function rgbToHex(r, g, b) {
    const hex = (x) => x.toString(16).padStart(2, '0');
    return `#${hex(r)}${hex(g)}${hex(b)}`;
  }
  
  window.onload = function() {
    const towerContainer = document.getElementById("tower-container");
    const modalContent = document.getElementById('modal-content');  // Assuming you have a modal with id 'modal-content'
  
    for (let i = 0; i <= 94; i++) {
      const towerButton = document.createElement("button");
      towerButton.classList.add("tower-button");
  
      const towerImage = document.createElement("img");
      towerImage.src = `../../media/test_images/towers_png6/tower_${i}.png`;
      towerImage.alt = `Tower ${i}`;
  
      towerButton.appendChild(towerImage);
  
      // Generate random color
      const red = Math.floor(Math.random() * 256);
      const green = Math.floor(Math.random() * 256);
      const blue = Math.floor(Math.random() * 256);
      const colorHex = rgbToHex(red, green, blue);
  
      // Add hover effect
      towerButton.addEventListener("mouseover", function() {
        towerButton.style.boxShadow = `0px 0px 15px 3px ${colorHex}`;
      });
      towerButton.addEventListener("mouseout", function() {
        towerButton.style.boxShadow = 'none';
      });
  
      // Add click event to open SVG in modal
      towerButton.addEventListener("click", function() {
        modalContent.innerHTML = `<object type="image/svg+xml" data="../../media/towers_svg/tower_${i}.svg">Your browser does not support SVG</object>`;
        document.getElementById('tower-modal').style.display = "block";
      });
  
        const modal = document.getElementById("tower-modal");
        const closeButton = document.getElementById("close-button");

        closeButton.onclick = function() {
            modal.style.display = "none";
          };
          window.onclick = function(event) {
            if (event.target === modal) {
              modal.style.display = "none";
            }
          };
        towerContainer.appendChild(towerButton);
    }
  };
  