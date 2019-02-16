#Have to work in point loss, as well as rat and sprinkle moving next wk. 


def setup():
    size(1920, 1200)
    frameRate(700)
    stroke(255)
    global table
    global donut
    global explosion
    global sprinkles
    global rat
    global verttable
    global vertrat
    global reversedrat
    global loss
    global cat
    global ipt
    global tpt
    global thpt
    global fpt
    global vpt
    table = loadImage("tabletop.png")
    donut = loadImage("donut.png")
    explosion = loadImage("explosion.png")
    sprinkles = loadImage("sprinkles.png")
    rat = loadImage("rat.png")
    verttable = loadImage("rotated table.jpeg") 
    vertrat = loadImage("rat copy.png")
    reversedrat = loadImage("reversed_rat.png")
    loss = loadImage("Loss.png")
    cat = loadImage("cat.png")
    ipt = loadImage("1pt.png")
    tpt = loadImage("2pt.png")
    thpt = loadImage("3pt.png")
    fpt = loadImage("4pt.png")
    vpt = loadImage("5pt.png")

def draw():
    pts = 5
    background(0)
    table.resize(1920, 200)
    verttable.resize(200, 400)
    donut.resize(100, 100)
    explosion.resize(100, 100)
    sprinkles.resize(100, 50)
    rat.resize(300, 300)
    vertrat.resize(200, 200)
    reversedrat.resize(300, 300)
    cat.resize(200, 200)
    loss.resize(800,700)
    ipt.resize(800, 700)
    tpt.resize(800, 700)
    thpt.resize(800, 700)
    fpt.resize(800, 700)
    vpt.resize(800, 700)
  
    image(table, 0, 0)
    image(verttable, 1720, 0)
    image(table, 0, 400)
    image(verttable, 0, 400)
    image(table, 0, 800)
    image(verttable, 1720, 800)
    
    if mouseY >= 0 and mouseY <= 200 or mouseY >= 760 and mouseY <= 1000:
        image(donut, mouseX, mouseY)
        image(rat, mouseX - 500, mouseY-100)
        if mouseY >= 0 and mouseY <= 190: 
            image(sprinkles, 1920-mouseX, 0)
            if mouseX in range(1870-mouseX, 1970-mouseX)and mouseY in range(0, 50):
                image(loss, width/2 -400, (height/2) - 200)
                pts -=1
        if mouseY >= 760 and mouseY <= 1000:
            image(sprinkles, 1920-mouseX, 800)
            if mouseX in range(1870-mouseX, 1970-mouseX) and mouseY in range(780, 850):
                image(loss, width/2 -400, (height/2) - 200)
                pts -=1
    elif mouseY >= 370 and mouseY <= 600:
         image(donut, mouseX, mouseY)
         image(reversedrat, mouseX + 500, mouseY-100)
         image(sprinkles, 1920-mouseX, 400)
         if mouseX in range(1870-mouseX, 1970-mouseX) and mouseY in range(370, 420):
            image(loss, width/2 -400, (height/2) - 200)
            pts -=1
    elif mouseY >= 0 and mouseY <= 400 and mouseX >= 1720:
         image(donut, mouseX, mouseY)
         image(vertrat, mouseX-100, mouseY - 200)
    elif mouseY >= 400 and mouseY <= 800 and mouseX <= 200:
         image(donut, mouseX, mouseY)
         image(vertrat, mouseX-50, mouseY -200)
    elif mouseY >= 800 and mouseX >= 1720:
         image(donut, mouseX, mouseY)
         image(vertrat, mouseX-100, mouseY - 200)
         if mouseY >= 700:
            image(cat, mouseX-200, mouseY - 220)
    else:
        image(explosion, mouseX, mouseY)
        image(loss, width/2 -400, (height/2) - 200)
        
