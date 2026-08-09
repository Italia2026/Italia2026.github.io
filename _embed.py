PLACEHOLDER = '''    <div class="block">
      <h3>Where we're staying</h3>
      <p>Address, check-in details, and the door code once we have them.</p>
    </div>'''

STYLE = 'width:100%;max-width:450px;height:300px;margin:12px auto 6px;'

def embed(data_id, label):
    room = f"https://www.airbnb.com/rooms/{data_id}?guests=1&amp;adults=1&amp;s=66&amp;source=embed_widget"
    return (f'<div class="airbnb-embed-frame" data-id="{data_id}" data-view="home" '
            f'data-hide-price="true" style="{STYLE}">'
            f'<a href="{room}">View On Airbnb</a>'
            f'<a href="{room}" rel="nofollow">{label}</a>'
            f'<script async="" src="https://www.airbnb.com/embeddable/airbnb_jssdk"></script></div>')

def block(inner):
    return ('    <div class="block">\n'
            '      <h3>Where we\'re staying</h3>\n'
            f'{inner}'
            '      <p>Address, check-in details, and the door code once we have them.</p>\n'
            '    </div>')

VILLA = ('      <a class="seealso" href="https://andreachiacchio.github.io/villa-cristina-guest-app/" '
         'target="_blank" rel="noopener" style="margin-bottom:12px">🏠 Villa guest app &amp; house guide →</a>\n')

pages = {
 'rome.html':    block('      '+embed("996140170924809285","Rental unit in Rome · ★4.96 · 3 bedrooms · 6 beds · 2.5 baths")+'\n'),
 'venice.html':  block('      '+embed("39298847","Rental unit in Venice · ★4.75 · 3 bedrooms · 6 beds · 2 baths")+'\n'),
 'tuscany.html': block('      '+embed("34525431","Villa in Greve in Chianti · ★5.0 · 4 bedrooms · 5 beds · 4 baths")+'\n'),
 'amalfi.html':  block(VILLA+'      '+embed("1378964735087256336","Villa in Praiano · ★5.0 · 4 bedrooms · 6 beds · 3 baths")+'\n'),
}

for f, newblock in pages.items():
    h = open(f).read()
    assert h.count(PLACEHOLDER) == 1, f"{f}: placeholder not found uniquely ({h.count(PLACEHOLDER)})"
    h = h.replace(PLACEHOLDER, newblock)
    open(f,'w').write(h)
    print(f"{f}: embed added" + (" + villa link" if f=='amalfi.html' else ""))
print("done")
