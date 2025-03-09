import json
from typing import Dict, List, Any, Optional


def transform_table_to_json(table: List[Dict[str, Any]], base_ws: Dict[str, Any],
                            key_mapping: Optional[Dict[str, str]] = None,
                            required_fields: List[str] = None) -> Dict[str, Any]:
    result = {}
    key_mapping = key_mapping or {}
    required_fields = required_fields or []
    ws_keys = {k.lower(): k for k in base_ws.keys()}
    try:
        for row in table:
            row_result = {}
            for table_key, table_value in row.items():
                target_key = (
                    key_mapping.get(table_key) or
                    next((ws_keys.get(k) for k in [table_key.lower(), table_key.replace(' ', '_').lower()]
                          if k in ws_keys), None))
                if not target_key:
                    continue
                expected_type = type(base_ws[target_key])
                try:
                    if expected_type == bool:
                        converted_value = str(table_value).lower() in ['true', '1', 'yes']
                    else:
                        converted_value = expected_type(table_value)
                except (ValueError, TypeError):
                    converted_value = table_value
                row_result[target_key] = converted_value
            missing_fields = [f for f in required_fields if f not in row_result]
            if missing_fields:
                raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")
            if row_result:
                result.setdefault('data', []).append(row_result)
        result['metadata'] = {k: v for k, v in base_ws.items() if k not in ws_keys.values()}
    except Exception as e:
        return {'error': str(e),'original_data': table,'partial_result': result}
    return result


