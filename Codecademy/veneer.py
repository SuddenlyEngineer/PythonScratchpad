class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
    self.owner.name = owner.name
    self.owner.location = owner.location
  def __repr__(self):
    return f"{self.artist} {self.title} {self.year} {self.medium} {self.owner.name} {self.owner.location}"
  
class Marketplace:
  def __init__(self, listings):
    self.listings = listings
  def add_listing(self, new_listing):
    self.listings.append(new_listing)
  def remove_listing(self, old_listing):
    self.listings.remove(old_listing)
  def show_listings(self):
    for listing in self.listings:
        print(listing)
      
class Client:
  def __init__(self, name, location, is_museum):
    self.name = name
    self.location = location
    self.is_museum = is_museum
  def sell_artwork(self, artwork, price, market):
    if artwork.owner.name == self.name:
      temp = Listing(artwork, price, self.name)
      market.add_listing(temp)
  def buy_artwork(self, artwork, market):
      if artwork.owner.name != self.name:
          if artwork.title in market.listings:
              artwork.owner = self.name
              market.remove_listing(artwork)

class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller
  def __repr__(self):
    return f"{self.art.title}, {self.price}"
      
veneer = Marketplace([])

veneer.show_listings

edytta = Client("Edytta Halpirt", "Private Collector", False)

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", 1910, edytta)

moma = Client("The MOMA", "New York", True)

edytta.sell_artwork(girl_with_mandolin,6_000_000, veneer)

veneer.show_listings()