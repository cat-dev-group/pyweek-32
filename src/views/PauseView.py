import arcade

import __main__


class PauseScreen(arcade.View):
    """
    Create pause menu screen, with options to resume or quit.

    Will accept a passed scheduled function to "pause" with `arcade.unschedule`.
    """

    def __init__(
        self,
        game_view,
        scheduled_function,
        score,
    ):
        super().__init__()
        self.game_view = game_view
        self.fill_color = arcade.make_transparent_color(
            arcade.color.WHITE, transparency=100
        )
        self.scheduled_function = scheduled_function
        arcade.unschedule(self.scheduled_function)
        self.score = score

    def on_draw(self):
        """Create a pause menu with options to quit or resume."""
        self.game_view.on_draw()
        arcade.draw_lrtb_rectangle_filled(
            left=0,
            right=__main__.SCREEN_WIDTH,
            top=__main__.SCREEN_HEIGHT,
            bottom=0,
            color=self.fill_color,
        )

        current_score = f"Current score: {self.score:9}"
        arcade.draw_text(
            current_score,
            __main__.SCREEN_WIDTH / 2,
            __main__.SCREEN_HEIGHT / 2 + 250,
            arcade.color.BLACK,
            font_size=20,
            anchor_x="center",
        )
        arcade.draw_text(
            "Press P to resume",
            __main__.SCREEN_WIDTH / 2,
            __main__.SCREEN_HEIGHT / 2 + 200,
            arcade.color.BLACK,
            font_size=20,
            anchor_x="center",
        )
        arcade.draw_text(
            "Press ESC to quit",
            __main__.SCREEN_WIDTH / 2,
            __main__.SCREEN_HEIGHT / 2 + 150,
            arcade.color.BLACK,
            font_size=20,
            anchor_x="center",
        )

    def on_key_press(self, symbol, modifiers):
        """Handle options to quit or resume."""
        if symbol == arcade.key.ESCAPE:
            # Quit immediately
            arcade.close_window()

        if symbol == arcade.key.P:
            self.window.show_view(self.game_view)
            arcade.schedule(self.scheduled_function, 0.5)
