output = []
for guest in guests:
    guest_data = {}
    guest_data['id'] = guest.id
    guest_data['name'] = guest.name
    guest_data['occupation'] = guest.occupation
    output.append(guest_data)

