import reflex as rx

def home() -> rx.Component:
    return rx.container(
      rx.vstack(
      rx.color_mode.button(
          position="top-right", 
          color="white"
          ),
      rx.heading("$olar$entry", 
                 font_size="100px", 
                 position="absolute", 
                 top="200px", left="70px", 
                 color="white"
                 ),
      rx.text("\"Find Your Real Solar Costs. Expose the Scams\"", 
              size="7", 
              position="absolute", 
              top="290px", 
              left="80px", 
              color="white"
              ),
      rx.text("📊 Smart Cost Estimator", 
              size="6", 
              position="absolute", 
              top="360px", 
              left="80px", 
              color="white"
              ),
      rx.text("🛡️ Scam Detection Engine", 
              size="6", 
              position="absolute", 
              top="410px", 
              left="80px", 
              color="white"
              ),
      rx.text(
              "💰 Compare Buy vs. Lease cost", 
              size="6", 
              position="absolute", 
              top="460px", 
              left="80px", 
              color="white"
              ),
      rx.link(
          rx.button(
            "Get Started", 
            size="4", 
            position="absolute", 
            top="530px", 
            left="80px", 
            radius="medium", 
            background_image="linear-gradient(to right, #5A32FA 0%, #D800F0 100%)",
            cursor="pointer",
            ),
            href="/input1",
        ),
        
        
      ),
      background="center/ 1440px url('/home_background.png')",
      width="1440px",
      height="731px",
      max_width="1440px",
      max_height="731px",
      )
