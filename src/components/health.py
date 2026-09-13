class Health:

    def __init__(self, max_health=100):
        self.max_health = max_health
        self.health = max_health
        self.invulnerable = False
        self.invulnerable_timer = 0
        self.invulnerable_duration = 1.0

    def take_damage(self, amount):
        if self.invulnerable:
            return
        self.health -= amount
        if self.health < 0:
            self.health = 0
        self.invulnerable = True
        self.invulnerable_timer = 0

    def heal(self, amount):
        self.health += amount
        if self.health > self.max_health:
            self.health = self.max_health

    def update(self, dt):
        if self.invulnerable:
            self.invulnerable_timer += dt
            if self.invulnerable_timer >= self.invulnerable_duration:
                self.invulnerable = False

    def is_alive(self):
        return self.health > 0
