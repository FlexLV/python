import tkinter as tk

class Spaceship:

    def __init__(self, canvas, x, y, width=50, height=20, color="blue", speed=15):
        self.canvas = canvas
        self.speed = speed
        self.id = canvas.create_rectangle(
            x - width / 2,
            y - height / 2,
            x + width / 2,
            y + height / 2,
            fill=color,
        )

    def move(self, dx, dy):
        self.canvas.move(self.id, dx, dy)
        x1, y1, x2, y2 = self.canvas.coords(self.id)
        width = int(self.canvas["width"])
        height = int(self.canvas["height"])
        fix_x = 0
        fix_y = 0
        if x1 < 0:
            fix_x = -x1
        if x2 > width:
            fix_x = width - x2
        if y1 < 0:
            fix_y = -y1
        if y2 > height:
            fix_y = height - y2
        if fix_x or fix_y:
            self.canvas.move(self.id, fix_x, fix_y)

    def get_coords(self):
        return self.canvas.coords(self.id)

class Defender(Spaceship):
    def move_left(self, event=None):
        self.move(-self.speed, 0)

    def move_right(self, event=None):
        self.move(self.speed, 0)

    def shoot(self):
        x1, y1, x2, y2 = self.get_coords()
        mid_x = (x1 + x2) / 2
        return Bullet(self.canvas, mid_x, y1)

class Bullet:
    def __init__(self, canvas, x, y, speed=-10):
        self.canvas = canvas
        self.speed = speed
        self.id = canvas.create_rectangle(x - 2, y - 10, x + 2, y, fill="white")

    def update(self):
        self.canvas.move(self.id, 0, self.speed)
        x1, y1, x2, y2 = self.canvas.coords(self.id)
        if y2 < 0:
            self.canvas.delete(self.id)
            return False
        return True

    def destroy(self):
        self.canvas.delete(self.id)

class GameApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Space Invaders")

        self.canvas_width = 800
        self.canvas_height = 500
        self.canvas = tk.Canvas(
            self.root,
            width=self.canvas_width,
            height=self.canvas_height,
            bg="black",
        )
        self.canvas.pack()

        self.defender = Defender(
            self.canvas,
            self.canvas_width / 2,
            self.canvas_height - 40,
        )

        self.bullets = []
        self.enemies = []

        self.enemy_direction = 1
        self.enemy_speed = 3
        self.enemy_drop = 20

        self.score = 0
        self.score_text = self.canvas.create_text(
            10,
            10,
            anchor="nw",
            fill="white",
            font=("Arial", 16),
            text=f"Score: {self.score}",
        )

        self.game_over = False

        self.spawn_pyramid_enemies(rows=5)

        self.root.bind("<Left>", self.defender.move_left)
        self.root.bind("<Right>", self.defender.move_right)
        self.root.bind("<space>", self.handle_shoot)

        self.game_loop()

    def spawn_pyramid_enemies(self, rows):
        spacing_x = 60
        spacing_y = 50
        start_y = 50
        for row in range(rows):
            count = row + 1
            total_width = (count - 1) * spacing_x
            start_x = self.canvas_width // 2 - total_width // 2
            for col in range(count):
                x = start_x + col * spacing_x
                y = start_y + row * spacing_y
                enemy = self.canvas.create_rectangle(
                    x - 20,
                    y - 10,
                    x + 20,
                    y + 10,
                    fill="red",
                )
                self.enemies.append(enemy)

    def handle_shoot(self, event=None):
        if self.game_over:
            return
        bullet = self.defender.shoot()
        self.bullets.append(bullet)

    def move_enemies(self):
        if not self.enemies:
            return
        for e in self.enemies:
            self.canvas.move(e, self.enemy_direction * self.enemy_speed, 0)
        left = self.canvas_width
        right = 0
        for e in self.enemies:
            x1, y1, x2, y2 = self.canvas.coords(e)
            if x1 < left:
                left = x1
            if x2 > right:
                right = x2
        if right >= self.canvas_width or left <= 0:
            self.enemy_direction = -self.enemy_direction
            for e in self.enemies:
                self.canvas.move(e, 0, self.enemy_drop)

    def check_collisions(self):
        for b in self.bullets[:]:
            bx1, by1, bx2, by2 = self.canvas.bbox(b.id)
            hit = False
            for enemy in self.enemies[:]:
                ex1, ey1, ex2, ey2 = self.canvas.bbox(enemy)
                if bx1 < ex2 and bx2 > ex1 and by1 < ey2 and by2 > ey1:
                    b.destroy()
                    self.canvas.delete(enemy)
                    self.bullets.remove(b)
                    self.enemies.remove(enemy)
                    self.score += 10
                    self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
                    if self.score and self.score % 50 == 0:
                        self.enemy_speed += 1
                    hit = True
                    break
            if hit:
                continue

    def check_win_lose(self):
        if not self.enemies:
            self.canvas.create_text(
                self.canvas_width / 2,
                self.canvas_height / 2,
                fill="white",
                font=("Arial", 32),
                text="YOU WIN!",
            )
            self.game_over = True
            return
        for e in self.enemies:
            x1, y1, x2, y2 = self.canvas.coords(e)
            if y2 >= self.canvas_height - 40:
                self.canvas.create_text(
                    self.canvas_width / 2,
                    self.canvas_height / 2,
                    fill="white",
                    font=("Arial", 32),
                    text="GAME OVER",
                )
                self.game_over = True
                return

    def game_loop(self):
        if self.game_over:
            return

        alive_bullets = []
        for b in self.bullets:
            if b.update():
                alive_bullets.append(b)
        self.bullets = alive_bullets

        self.move_enemies()
        self.check_collisions()
        self.check_win_lose()

        if not self.game_over:
            self.root.after(30, self.game_loop)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    GameApp().run()
