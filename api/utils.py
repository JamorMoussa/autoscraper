from bs4scraper import (
    SelectorField, ParseType
)

def convert_selector_field(
    fields: dict[str, dict]
) -> dict:

    out_fields = {}

    for field_name in fields:
        out_fields[field_name] = (
            SelectorField, SelectorField(
                css_class= fields[field_name].css_class,
                parse_type= ParseType.CONTENT if fields[field_name].parse_type == "content" else ParseType.ATTRIBUTE,
                attr_name= fields[field_name].attr_name,
                processor= eval(fields[field_name].processor)
            )
        )

    return out_fields