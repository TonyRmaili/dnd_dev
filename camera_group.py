import pygame
from char3 import Character


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.offset = pygame.math.Vector2()

        # free roam attributes
        self.speed = 20
        self.direction = pygame.math.Vector2()
      
    def target_acter(self,acter):      
        self.offset.x = acter.rect.centerx - self.half_w
        self.offset.y = acter.rect.centery - self.half_h

        
    def free_roam(self,camera_pos):
        self.offset.x = camera_pos[0] -self.half_w
        self.offset.y = camera_pos[1] -self.half_h

        
            
    def custom_draw(self,screen): 
        
        # should be in init but loading screen error     
        self.half_w = screen.get_size()[0] // 2
        self.half_h = screen.get_size()[1] // 2

        for sprite in self.sprites():
        
            self.offset_pos = sprite.rect.topleft - self.offset

            if type(sprite) == Character:
                sprite.offset_pos = self.offset_pos           
                sprite.offset_rect = pygame.rect.Rect(sprite.offset_pos[0],
                                        sprite.offset_pos[1],
                                        sprite.size,sprite.size)
            
        

            screen.blit(sprite.image,self.offset_pos)

    
        
    