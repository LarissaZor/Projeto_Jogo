import pygame


print("Setup Start")
#ctrl+alt+l --- organiza o código de acordo com a pep(retira spaces)
pygame.init()
window = pygame.display.set_mode(size=(800,480))
print("Setup End")


print("Loop Start")
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quit..")
            pygame.quit() # Close window
            quit()

