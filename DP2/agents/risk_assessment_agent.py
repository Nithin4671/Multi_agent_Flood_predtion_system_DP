class RiskAssessmentAgent:
    """
    Evaluates the overall risk of a flood based on prediction probability
    and the vulnerability of the affected area.
    """
    
    def __init__(self):
        # We can set thresholds for what counts as High or Severe risk
        self.severe_threshold = 75
        self.high_threshold = 50
        self.medium_threshold = 25

    def calculate_vulnerability_score(self, population_density, infrastructure_criticality):
        """
        Calculates how vulnerable an area is on a scale of 0 to 100.
        - population_density: Number of people (e.g., scale 0-100)
        - infrastructure_criticality: Importance of buildings/roads (e.g., scale 0-100)
        """
        # Weighting: Population matters slightly more than infrastructure
        score = (population_density * 0.6) + (infrastructure_criticality * 0.4)
        return score

    def assess_risk(self, location_id, flood_probability, population_density, infrastructure_criticality):
        """
        Combines flood probability and vulnerability to determine the final risk level.
        - flood_probability: Percentage (0 to 100) from the Flood Prediction Agent
        """
        # 1. Get the vulnerability score
        vulnerability = self.calculate_vulnerability_score(population_density, infrastructure_criticality)
        
        # 2. Calculate final risk (Probability x Vulnerability)
        # We divide by 100 to keep the final score on a 0-100 scale
        risk_score = (flood_probability * vulnerability) / 100
        
        # 3. Categorize the risk
        if risk_score >= self.severe_threshold:
            risk_level = "SEVERE"
        elif risk_score >= self.high_threshold:
            risk_level = "HIGH"
        elif risk_score >= self.medium_threshold:
            risk_level = "MEDIUM"
        else:
            risk_level = "LOW"
            
        # 4. Return a structured report for the next agent (Resource Allocation)
        return {
            "location_id": location_id,
            "flood_probability": flood_probability,
            "vulnerability_score": round(vulnerability, 2),
            "final_risk_score": round(risk_score, 2),
            "risk_level": risk_level
        }