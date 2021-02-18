def get_city_country_name(city, country, population=None):
    """Строит отформатированое город, страна."""
    if population:
        formatted_name = f"{city.title()}, {country.title()} - population {population}"
    else:
        formatted_name = f'{city.title()}, {country.title()}'
    return formatted_name
