##Args and Kwargs

def my_sum(my_integers):
    result = 0
    for x in my_integers:
        result += x
    return result


list_of_integers = [1, 2, 3]
print( my_sum( list_of_integers ) )


def my_sum(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result


print( my_sum( 1, 2, 3 ) )


def concatenate(**kwargs):
    result = ""
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
        result += arg
    return result


print( concatenate( a="Real", b="Python", c="Is", d="Great", e="!" ) )

my_list = [1, 2, 3, 4, 5, 6]

a, *b, c = my_list

print( a )
print( b )
print( c )

my_first_list = [1, 2, 3]
my_second_list = [4, 5, 6]
my_merged_list = [*my_first_list, *my_second_list]

print( my_merged_list )

#### recursion

houses = ["Misha's house", "Darya's house", "Olena's house", "Max's house"]


# Each function call represents an elf doing his work
def deliver_presents_recursively(houses):
    # Worker elf doing his work
    if len( houses ) == 1:
        house = houses[0]
        print( "Delivering presents to", house )

    # Manager elf doing his work
    else:
        mid = len( houses ) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]

        # Divides his work among two elves
        deliver_presents_recursively( first_half )
        deliver_presents_recursively( second_half )


full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
print( full_name( 'guido', "van rossum" ) )
