#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automated SQL Schema Extractor & Data Dictionary Builder
Parses .sql dump files (CREATE TABLE statements) or database JSON schemas
and structures them into formal Thai Academic Data Dictionary tables.
"""

import re
import json
import os

def parse_sql_file(sql_path):
    """Parses a .sql file and extracts all table definitions."""
    with open(sql_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # Pattern for CREATE TABLE `table_name` (...)
    table_pattern = re.compile(r"CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?`?(\w+)`?\s*\((.*?)\)\s*ENGINE", re.DOTALL | re.IGNORECASE)
    matches = table_pattern.findall(content)

    schema = {}
    for table_name, body in matches:
        lines = [line.strip().rstrip(",") for line in body.split("\n") if line.strip()]
        columns = []
        for line in lines:
            # Skip keys/indexes definitions
            if re.match(r"^(PRIMARY\s+KEY|KEY|UNIQUE\s+KEY|CONSTRAINT|INDEX)", line, re.IGNORECASE):
                continue
            
            # Match column definition: `col_name` type ...
            col_match = re.match(r"^`?(\w+)`?\s+([\w\(\)]+(?:\s+unsigned)?)\s*(.*)$", line, re.IGNORECASE)
            if col_match:
                col_name = col_match.group(1)
                col_type = col_match.group(2)
                col_rest = col_match.group(3)
                
                is_not_null = "NOT NULL" in col_rest.upper()
                is_pk = "PRIMARY KEY" in col_rest.upper()
                
                columns.append({
                    "field": col_name,
                    "type": col_type,
                    "null": "NOT NULL" if is_not_null else "NULL",
                    "definition": f"{col_type} {col_rest}".strip()
                })
        if columns:
            schema[table_name] = columns

    return schema

def build_data_dictionary_sections(schema, descriptions_map=None, table_titles_map=None):
    """
    Constructs ready-to-render formal Thai Data Dictionary table entries for generate_academic_thesis.py.
    """
    if descriptions_map is None:
        descriptions_map = {}
    if table_titles_map is None:
        table_titles_map = {}

    items = []
    for idx, (t_name, cols) in enumerate(schema.items(), start=2):
        t_title = table_titles_map.get(t_name, f"ตารางข้อมูล {t_name}")
        items.append(f"{idx-1}) {t_title} รายละเอียดดังตารางที่ 3.{idx}")
        items.append({"type": "table_caption", "text": f"ตารางที่ 3.{idx} {t_title}"})

        headers = ["ลำดับ", "ชื่อฟิลด์ (Field Name)", "ประเภทข้อมูล (Data Type)", "ข้อจำกัด / คีย์", "คำอธิบาย"]
        rows = []
        for c_idx, c in enumerate(cols, start=1):
            fld = c["field"]
            dtype = c["type"]
            null_info = c["null"]
            desc_tuple = descriptions_map.get(t_name, {}).get(fld, (fld, ""))
            desc = desc_tuple[0] if isinstance(desc_tuple, tuple) else desc_tuple
            key_info = desc_tuple[1] if isinstance(desc_tuple, tuple) and desc_tuple[1] else null_info
            rows.append([str(c_idx), fld, dtype, key_info, desc])

        items.append({"type": "table", "headers": headers, "rows": rows})

    return items

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        sql_file = sys.argv[1]
        schema = parse_sql_file(sql_file)
        print(f"Extracted {len(schema)} tables from {sql_file}")
        out_json = sys.argv[2] if len(sys.argv) > 2 else "schema_extracted.json"
        with open(out_json, "w", encoding="utf-8") as f:
            json.dump(schema, f, ensure_ascii=False, indent=2)
        print(f"Saved extracted schema to {out_json}")
