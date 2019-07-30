# jsontran

####Applies i18n translations to json. Should support any valid json 

example:

`json_dict = {"title": "Hello", "i18n": {"title_pt": "Olá}}` 

`translate(json_dict, "pt")` results in:

`{"title": "Olá"}`


more examples: see tests

####To run tests:

`$ pytest`