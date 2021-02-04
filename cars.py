def dictCars(manufacturer, model, **kwargs):
    kwargs['manufacturer'] = manufacturer
    kwargs['model'] = model
    return kwargs

car = dictCars('subaru', 'outback', color='blue', tow_package=True)
print(car)
