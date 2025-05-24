"""Module defining Pet and Owner classes for managing pet ownership relationships."""

class Pet:
    """A class representing a pet with a type and an optional owner."""
    
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        """Initialize a Pet with a name, type, and optional owner.
        
        Args:
            name (str): The pet's name.
            pet_type (str): The type of pet (must be in PET_TYPES).
            owner (Owner, optional): The owner of the pet. Defaults to None.
        
        Raises:
            ValueError: If pet_type is not in PET_TYPES.
        """
        if pet_type not in Pet.PET_TYPES:
            raise ValueError(f"Invalid pet type: {pet_type}. Must be one of {Pet.PET_TYPES}")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)


class Owner:
    """A class representing an owner who can have multiple pets."""

    def __init__(self, name):
        """Initialize an Owner with a name."""
        self.name = name

    def pets(self):
        """Return a list of all pets owned by this owner.
        
        Returns:
            list[Pet]: A list of Pet instances.
        """
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Add a pet to this owner.
        
        Args:
            pet (Pet): The pet to be added.
            
        Raises:
            TypeError: If pet is not a Pet instance.
        """
        if not isinstance(pet, Pet):
            raise TypeError("Argument must be a Pet instance.")
        pet.owner = self

    def get_sorted_pets(self):
        """Return a list of pets owned by this owner, sorted by name.
        
        Returns:
            list[Pet]: A sorted list of Pet instances.
        """
        return sorted(self.pets(), key=lambda pet: pet.name)