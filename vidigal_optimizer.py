import pandas as pd
import numpy as np

class InformalEconomyOptimizer:
    def __init__(self, daily_capacity=15, base_price_brl=80):
        """
        Initializes the optimizer for a Vidigal Micro-Enterprise.
        :param daily_capacity: Total number of beds available.
        :param base_price_brl: Average price per bed in Brazilian Reais.
        """
        self.capacity = daily_capacity
        self.base_price = base_price_brl
        # Informal markets have high 'Trust Tax' (No-show rates)
        self.analog_no_show_rate = 0.30  
        self.digital_no_show_rate = 0.08 

    def load_data(self, filepath):
        """Loads transaction data from the digital twin excel sheet."""
        self.df = pd.read_csv(filepath)
        self.df['date'] = pd.to_datetime(self.df['date'])
        return self.df.head()

    def calculate_digital_exclusion_tax(self, days_active=30):
        """
        Quantifies the revenue lost due to lack of digital visibility.
        Compares 'Analog' (Walk-in only) vs 'Digital' (Platform integrated) scenarios.
        """
        # Scenario A: Analog (High friction, cash only, high no-shows)
        analog_occupancy = 0.41 # Based on field observation
        analog_revenue = (self.capacity * analog_occupancy * self.base_price * days_active) * (1 - self.analog_no_show_rate)

        # Scenario B: Digital Integration (Global visibility, lower friction)
        digital_occupancy = 0.60 # Post-intervention observation
        # Digital users pay a premium for security
        digital_price_premium = 1.15 
        digital_revenue = (self.capacity * digital_occupancy * (self.base_price * digital_price_premium) * days_active) * (1 - self.digital_no_show_rate)

        exclusion_tax = digital_revenue - analog_revenue

        print(f"--- VIDIGAL MICRO-ENTERPRISE ANALYSIS ---")
        print(f"Analog Monthly Revenue (Est): R$ {analog_revenue:,.2f}")
        print(f"Digital Integrated Revenue (Est): R$ {digital_revenue:,.2f}")
        print(f"THE DIGITAL EXCLUSION TAX (Loss): R$ {exclusion_tax:,.2f}")

        return exclusion_tax

    def suggest_dynamic_pricing(self, current_occupancy):
        """
        Simple rule-based algorithm to optimize pricing based on demand signals.
        Designed for low-bandwidth execution (WhatsApp deployment).
        """
        if current_occupancy < 0.30:
            return "ACTION: Activate 'Flash Sale' on WhatsApp Status. Discount 20%."
        elif current_occupancy > 0.80:
            return "ACTION: High Demand. Increase Walk-in Price by 15%."
        else:
            return "ACTION: Maintain Base Price. Focus on Reviews."

# Example Usage Simulation
if __name__ == "__main__":
    # Simulate a hostel in the 'Arvrão' sector of Vidigal
    optimizer = InformalEconomyOptimizer(daily_capacity=20, base_price_brl=90)

    # Calculate the cost of being offline
    lost_revenue = optimizer.calculate_digital_exclusion_tax(days_active=30)

    # Run pricing logic for a specific day
    todays_occupancy = 0.85
    recommendation = optimizer.suggest_dynamic_pricing(todays_occupancy)
    print(f"TODAY'S STRATEGY: {recommendation}")

