class Game:
    Name = 'Minecraft'
    Published_Date = '1999/21/1'
    Mode = ['Survial', 'Creative', 'Adventure', 'Easy']
    
    
    
g = Game()

print("Name: ", g.Name)
del g
print(f"Published date: {g.Published_Date} {g.Mode}" )
print("Gaming mode:", g.Mode)
