import reflex as rx
from .choice import choiceState


class scamState(rx.State):
    quote: str = ""
    scam: str = ""
    size: str = ""

    @rx.event
    def set_quote(self, value: str):
        self.quote = value

    @rx.event
    async def get_var(self):
        choice = await self.get_state(choiceState)

        if self.quote and choice.total_cost:
            int_quote = int(self.quote)
            boundary = 5000
            max_value = choice.total_cost + boundary
            min_value = choice.total_cost - boundary

            if int_quote > max_value:
                self.scam = "QUOTE OVERPRICED"
                self.size = "85px"
            elif int_quote < min_value:
                self.scam = "EXCELLENT DEAL"
                self.size = "100px"
            else:
                self.scam = "REGULAR QUOTE"
                self.size = "100px"



def scam() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.input(
                placeholder="Input your quote",
                on_change=scamState.set_quote,
                on_blur=scamState.get_var,
                position="absolute",
                top="210px",
                left="1045px",
                width="250px",
            ),
            rx.text(
                scamState.scam,
                position="absolute",
                top="130px",
                left="90px",
                color="rgba(0, 255, 255, 1)",
                font_size=scamState.size,

            ),
            rx.link(
                rx.button(
                    "",
                    size="4",
                    position="absolute",
                    top="65px",
                    left="988px",
                    width="10px",
                    height="30px",
                    radius="full",
                    background_color="transparent",
                    text_color="transparent",
                    variant="ghost",
                    cursor="pointer",
                    ),
                href="/choice",
            ),
            rx.text(
                "Input your quote to see if its a scam!",
                font_weight="bold",
                color="white",
                position="absolute",
                top="130px",
                left="1010px",
            )

    ),

    background="center/ 1440px url('/buy.png')",
    width="1440px",
    height="731px",
    max_width="1440px",
    max_height="731px",
    )
