import reflex as rx
from .choice import choiceState
from .input1 import input1State
from .input2 import input2State
import plotly.express as px
import plotly.graph_objects as go


class buyState(rx.State):
    interest: str = ""
    m_bill: str = ""
    data: dict = {"year": [], "debt": []}
    fig: go.Figure = go.Figure()
    breakeven: str = ""
    data_str: dict = {"debt": []}
    year: str = ""
    m_o_a: str = ""
    num: str = ""
    m_bill: str = ""
    p_o_d: str = ""
    saving: str = ""
    msaving: str = ""
    annual: str = ""
    monthly: str = ""


    @rx.event
    def set_year(self, value = str):
        self.year = value
    @rx.event
    def reset_year(self):
        self.year = ""
    @rx.event
    def reset_num(self):
        self.num = ""

    @rx.event
    def set_pod(self, value = str):
        self.p_o_d = value

    @rx.event
    def set_moa(self, value = str):
        self.m_o_a = value

    @rx.event
    def reload(self, value = str):
        self.year = value
        if not self.year == "":
            num = self.data_str["debt"][(int(float(self.year)))]
            self.num = str(int(float(num)))
            num1 = self.data_str["debt"][1]
            num2 = self.data_str["debt"][2]
            annual = float(num1) - float(num2)
            self.annual = str(int(annual))
            self.monthly = str(int(annual/12))
    @rx.event
    def reload2(self, value = str):
        self.m_o_a = value
        if not self.m_o_a == "":
            if not self.year == "":
                num = self.data_str["debt"][(int(float(self.year)))]
                self.num = str(int(float(num)))
                num1 = self.data_str["debt"][1]
                num2 = self.data_str["debt"][2]
                annual = float(num1) - float(num2)
                self.annual = str(int(annual))
                self.monthly = str(int(annual/12))



    @rx.event
    def set_interest(self, value: str):
        self.interest = value

    @rx.event
    async def get_var(self):
        choice = await self.get_state(choiceState)
        input1 = await self.get_state(input1State)
        input2 = await self.get_state(input2State)

    

        if not input1.m_bill == "":
            self.m_bill = input1.m_bill
        else:
            self.m_bill = input2.m_bill

        if choice.total_cost and self.m_bill:
                if self.interest:
                    m_bill = float(self.m_bill)
                    monthly_payment = m_bill - (m_bill * 0.15)
                    years = (int(((choice.total_cost * ((int(self.interest) / 100) + 1)) / (monthly_payment * 12)))) + 1
                    remaining_payment = (choice.total_cost * ((int(self.interest) / 100) + 1))
                    self.data = {"year": [], "debt": []}
                    year = 0
                
                    while year <= years:
                        self.data["year"].append(year)
                        remaining_payment -= int((monthly_payment * 12))
                        self.data["debt"].append(remaining_payment)
                        self.data_str["debt"].append(str(remaining_payment))
                        if year == years:
                            self.breakeven = str(year)
                        year += 1
        if not self.m_o_a == "":
            if not self.year == "":
                num = self.data_str["debt"][(int(float(self.year)))]
                self.num = str(int(float(num)))
            num1 = self.data_str["debt"][1]
            num2 = self.data_str["debt"][2]
            annual = float(num1) - float(num2)
            self.annual = str(int(annual))
            self.monthly = str(int(annual/12))
        


        self.fig = px.line(self.data, markers=True)
        self.fig.update_layout(width=770, height=292, margin=dict(l=0, r=0, t=35, b=0), paper_bgcolor="rgba(0,0,0,1)", plot_bgcolor="rgba(0,0,0,1)", legend=dict(font=dict(size=12, color="#ffffff")), hoverlabel=dict(font=dict(size=12, color="#040000")))
        self.fig.update_traces(marker=dict(line=dict(width=0)), line=dict(width=3, color="#00c8ff"),hovertemplate="Year %{x}<br>$%{y:.0f}<extra></extra>", mode="lines+markers")
        self.fig.update_yaxes(tickfont=dict(size=12, color="#ffffff"),title_font=dict(size=14, color="#ffffff"), showline=True, zeroline=False)
        self.fig.update_xaxes(tickfont=dict(size=12, color="#ffffff"),title_font=dict(size=14, color="#ffffff"), dtick=1)


def overview():
    return rx.card(
        rx.vstack(
            rx.text(
                "What does this graph mean?",
                font_weight="bold",
                color="white",
                text_align="center"
            ),
            rx.text(
                "Total cost: " + choiceState.total_cost_str,
                color="white",
                text_align="center"
            ),
            align_items="center",
            spacing="0",
            margin="0px",
            gap="0px",
            margin_top="-8px"
        ),
        background="linear-gradient(to right, #5A32FA 0%, #D800F0 50%, #5A32FA 100%)",
        width="370px",
        height="55px",
        position="absolute",
        top="125px",
        left="980px",
        variant="ghost",
    )
def LoanTerm():
    return rx.card(
        rx.vstack(
            rx.text(
                "Loan Term(How long your paying for your solar panels): " + buyState.breakeven,
                color="white",
            ),
            spacing="0",
            margin="0px",
            gap="0px",
            margin_top="-8px"
        ),
        background="linear-gradient(to right, #5A32FA 0%, #D800F0 50%, #5A32FA 100%)",
        width="370px",
        height="55px",
        position="absolute",
        top="285px",
        left="980px",
        variant="ghost",
    )
def breakeven():
    return rx.card(
        rx.vstack(
            rx.text(
                "Break Even year(Starting this year, your electricity bill will be $0): " + buyState.breakeven,
                color="white",
                width="350px",
            ),
            spacing="0",
            margin="0px",
            gap="0px",
            margin_top="-8px"
        ),
        background="linear-gradient(to right, #5A32FA 0%, #D800F0 50%, #5A32FA 100%)",
        width="370px",
        height="55px",
        position="absolute",
        top="355px",
        left="980px",
        variant="ghost",
    )
def yearLookup():
    return rx.card(
        rx.vstack(
            rx.text(
                "See your remaining debt and payments for any year—just answer a few questions!",
                font_weight="bold",
                color="white",
                width="100%",
                max_width="330px"
            ),
            rx.box(
                rx.select(
                    items=["Choose...", "Payment", "Debt"],
                    value=buyState.p_o_d,
                    on_change=[buyState.set_pod, buyState.reset_year, buyState.reset_num],
                    placeholder="Select annually or monthly",
                    position="popper",
                    width="270px"
                    

            ),  
            
            ),
            rx.cond(
                buyState.p_o_d == "Debt",
                rx.vstack(
                    rx.text(
                        "Want to know your remaining debt at a specific year in your Loan! Input the year you would like to see.",
                        font_weight="bold",
                        color="white",
                        width="100%",
                        max_width="350px"
                    ),
                    rx.input(
                        placeholder="Enter the year you would like to check",
                        on_change=[buyState.set_year, buyState.reload],
                        width="100%",
                        max_width="270px",
                    ),
                ),
                None,
            ),
            rx.cond(
                buyState.year != "",
                rx.text(
                    "Year " + buyState.year + ": $" + buyState.num,
                    font_weight="bold",
                    color="white",
                ),
                None,
            ),
            rx.cond(
                buyState.p_o_d == "Payment",
                rx.vstack(
                    rx.text(
                        "Per year cost: " + buyState.annual,
                        color="white",
                        font_weight="bold"
                    ),
                    rx.text(
                        "Per month cost: " + buyState.monthly,
                        color="white",
                        font_weight="bold"
                    ),
                )
            ),
            
            spacing="2",
            margin="0px",
            gap="8px",
            margin_top="-8px"
        ),
        background="linear-gradient(to right, #5A32FA 0%, #D800F0 50%, #5A32FA 100%)",
        width="370px",
        height="280px",
        position="absolute",
        top="425px",
        left="980px",
        variant="ghost",
    )

def buy() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.box(
                rx.plotly(data=buyState.fig),
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
            rx.input(
                placeholder="Input your interest. Dont know put 7",
                on_change=buyState.set_interest,
                on_blur=buyState.get_var,
                position="absolute",
                top="210px",
                left="1045px",
                width="250px",
            ),
            overview(),
            LoanTerm(),
            breakeven(),
            yearLookup(),
    ),
    background="center/ 1440px url('/buy.png')",
    width="1440px",
    height="731px",
    max_width="1440px",
    max_height="731px",
    )

