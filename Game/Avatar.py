class Avatar:
    def __init__(self, imagem, nome, posx, posy):
        self.imagem = imagem
        self.score = 0
        self.nome = nome
        self.pos = Vector2()
        self.pos.x = posx
        self.pos.y = posy
        self.andar = False
        
        
    def movimentar(self):
        v = pygame.Vector2()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                v.x = 1
            if event.key == pygame.K_a:
                v.x = -1
            if event.key == pygame.K_w:
                v.y = -1
            if event.key == pygame.K_s:
                v.y = 1
            self.andar = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                v.x = 0
            if event.key == pygame.K_a:
                v.x = 0
            if event.key == pygame.K_w:
                v.y = 0
            if event.key == pygame.K_s:
                v.y = 0
            self.andar = False

        if self.andar == True:
            self.pos += v

    def desenhar(self, surface):
        surface.blit(imagem, posicao)

    
