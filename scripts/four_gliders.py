"""Play Life with two colliding gliders."""
from life import Game, Pattern, glider

g = Game(30)
g.insert(Pattern(glider), [1, 1])
g.insert(Pattern(glider).flip_horizontal(), [1, 28])
g.insert(Pattern(glider).rotate(2), [28, 28])
g.insert(Pattern(glider).flip_vertical(), [28, 1])
g.play()
