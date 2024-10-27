import turtle

# класс для визначення кольору пера


class Color:
    def __init__(self):
        self.dir = "next"
        self.colors = ["#292f56", "#1e4572", "#005c8b", "#007498", "#008ba0",
                       "#00a3a4", "#00bca1", "#00d493", "#69e882", "#acfa70"]
        self.i = 0

    def get(self):
        if self.dir == "next":
            self.i += 1
            if self.i >= len(self.colors):
                self.dir = "prev"
                self.i = len(self.colors) - 1
                return self.get()
            else:
                return self.colors[self.i]
        else:
            self.i -= 1
            if self.i < 0:
                self.dir = "next"
                self.i = -1
                return self.get()
            else:
                return self.colors[self.i]


colors = Color()

# Дерево Піфагора


def tree(t: turtle.Turtle, size, angle, deep_lvl, step):
    color = colors.get()

    t.forward(size)
    if deep_lvl != 0:
        size = size - step
        # зберигаемо позицію та напрям
        temp_pos = t.pos()
        temp_heading = t.heading()

        # повертаемо праворуч
        t.left(angle)
        t.pencolor(color)
        tree(t, size, angle, deep_lvl - 1, step)

        # відновлюємо напрямок та позицію
        t.penup()
        t.goto(temp_pos)
        t.setheading(temp_heading)
        t.pendown()

        # повертаемо ліворуч
        t.right(angle)
        t.pencolor(color)
        tree(t, size, angle, deep_lvl - 1, step)


def draw_tree(size=100, deep_lvl=3, angle=45):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, -size)
    t.setheading(90)
    t.pendown()

    step = size / deep_lvl

    tree(t, size, angle,  deep_lvl, step)

    window.mainloop()


if __name__ == "__main__":
    # Виклик функції
    draw_tree(size=100, deep_lvl=10, angle=45)
