import reflex as rx
import requests
import json
from .input1 import input1State
from .input2 import input2State


class choiceState(rx.State):
    total_cost: float = 0
    start_m_lease: str = ""
    grid_connection: float = 0
    extra_usage: float = 0
    extra_cost: float = 0
    start_year_lease: str = ""
    total_cost_str: str = ""



    @rx.event
    async def get_vars(self):
        input1 = await self.get_state(input1State)
        input2 = await self.get_state(input2State)


        
        if input2.ev_charger == True:
            self.extra_usage += 4500
        if input2.people == "1-2":
            self.extra_usage -= 100
        elif input2.people == "3-4":
            self.extra_usage += 1500
        else:
            self.extra_usage += 3000
        if input2.pool == True:
            self.extra_usage += 2500
        if input2.hotTub == True:
            self.extra_usage += 1500
        #input1
            #Buy
                #APIs

        if input1.address and input1.m_bill and input1.util_rate:



            #Nomatim openstreet/Geocoding API Result: State + lon/lat
            url = "https://nominatim.openstreetmap.org/search"

            response = requests.get(
                url,
                params={
                "q": input1.address,
                "format": "jsonv2",
                "addressdetails" : 1,
                "limit": 1,
            },
                headers={
                "User-Agent": "my-geocoder/1.0"
            },
                timeout=10,
            )


            data = response.json()
            print(response.json())

            latitude = float(data[0]["lat"])
            longitude = float(data[0]["lon"])

            #NRL solar resource API Result: GHI
            api_key = "YdbhU0IrDq3Kyh5Dbr9rIr2KQnh7rC73OBVd4od0"


            url = "https://developer.nlr.gov/api/solar/solar_resource/v1.json"


            params={
                "api_key": api_key,
                "lat": latitude,
                "lon": longitude,
            }


            response = requests.get(url, params=params)
            data = response.json()
            ghi = data["outputs"]["avg_ghi"]["annual"]
            print(ghi)

            #Calculations for cost

            annual_kwh = (int(input1.m_bill) / float(input1.util_rate)) * 12
            sunshine_production = ghi * 0.285
            s_size = (annual_kwh / sunshine_production) / 1000
            self.total_cost = s_size * 3000
            self.total_cost_str = str(int(s_size * 3000))


            #Lease
            sun_production = (ghi * 365) * 0.8
            discount_energy_rate = float(input1.util_rate) * 0.8
            self.grid_connection = 15
            self.start_m_lease = str(int(((sun_production * discount_energy_rate) / 12)))
            self.start_year_lease = str(int((((sun_production * discount_energy_rate) / 12)*12)))


        #input2

            #APIs


        if input2.address and input2.sqft and input2.people:


            #Nomatim openstreet/Geocoding API Result: State + lon/lat
            url = "https://nominatim.openstreetmap.org/search"

            response = requests.get(
                url,
                params={
                "q": input2.address,
                "format": "jsonv2",
                "addressdetails" : 1,
                "limit": 1,
            },
                headers={
                "User-Agent": "my-geocoder/1.0"
            },
                timeout=10,
            )


            data = response.json()
            print(response.json())

            latitude = float(data[0]["lat"])
            longitude = float(data[0]["lon"])
            address_state = data[0]["address"]["state"]
            us_states = [
            ["Alabama", "AL"],
            ["Alaska", "AK"],
            ["Arizona", "AZ"],
            ["Arkansas", "AR"],
            ["California", "CA"],
            ["Colorado", "CO"],
            ["Connecticut", "CT"],
            ["Delaware", "DE"],
            ["Florida", "FL"],
            ["Georgia", "GA"],
            ["Hawaii", "HI"],
            ["Idaho", "ID"],
            ["Illinois", "IL"],
            ["Indiana", "IN"],
            ["Iowa", "IA"],
            ["Kansas", "KS"],
            ["Kentucky", "KY"],
            ["Louisiana", "LA"],
            ["Maine", "ME"],
            ["Maryland", "MD"],
            ["Massachusetts", "MA"],
            ["Michigan", "MI"],
            ["Minnesota", "MN"],
            ["Mississippi", "MS"],
            ["Missouri", "MO"],
            ["Montana", "MT"],
            ["Nebraska", "NE"],
            ["Nevada", "NV"],
            ["New Hampshire", "NH"],
            ["New Jersey", "NJ"],
            ["New Mexico", "NM"],
            ["New York", "NY"],
            ["North Carolina", "NC"],
            ["North Dakota", "ND"],
            ["Ohio", "OH"],
            ["Oklahoma", "OK"],
            ["Oregon", "OR"],
            ["Pennsylvania", "PA"],
            ["Rhode Island", "RI"],
            ["South Carolina", "SC"],
            ["South Dakota", "SD"],
            ["Tennessee", "TN"],
            ["Texas", "TX"],
            ["Utah", "UT"],
            ["Vermont", "VT"],
            ["Virginia", "VA"],
            ["Washington", "WA"],
            ["West Virginia", "WV"],
            ["Wisconsin", "WI"],
            ["Wyoming", "WY"]
            ]
            for i in us_states:
                if i[0] == address_state:
                    state_abb = i[1]

            #NRL solar resource API Result: GHI
            api_key = "YdbhU0IrDq3Kyh5Dbr9rIr2KQnh7rC73OBVd4od0"


            url = "https://developer.nlr.gov/api/solar/solar_resource/v1.json"


            params={
                "api_key": api_key,
                "lat": latitude,
            "lon": longitude,
            }


            response = requests.get(url, params=params)
            data = response.json()
            ghi = data["outputs"]["avg_ghi"]["annual"]
            print(ghi)

            #EIA API Result: Sales + Customers

            api_key = "m1fgcmUCQbrbGxLt5eX1nqsIrh6Jz3JpIcwd9Fkb"


            url = "https://api.eia.gov/v2/electricity/retail-sales/data"


            params = {
            "api_key": api_key,
            "frequency": "annual",
            "data[]": ["sales", "customers"],
            "facets[stateid][]": "NC",
            "facets[sectorid][]": "RES",
            "sort[0][column]": "period",
            "sort[0][direction]": "desc",
            "length": 1
        }


            response = requests.get(url, params=params)
            print(response.status_code)
            data = response.json()
            sales = float(data["response"]["data"][0]["sales"])
            customers = int(data["response"]["data"][0]["customers"])
            sales *= 1000000
            print(sales)
            print(customers)
            avg_kwh = sales/customers
            print(sales/customers)

            #List of average house sqft per state

            state_home_sizes = [
            ["UT", 2800],
            ["CO", 2464],
            ["ID", 2311],
            ["WY", 2285],
            ["DE", 2277],
            ["GA", 2262],
            ["MD", 2207],
            ["MT", 2200],
            ["ND", 2190],
            ["WA", 2185],
            ["TX", 2170],
            ["CT", 2158],
            ["TN", 2157],
            ["NC", 2152],
            ["AL", 2146],
            ["SC", 2123],
            ["VA", 2105],
            ["NM", 2087],
            ["MS", 2065],
            ["NV", 2060],
            ["AZ", 2049],
            ["PA", 2045],
            ["MN", 2026],
            ["KS", 2020],
            ["NE", 2016],
            ["IN", 2011],
            ["VT", 2000],
            ["FL", 1960],
            ["LA", 1955],
            ["KY", 1953],
            ["OR", 1946],
            ["OK", 1941],
            ["NH", 1934],
            ["SD", 1915],
            ["RI", 1913],
            ["AK", 1910],
            ["AR", 1860],
            ["CA", 1860],
            ["MO", 1848],
            ["WI", 1822],
            ["OH", 1803],
            ["MA", 1800],
            ["NJ", 1753],
            ["WV", 1752],
            ["MI", 1726],
            ["IL", 1700],
            ["ME", 1680],
            ["IA", 1623],
            ["NY", 1490],
            ["HI", 1164]
        ]

            #Calulations for cost
            avg_sqft = 0
            for state in state_home_sizes:
                if state_abb in state:
                    avg_sqft = state[1]
                    print(state[1])
            sqft_kwh = avg_kwh/avg_sqft
            print(avg_kwh/avg_sqft)
            annual_sun_hrs = ghi * 365
            input2.sqft = float(input2.sqft)
            s_size = ((input2.sqft * sqft_kwh) + self.extra_usage)/(annual_sun_hrs)
            if s_size > 15:
                self.extra_cost += 3500
            elif s_size >= 7.6:
                self.extra_cost += 1500
            self.total_cost = ((s_size * 3000) + self.extra_cost)
            self.total_cost_str = str(((s_size * 3000) + self.extra_cost))
            #lease
            start_m_lease = ((input2.m_bill - 15) * 0.8)
            grid_connection = 15
            self.start_m_lease = start_m_lease
            self.grid_connection = grid_connection

        



def choice() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.link(
                rx.button(
                    "",
                    size="4",
                    position="absolute",
                    top="560px",
                    left="885px",
                    width="400px",
                    height="105px",
                    cursor="pointer",
                    background_color="transparent",
                    text_color="transparent",
                    variant="ghost",
                                ),
                href="/buy",
            ),
            rx.link(
                rx.button(
                    "",
                    size="4",
                    position="absolute",
                    top="315px",
                    left="885px",
                    width="400px",
                    height="105px",
                    background_color="transparent",
                    cursor="pointer",
                    text_color="transparent",
                    variant="ghost",
                                            ),
                href="/scam",
            ),
            rx.link(
                rx.button(
                    "",
                    size="4",
                    position="absolute",
                    top="440px",
                    left="885px",
                    width="400px",
                    height="105px",
                    background_color="transparent",
                    cursor="pointer",
                    text_color="transparent",
                    variant="ghost",
            ),
            href="/lease",
            ),
            rx.link(
                rx.button(
                    "",
                    size="4",
                    position="absolute",
                    top="95px",
                    left="898px",
                    width="10px",
                    height="30px",
                    radius="full",
                    background_color="transparent",
                    text_color="transparent",
                    variant="ghost",
                    cursor="pointer",
                    ),
                href="/input1",
            ),
            rx.text(
                choiceState.total_cost_str,
                color="white"
                )

        ),
        background="center/ 1440px url('/choice.png')",
        width="1440px",
        height="731px",
        max_width="1440px",
        max_height="731px",
    )
    
