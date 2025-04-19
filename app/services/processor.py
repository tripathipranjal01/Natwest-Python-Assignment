import pandas as pd
import yaml
import os
from app.utils.logger import logger

INPUT_CSV = "data/input.csv"
REFERENCE_CSV = "data/reference.csv"
RULES_YAML = "data/rules.yaml"
OUTPUT_CSV = "data/output.csv"
OUTPUT_XLSX = "data/output.xlsx"
OUTPUT_JSON = "data/output.json"

def generate_report():
    logger.info("Starting report generation process...")

    input_df = pd.read_csv(INPUT_CSV)
    reference_df = pd.read_csv(REFERENCE_CSV)
    logger.info(" Loaded input.csv and reference.csv")

    merged_df = pd.merge(
        input_df,
        reference_df,
        on=["refkey1", "refkey2"],
        how="left"
    )
    logger.info("Merged input and reference data on [refkey1, refkey2]")

    with open(RULES_YAML, 'r') as file:
        rules = yaml.safe_load(file)
    logger.info("Loaded transformation rules from rules.yaml")

    output_data = pd.DataFrame()

    for rule in rules.get("output_rules", []):
        outfield = rule["outfield"]
        operation = rule["operation"]
        fields = rule["fields"]

        logger.info(f"Applying rule: {operation} -> {outfield} from {fields}")

        if operation == "add":
            output_data[outfield] = merged_df[fields].apply(pd.to_numeric, errors="coerce").sum(axis=1)
        elif operation == "assign":
            output_data[outfield] = merged_df[fields[0]]
        elif operation == "max":
            output_data[outfield] = merged_df[fields].apply(pd.to_numeric, errors="coerce").max(axis=1)
        elif operation == "multiply_max":
            max_val = merged_df[[fields[1], fields[2]]].apply(pd.to_numeric, errors="coerce").max(axis=1)
            output_data[outfield] = pd.to_numeric(merged_df[fields[0]], errors="coerce") * max_val
        else:
            logger.warning(f" Unknown operation '{operation}' in rule: {rule}")
            output_data[outfield] = None

    logger.info("📤 Writing output files (CSV, Excel, JSON)...")
    output_data.to_csv(OUTPUT_CSV, index=False)
    output_data.to_excel(OUTPUT_XLSX, index=False)
    output_data.to_json(OUTPUT_JSON, orient="records", indent=2)

    logger.info(" Report generation complete.")
    return f" Report generated: {OUTPUT_CSV}, {OUTPUT_XLSX}, {OUTPUT_JSON}"

