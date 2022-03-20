from mediator import logic, components, handlers

# Mediator class
mediator = logic.Mediator()

# Mediator object model
pokemon = components.PokemonComponent()
# Mediator object handler
pokemon_handler = handlers.PokemonComponentHandler()
# Mediator object model
university = components.UComponent()
# Mediator object handler
u_handler = handlers.UComponentHandler()

# Object model & handler register in the mediator
mediator.add(pokemon, pokemon_handler)
mediator.add(university, u_handler)

# sending objects to test
mediator.send(components.PokemonComponent("ditto"))
# mediator.send(components.UComponent('United+States'))

print(mediator.response)
print(mediator.response.json())

