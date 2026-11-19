import reflex as rx
from .choice import choiceState
from .input1 import input1State
from .input2 import input2State
import plotly.express as px
import plotly.graph_objects as go
import math


class leaseState(rx.State):
    data: dict = {"year": [], "payment": []}
    fig: go.Figure = go.Figure()
    year: str = ""
    m_o_a: str = ""
    data_str: dict = {"payment": []}
    num: str = ""
    m_bill: str = ""
    saving: str = ""
    start_year_lease: str = ""



    @rx.event
    def set_year(self, value = str):
        self.year = value

    @rx.event
    def set_moa(self, value = str):
        self.m_o_a = value

    @rx.event
    def reload(self, value = str):
        self.year = value
        if not self.m_o_a == "":
            if not self.year == "":
                num = self.data_str["payment"][(int(float(self.year)) - 1)]
                if self.m_o_a == "Monthly":
                    self.num = str(int(float(num) / 12))

                else:
                    self.num = str(int(float(num)))
        
    @rx.event
    def reload2(self, value = str):
        self.m_o_a = value
        if not self.m_o_a == "":
            if not self.year == "":
                num = self.data_str["payment"][(int(float(self.year)) - 1)]
                if self.m_o_a == "Monthly":
                    self.num = str(int(float(num) / 12))

                else:
                    self.num = str(int(float(num)))



    @rx.event
    async def get_var(self):
        choice = await self.get_state(choiceState)
        input1 = await self.get_state(input1State)
        input2 = await self.get_state(input2State)
        

        if not input1.m_bill == "":
            self.m_bill = input1.m_bill
        else:
            self.m_bill = input2.m_bill


        if choice.start_m_lease and choice.grid_connection:
            m_lease = float(choice.start_m_lease)
            years_payment = (float(choice.start_m_lease) + choice.grid_connection) * 12
            self.data = {"year" : [], "payment": []}
            year = 1
                
            for i in range(100):
                if year <= 10:
                    self.data["year"].append(year)
                    self.data["payment"].append(years_payment)
                self.data_str["payment"].append(str(years_payment))
                m_lease *= 1.025
                choice.grid_connection *= 1.035
                years_payment = (m_lease + choice.grid_connection) * 12
                year += 1
                print(years_payment)
                print(year)

        if not self.m_o_a == "":
            if not self.year == "":
                num = self.data_str["payment"][(int(float(self.year)) - 1)]
                if self.m_o_a == " Monthly":
                    self.num = str(int(float(num) / 12))

                else:
                    self.num = str(int(float(num)))

        self.start_year_lease = self.data_str["payment"][0]






        self.fig = px.line(self.data)
        self.fig.update_layout(width=770, height=292, margin=dict(l=0, r=0, t=35, b=0), paper_bgcolor="rgba(0,0,0,1)", plot_bgcolor="rgba(0,0,0,1)", legend=dict(font=dict(size=12, color="#ffffff")), hoverlabel=dict(font=dict(size=12, color="#040000")), xaxis_title="Lease Year", yaxis_title="Lease payment($)")
        self.fig.update_traces(marker=dict(line=dict(width=0)), line=dict(width=3, color="#00c8ff"),hovertemplate="Year %{x}<br>$%{y:.0f}<extra></extra>")
        self.fig.update_yaxes(tickfont=dict(size=12, color="#ffffff"),title_font=dict(size=14, color="#ffffff"), showline=True, zeroline=False)
        self.fig.update_xaxes(tickfont=dict(size=12, color="#ffffff"),title_font=dict(size=14, color="#ffffff"), dtick=1)


def overview():
    return rx.card(
        rx.vstack(
            rx.text(
                "What does this graph mean?",
                font_weight="bold",
                color="white",
            ),
            rx.hstack(
                rx.text(
                    "Upfront cost: 0",
                    color="white",
                ),
    
                rx.text(
                    "First year cost: " + leaseState.start_year_lease,
                    color="white",
                ),
            ),
            spacing="2",
            margin="0px",
            gap="15px",
            margin_top="-8px"
        ),
        background="linear-gradient(to right, #5A32FA 0%, #D800F0 50%, #5A32FA 100%)",
        width="370px",
        height="90px",
        position="absolute",
        top="140px",
        left="980px",
        variant="ghost",
    )

def search():
    return rx.card(
        rx.vstack(
            rx.text(
                "Want to know the monthly or annual cost for a specific year? input it here to get the price!",
                font_weight="bold",
                color="white",
                width="100%",
                max_width="310px"
            ),
            rx.input(
                placeholder="Enter the year you would like to check",
                on_change=[leaseState.set_year, leaseState.reload],
                width="100%",
                max_width="270px",

            ),
            rx.box(
                rx.select(
                    items=["Monthly", "Annually"],
                    value=leaseState.m_o_a,
                    on_change=[leaseState.set_moa, leaseState.reload2],
                    placeholder="Select annually or monthly",
                    position="popper",
                    width="270px"

                ),
            ),
            rx.text(
                "Year " + leaseState.year + ": $" + leaseState.num,
                font_weight="bold",
                color="white",
            ),
            spacing="2",
            margin="0px",
            gap="20px",
            margin_top="-8px",
            justify="between"
        ),
        background="linear-gradient(to right, #5A32FA 0%, #D800F0 50%, #5A32FA 100%)",
        width="370px",
        height="300px",
        position="absolute",
        top="300px",
        left="980px",
        variant="ghost",
    )


def lease() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.button(
                "",
                background_color="#031124",
                text_color="transparent",
                position="absolute",
                top="160px",
                left="965px",
                width="380px",
                height="100px",
            ),
            rx.box(
                rx.plotly(data=leaseState.fig),
                position="absolute",
                top="63px",
                left="100px",
                max_width="770px",
                radius="large",
                overflow="hidden",

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
            overview(),
            search()
        ),


    background="center/ 1440px url('/buy.png')",
    width="1440px",
    height="731px",
    max_width="1440px",
    max_height="731px",

)