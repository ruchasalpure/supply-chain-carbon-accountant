from crewai import Agent

supply_chain_carbon_accountant = Agent(
    role="Supply Chain Carbon Accountant",
    goal="Deliver high-precision autonomous Supply Chain Carbon Accountant operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
