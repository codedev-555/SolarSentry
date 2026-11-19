import reflex as rx

class input2State(rx.State):
    address: str = "" 
    m_bill: str = ""
    sqft: str = ""
    people: str = ""
    ev_charger: bool = False
    pool: bool = False
    hotTub: bool = False
    


    @rx.event
    def update_address(self, value: str):
        self.address = value
    @rx.event
    def update_m_bill(self, value: str):
        self.m_bill = value
    @rx.event
    def update_ppl(self, value: str):
        self.people = value
    @rx.event
    def update_ev_charger(self, value: bool):
        self.ev_charger = value
    @rx.event
    def update_hotTub(self, value: bool):
        self.hotTub = value
    @rx.event
    def update_pool(self, value: bool):
        self.pool = value
    @rx.event
    def update_sqft(self, value: str):
        self.sqft = value

def input2() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.input(
                placeholder="Enter your monthly electricity bill",
                on_change=input2State.update_m_bill,
                position="absolute",
                top="327px",
                left="1048px",
                width="100%",
                height="100%",
                max_height="25px",
                max_width="270px",
                ),
                rx.input(
                    placeholder="Enter your address",
                    on_change=input2State.update_address,
                    position="absolute",
                    top="260px",
                    left="1048px",
                    width="100%",
                    height="100%",
                    max_height="25px",
                    max_width="270px",
                    ),
                rx.input(
                    placeholder="Enter your house square footage",
                    on_change=input2State.update_m_bill,
                    position="absolute",
                    top="392px",
                    left="1048px",
                    width="100%",
                    height="100%",
                    max_height="25px",
                    max_width="270px",
                    ),
                rx.switch(
                    checked=input2State.ev_charger,
                    on_change=input2State.update_ev_charger,
                    position="absolute",
                    top="513px",
                    left="1276px",
                    transform="scale(1.2, 1.1)",
                ),
                rx.switch(
                    checked=input2State.pool,
                    on_change=input2State.update_pool,
                    position="absolute",
                    top="567px",
                    left="1276px",
                    transform="scale(1.2, 1.1)",
                ),
                rx.switch(
                    checked=input2State.hotTub,
                    on_change=input2State.update_hotTub,
                    position="absolute",
                    top="620.5px",
                    left="1276px",
                    transform="scale(1.2, 1.1)",
                ),
                rx.box(
                    rx.select(
                        items=["1-2", "3-4", "5+"],
                        value=input2State.people,
                        on_change=input2State.update_ppl,
                        placeholder="Select number of people in your household",
                        position="popper",
                        width="278px",
                        size="1"

                ),
                    position="absolute",
                    top="458px",
                    left="1049px",
                    
                ),
                rx.link(
                    rx.button(
                        "",
                        size="4",
                        position="absolute",
                        top="675px",
                        left="999px",
                        width="310px",
                        height="40px",
                        variant="ghost",
                        background_color="black",
                        text_color="transparent",
                        cursor="pointer",
                        ),
                    href="/input2",
                ),
                rx.link(
                    rx.button(
                        "Back <-",
                        size="4",
                        position="absolute",
                        top="675px",
                        left="1160px",
                        width="185px",
                        height="40px",
                        background_image="linear-gradient(to right, #5A32FA 0%, #D800F0 100%)",
                        cursor="pointer",
                                    ),
                    href="/input1",
            
                
                    ),
                    rx.link(
                        rx.button(
                            "Continue ->",
                            size="4",
                            position="absolute",
                            top="675px",
                            left="970px",
                            width="185px",
                            height="40px",
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
                            top="60px",
                            left="990px",
                            width="40px",
                            height="40px",
                            radius="full",
                            background_color="transparent",
                            padding="0px",
                            text_color="transparent",
                            variant="ghost",
                            cursor="pointer",
                            ),
                        href="/input1",
                    ),

        

        ),
        position="relative",
        background="center/ 1440px url('/input2new.png')",
        width="1440px",
        height="731px",
        max_width="1440px",
        max_height="731px",
    )