import pandas as pd
import datetime

class FleetCostAnalyzer:
    def __init__(self, data_source):
        # Load the data from your SSR Google Sheet or CSV
        self.df = pd.read_csv(data_source)
        self.utilization_goal = 0.93  # Your record-breaking 93%

    def calculate_burn_rate(self):
        # Logic to see where the money is going
        total_repair_cost = self.df['repair_cost'].sum()
        avg_cost_per_unit = self.df['repair_cost'].mean()
        return f"Total Maintenance Burn: ${total_repair_cost:,.2f}"

    def maintenance_forecast(self):
        # Flag trucks approaching the 'Danger Zone'
        upcoming_service = self.df[self.df['miles_to_service'] < 500]
        return upcoming_service[['unit_id', 'miles_to_service']]

    def generate_cfo_report(self):
        print(f"--- FLEET HEALTH REPORT: {datetime.date.today()} ---")
        print(self.calculate_burn_rate())
        print("\n--- CRITICAL SERVICE ALERTS ---")
        print(self.maintenance_forecast())

# Sandbox Test
# analyzer = FleetCostAnalyzer('ssr_data_export.csv')
# analyzer.generate_cfo_report()
