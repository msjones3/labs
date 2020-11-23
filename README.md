# PyGame Start Here!
## What is Pygame?
Pygame is a “game library” - a set of tools to help programmers making games. Some of these things are:  

- Graphics and animation
- Sound (including music)
- Control (keyboard, mouse, gamepad, etc.)
{% next %}
## Game Loop
At the heart of every game is a loop, which we call the “Game Loop”. This loop is constantly running, over and over again, doing all the things that are needed to make the game work. Each time the game goes through this loop is called a frame.  

Each frame, many different things may happen, but they can be organized into three different categories:

1. Process Input (or Events)
This means anything from outside your game that you want to pay attention to - anything that you need the game to respond to. These may be keys being pressed on the keyboard, the mouse being clicked, etc.

2. Update Game
This means changing anything that needs to change on this frame. If a character is up in the air, gravity needs to pull it down. If two objects run into each other, they need to explode.

3. Render (or Draw)
In this step, we draw everything on the screen. Backgrounds, characters, menus, or anything else that the player needs to see must be drawn on the screen in its correct, updated location.
{% next %}

## Clock
One other important aspect of the loop is controlling how fast the whole loop runs. You may have heard the term FPS, which stands for Frames Per Second. This means how many times per second should this loop happen. This is important because you don’t want your game to run too fast or too slow. You also don’t want it to run at a different speed on different computers - if your character should take 10 seconds to run across the screen, that should be true no matter what computer it’s happening on.


{% next %}
## Building a Pygame Template
Now that we know what pieces we need to make the game work, we can start writing some code. To begin with, we’re going to make a simple pygame program that does nothing but open a window and run a game loop. This will be a great starting point for any pygame project you want to make.
{% next %}
At the top of our program, we’re going to import the libraries we need and set a few variables for our game options:  
`# Pygame template - skeleton for a new pygame project`
`import pygame`
`import random`

`WIDTH = 360  # width of our game window`  
`HEIGHT = 480 # height of our game window`  
`FPS = 30 # frames per second `  
{% next %}
Next we need to open the game window:  

`# initialize pygame and create window`  
`pygame.init()`  
`pygame.mixer.init()  # for sound`  
`screen = pygame.display.set_mode((WIDTH, HEIGHT))`  
`pygame.display.set_caption("My Game")`  
`clock = pygame.time.Clock()`  

{% next %}
`pygame.init()` is the command to start up pygame and “initialize” it (which is a fancy word for start). screen will refer to our game screen, and we create it at the size we set in our configuration constants. Finally, we create a clock so that we will be able to make sure our game runs at the FPS we want.

{% next %}
Now it’s time to make the game loop:

`# Game Loop`  
`running = True`  
`while running:`  
    `# Process input (events)`  
    `# Update`  
    `# Render (draw)`  
{% next %}
Here is our game loop, which is a `while` loop controlled by the variable `running`. If we ever want the game to end, we just have to set `running` to `False` and the loop will end. Now we can fill in each of the sections with some basic code.

## Render / Draw Section
We’ll start with the Draw section.  
We don’t have any characters yet, but we can fill the screen with a solid color. To do this, we need to talk about how computers handle color.

Computer screens are made up of pixels, and these pixels have 3 parts to them: red, green, and blue. How much each part is lit up determines what color that pixel is, like this:
{% spoiler %} The Answer to the Great Question... Of Life, the Universe and Everything... Is...

{% endspoiler %}

{% spoiler "Hint" %} You're really not going to like it. {% endspoiler %}

{% spoiler "Solution" %} Forty-two. {% endspoiler %}

{% video https://www.youtube.com/watch?v=oHg5SJYRHA0 %}
