import os
import pygame
import time
import random
 
class image_display:
#Based on adafruit's pyscope code
#Found here: http://learn.adafruit.com/pi-video-output-using-pygame/overview
    screen = None;
    
    def __init__(self):
        "Ininitializes a new pygame screen using the framebuffer"
        # Based on "Python GUI in Linux frame buffer"
        # http://www.karoltomala.com/blog/?p=679
        disp_no = os.getenv("DISPLAY")
        if disp_no:
            print "I'm running under X display = {0}".format(disp_no)
        
        # Check which frame buffer drivers are available
        # Start with fbcon since directfb hangs with composite output
        drivers = ['fbcon', 'directfb', 'svgalib']
        found = False
        for driver in drivers:
            # Make sure that SDL_VIDEODRIVER is set
            if not os.getenv('SDL_VIDEODRIVER'):
                os.putenv('SDL_VIDEODRIVER', driver)
            try:
                pygame.display.init()
            except pygame.error:
                print 'Driver: {0} failed.'.format(driver)
                continue
            found = True
            break
    
        if not found:
            raise Exception('No suitable video driver found!')
        
        size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        print "Framebuffer size: %d x %d" % (size[0], size[1])
        self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        # Clear the screen to start
        self.screen.fill((0, 0, 0))        
        # Initialise font support
        pygame.font.init()
        # Render the screen
        pygame.display.update()
 
    def __del__(self):
        "Destructor to make sure pygame shuts down, etc."
 
    def display_images(self, image_array, sleep_time):
        # runs through a list of images and displays them to the screen
        for image in image_array:
            picture = pygame.image.load('/home/pi/images/' + image)
            main_surface = pygame.display.get_surface()
            main_surface.blit(picture, (0,0))
            # Update the display
            pygame.display.update()
            time.sleep(sleep_time)
    
 

# Create an instance of the PyScope class
image_display = image_display()
fileList = os.listdir('/home/pi/images')
image_display.display_images(fileList, 20)
