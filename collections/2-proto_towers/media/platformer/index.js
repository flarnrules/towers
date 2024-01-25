const canvas = document.querySelector('canvas')
const c = canvas.getContext('2d')
canvas.width = 768
canvas.height = 768

const floorCollisions2D = []
for (let i = 0; i < floorCollisions.length; i += 32) {
    floorCollisions2D.push(floorCollisions.slice(i, i + 32))
}

const collisionBlocks = []
floorCollisions2D.forEach((row, y) => {
    row.forEach((symbol, x) => {
        if(symbol === 1) {
            console.log('draw a block here!')
            collisionBlocks.push(
                new CollisionBlock({
                position: {
                    x: x * 24,
                    y: y * 24,
                },
            }))
        }

    })
})

console.log(collisionBlocks)

const gravity = 0.5

const player = new Player({
    x: 0,
    y: 0,
})
const player2 = new Player({
    x: 300,
    y: 100,
})

const keys = {
    d: {
        pressed: false,

    },
    a: {
        pressed: false,
        
    },
}

const background = new Sprite({
    position: {
        x: 0,
        y: 0,
    },
    imageSrc: './img/background.png',
})

function animate() {
    window.requestAnimationFrame(animate)
    //background
    c.fillStyle= 'white'
    c.fillRect(0, 0, canvas.width, canvas.height)
    background.update()

    //collision blocks
    collisionBlocks.forEach(collisionBlock => {
        collisionBlock.update()
    })

    //player character
    player.update()
    player2.update()

    player.velocity.x = 0
    if (keys.d.pressed) player.velocity.x = 5
        else if (keys.a.pressed) player.velocity.x = -5
}

animate()

window.addEventListener('keydown', (event) => {
    switch (event.key) {
        case 'd':
            keys.d.pressed = true
            break
        case 'a':
            keys.a.pressed = true
            break
        case 'w':
            player.velocity.y = -15
            break
    }
})

window.addEventListener('keyup', (event) => {
    switch (event.key) {
        case 'd':
            keys.d.pressed = false
            break
        case 'a':
            keys.a.pressed = false
            break
    }
})