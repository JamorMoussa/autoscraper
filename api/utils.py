from autoscraper import (
    SelectorField, ParseType
)

def convert_selector_field(
    fields: dict[str, dict]
) -> dict:

    out_fields = {}

    for field_name in fields:
        out_fields[field_name] = (
            SelectorField, SelectorField(
                selector= fields[field_name].selector,
                data_from= ParseType.CONTENT if fields[field_name].data_from == "content" else ParseType.ATTRIBUTE,
                attribute= fields[field_name].attribute,
                processor= eval(fields[field_name].processor)
            )
        )

    return out_fields