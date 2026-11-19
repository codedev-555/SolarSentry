import reflex as rx

class input1State(rx.State):
    address: str = "" 
    m_bill: str = ""
    util_rate: str = ""
    mbill_int: float = 0

    

    @rx.event
    def set_address(self, value: str):
        self.address = value
    @rx.event
    def set_m_bill(self, value: str):
        self.m_bill = value
    @rx.event
    def set_util_rate(self, value: str):
        self.util_rate = value




def input1() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("hello"),
            rx.input(
                placeholder="Enter your monthly electricity bill",
                on_change=input1State.set_m_bill,
                position="absolute",
                top="375px",
                left="980px",
                width="100%",
                max_width="270px",
            ),
            rx.input(
                placeholder="Enter your local utility rate (cents/kWh)",
                on_change=input1State.set_util_rate,
                position="absolute",
                top="470px",
                left="980px",
                width="100%",
                max_width="270px",
            ),
            rx.input(
                placeholder="Enter your address",
                on_change=input1State.set_address,
                position="absolute",
                top="560px",
                left="980px",
                width="100%",
                max_width="270px",
            ),
            rx.link(
                rx.button(
                    "",
                    size="4",
                    position="absolute",
                    top="630px",
                    left="895px",
                    width="370px",
                    height="60px",
                    variant="ghost",
                    background_color="black",
                    text_color="transparent",
                    cursor="pointer",
                    ),
            ),
            rx.link(
                rx.button(
                    "Continue ->",
                    size="4",
                    position="absolute",
                    top="670px",
                    left="895px",
                    width="370px",
                    height="35px",
                    background_image="linear-gradient(to left, #5A32FA 0%, #D800F0 100%)",
                    cursor="pointer",
                    ),
                href="/choice",
            ),
            rx.link(
                rx.button(
                    "",
                    size="4",
                    position="absolute",
                    top="100px",
                    left="890px",
                    width="30px",
                    height="40px",
                    radius="full",
                    background_color="transparent",
                    text_color="transparent",
                    variant="ghost",
                    cursor="pointer",
                    ),
                href="/",
            ),
            rx.link(
                rx.button(
                    "Dont know your utility rate! Click Here",
                    size="4",
                    position="absolute",
                    top="620px",
                    left="895px",
                    width="370px",
                    height="40px",
                    background_image="linear-gradient(to right, #5A32FA 0%, #D800F0 50%, #5A32FA 100%)",
                    cursor="pointer",
                    ),
                href="/input2",
            ),
        ),
        background="center/ 1440px url('/input1.png')",
        width="1440px",
        height="731px",
        max_width="1440px",
        max_height="731px",
    )

