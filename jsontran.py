def translate(translatable, language):
    if not translatable:
        return translatable

    if type(translatable) is dict:
        result = {}

        translations = translatable.get("i18n", {})
        for key, value in translatable.items():
            if key == "i18n":
                continue
            if type(value) in [dict, list]:
                result[key] = translate(value, language)
            elif f"{key}_{language}" in list(translations.keys()):
                result[key] = translations[f"{key}_{language}"]
            else:
                result[key] = value
        return result

    if type(translatable) is list:
        return [translate(item, language) for item in translatable]