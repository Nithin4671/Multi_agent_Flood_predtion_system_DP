from agents.risk_assessment_agent import RiskAssessmentAgent

# 1. Initialize the agent
risk_agent = RiskAssessmentAgent()

# 2. Simulate data coming from your other agents
# Let's pretend the Flood Agent says there is an 85% chance of a flood in Guwahati
simulated_data = {
    "location_id": "Guwahati_Sector_4",
    "flood_probability": 85.0,           
    "population_density": 90.0,          # Very crowded area
    "infrastructure_criticality": 80.0   # Contains a hospital
}

# 3. Run the assessment
report = risk_agent.assess_risk(
    location_id=simulated_data["location_id"],
    flood_probability=simulated_data["flood_probability"],
    population_density=simulated_data["population_density"],
    infrastructure_criticality=simulated_data["infrastructure_criticality"]
)

# 4. Print the result
print(f"Risk Level for {report['location_id']}: {report['risk_level']}")
print(f"Details: {report}")