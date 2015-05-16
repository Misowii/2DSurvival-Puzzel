import pygame, sys;

from pygame.locals import *;

pygame.init();

windowSurface = pygame.display.set_mode((500, 400), 0, 32);
pygame.display.set_caption('Testing!');

BLACK = (0, 0, 0);
WHITE = (255, 255, 255);
RED = (255, 0, 0);
GREEN = (0, 255, 0);
BLUE = (0, 0, 255);

basicFont = pygame.font.SysFont(None, 48);

text = basicFont.render("Hello world!", True, WHITE, BLUE);
textRect = text.get_rect();
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# draw the white background onto the surface

windowSurface.fill(WHITE)

# draw the text's background rectangle onto the surface

pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

# get a pixel array of the surface

pixArray = pygame.PixelArray(windowSurface)

pixArray[480][380] = BLACK

del pixArray

# draw the text onto the surface

windowSurface.blit(text, textRect)

# draw the window onto the screen

pygame.display.update()

# run the game loop

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

pygame.display.update()
time.sleep(.02)


