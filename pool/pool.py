#!/usr/bin/env python3


def volume(diameter, height, full=1.0):
    return (diameter / 2) * (diameter / 2) * 3.1415 * height * full


def gallons_from_volume(vol):
    return vol / 231.0
    

def how_much_pool_shock(gals):
    per_gallon = 453 / 12000.0
    return gals * per_gallon
        

if __name__ == "__main__":
    
    how_full = 0.8125
    vol = volume(144, 30, full=how_full)
    gal = gallons_from_volume(vol)
    shock = how_much_pool_shock(gal)
    
    print(f'{how_full * 100}% Pool Volume: {vol:,} cubic inches')
    print(f'We will have {gal:,.2f} gallons of water')
    print(f'We need {shock:.2f} grams of pool shock')
