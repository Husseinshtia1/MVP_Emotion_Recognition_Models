
import logging

def report_incident(incident_details):
    """Log and report incidents."""
    logging.basicConfig(filename='incidents.log', level=logging.INFO)
    logging.info(f"Incident reported: {incident_details}")

if __name__ == "__main__":
    report_incident("Test incident: Database connection failure.")
