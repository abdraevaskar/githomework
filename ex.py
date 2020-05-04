a = """
        Sed ut perspiciatis unde omnis iste natus error sit 
        voluptatem accusantium doloremque laudantium, totam rem aperiam, 
        eaque ipsa quae ab illo inventore veritatis et quasi architecto 
        beatae vitae dicta sunt explicabo. Nemo enim 
        ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, 
        sed quia consequuntur magni dolores eos qui
    """
for item in a:
    if item in [' ', ',', '.']:
        continue
    counter += 1

print(counter)
print(len(a))
