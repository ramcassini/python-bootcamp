status = 404

match status:
    case 404:
        print('page not found')
    case 400:
        print('bad request')
    case _:
        print('invalid code')