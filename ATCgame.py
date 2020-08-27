import pygame
import math
global score
score = 0
class Plane:
     def __init__(self,elevation,x,y,speed,heading,destination,name,pastPositions):
          self.elevation = elevation
          self.x = x
          self.y = y
          self.speed = speed
          self.heading = heading
          self.destination = destination
          self.name = name
          self.pastPositions = pastPositions
          pastPositions = []
          pass
     def move(self):
          self.pastPositions.append((self.x,self.y))
          if len(self.pastPositions)==6:
               del self.pastPositions[0]
          else:
               pass
          
          
          '''
          Convert heading and speed to new x,y
          pixels = speed/10
          '''
          if self.heading>180:
               heading_modified = 180 - (self.heading-180)
          else:
               heading_modified = self.heading
              
          A = heading_modified
          B = 90
          C = 180 - (self.heading+B)
          b = self.speed/20

          a = int(b*(math.sin(math.radians(A))/math.sin(math.radians(B))))
          c = int(b*(math.sin(math.radians(C))/math.sin(math.radians(B))))

          if self.heading!=heading_modified:
               a*=-1

          #if heading_modified>90:
          #     c*=-1

          a*=-1
          b*=-1

          self.x+=a
          self.y+=c
          
          pygame.draw.circle(gameDisplay, (255,255,255), (self.x,self.y), 3)
          for thing in self.pastPositions:
               pygame.draw.circle(gameDisplay, (240,240,240), (thing[0],thing[1]), 1)

          pygame.draw.line(gameDisplay, (30,250,30), (self.x,self.y),(self.x+a,self.y+c),1)
          writeColor(self.x, self.y, 12, 0, self.name, (50,50,250))
          pygame.display.update()

          if self.x>(destination_coordinates[self.destination][0]-15) and self.x<(destination_coordinates[self.destination][0]+15) and self.y>(destination_coordinates[self.destination][1]-15) and self.y<(destination_coordinates[self.destination][1]+15):
               global score
               landed.append(self.name)
               score += 1

               
def writeColor(x, y, s, angle, text, color):
     myfont = pygame.font.SysFont('freemono', s)
     textsurface = myfont.render(text, False, color)
     textsurface = pygame.transform.rotate(textsurface, angle)
     gameDisplay.blit(textsurface,(x,y))

area = [
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
     ]

destinations = []
destination_coordinates = []
disp_w = 900
disp_h = 600

pygame.init()
gameDisplay = pygame.display.set_mode((disp_w, disp_h))
pygame.display.set_caption('ATC Sim')

def drawArea():
     pygame.draw.rect(gameDisplay, (0,0,0), (0,0,900,600))
     county = 0
     for row in area:
          countx = 0
          for number in row:
               if number != 0:
                    pygame.draw.circle(gameDisplay, (number*20,100,100), (countx*30, county*30), 10)
                    destinations.append(number)
                    destination_coordinates.append((countx*30, county*30))
                    writeColor(destination_coordinates[number-1][0], destination_coordinates[number-1][1], 10, 0, str(number), (255,255,255))
               countx+=1
          county+=1
     pygame.display.update()

drawArea()


names = ['aa3377', 'ak7777', 'af3141', 'sw9909', 'ag3436', 'av0000', 'ac4563']

American1 = Plane(32000,300,300,400,135,3,'aa1000',[])
American2 = Plane(32000,400,310,100,135,3,'aa2100',[])
United    = Plane(30000,200,200,350,190,2,'untd',[])
American  = Plane(35000,600,600,300,120,1,names[0],[])
Alaskan   = Plane(30000,600,100,350,120,0,names[1],[])
AirFrance = Plane(35000,000,100,200,270,1,names[2],[])
SouthWest = Plane(27000,400,300,150,000,4,names[3],[])
Allegiant = Plane(39000,900,300,200,100,2,names[4],[])
AirVietnam= Plane(35000,600,500,350,120,3,names[5],[])
AirChina  = Plane(15000,000,000,800,350,1,names[6],[])

pos_planes = [American,Alaskan,AirFrance,SouthWest,Allegiant,AirVietnam,AirChina]
landed = []

planes = [American1, American2, United]

num = 0
counter=0

def blackout():
     writeColor(selected.x+5, selected.y+10, 13, 0, 'Heading: '+str(selected.heading), (0,0,0))
     writeColor(selected.x+5, selected.y+20, 13, 0,'Speed: '+str(selected.speed), (0,0,0))
     writeColor(selected.x+5, selected.y+30, 13, 0,'FL: '+str(int(selected.elevation/100)), (0,0,0))

def lose():
     pygame.draw.rect(gameDisplay, (0,0,0), (0,0,disp_w,disp_h))
     writeColor(disp_w/2, disp_h/2, 30, 0, 'You\'re fired!', (250,0,0))
     pygame.display.update()
     pygame.time.wait(3000)
     pygame.quit()
     quit()

def win():
     pygame.draw.rect(gameDisplay, (0,0,0), (0,0,disp_w,disp_h))
     writeColor(disp_w/2, disp_h/2, 30, 0, 'You survived \nanother shift!', (0,250,0))
     pygame.display.update()
     pygame.time.wait(3000)
     pygame.quit()
     quit()

def spawn_new():
     try:
          planes.append(pos_planes[0])
          del pos_planes[0]
     except:
          pass
     if len(planes)==0:
          win()

while 1:
     pygame.time.wait(10)
     counter+=1
     
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               pygame.quit()
               quit()

          if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_LEFT:
                    if (num+1)<len(planes):
                         num+=1
                    else:
                         num=0
               if event.key == pygame.K_RIGHT:
                    if (num-1)<0:
                         num=len(planes)-1
                    else:
                         num-=1
               if event.key == pygame.K_UP:
                    blackout()
                    selected.elevation+=500
               if event.key == pygame.K_DOWN:
                    blackout()
                    selected.elevation-=500
               if event.key == pygame.K_s:
                    blackout()
                    selected.speed-=50
               if event.key == pygame.K_w:
                    blackout()
                    selected.speed+=50
               if event.key == pygame.K_a:
                    blackout()
                    selected.heading-=5
               if event.key == pygame.K_d:
                    blackout()
                    selected.heading+=5
               if event.key == pygame.K_SPACE:
                    pause=True
                    writeColor(50, 100, 20, 0, 'Paused', (255,0,255))
                    pygame.display.update()
                    while pause==True:
                         pygame.time.wait(20)
                         for event in pygame.event.get():
                              if event.type == pygame.QUIT:
                                   pygame.quit()
                                   quit()

                              if event.type == pygame.KEYDOWN:
                                   if event.key == pygame.K_SPACE:
                                        pause = False
                                        writeColor(50, 100, 20, 0, 'Paused', (0,0,0))
                                        pygame.display.update()
          else:
               pass
     if counter==100:
          drawArea()
          positions=[]
          for plane in planes:
               positions.append([plane.x, plane.y, plane.elevation])
               for thing in landed:
                    if thing==plane.name:
                         planes.remove(plane)
                         spawn_new()
               plane.move()
               
          xs = []
          ys = []
          elevs = []
          for li in positions:
               xs.append(li[0])
               ys.append(li[1])
               elevs.append(li[2])
          trackera = 0
          for val in xs:
               trackerb = 0
               for other in xs:
                    if (other-10)<val and val<(other+10) and trackera!=trackerb:
                         if (ys[trackera]-10<ys[trackerb] and ys[trackerb]<ys[trackera]+10)or(ys[trackerb]-10<ys[trackera] and ys[trackera]<ys[trackerb]+10):
                              if (elevs[trackera]-10000<elevs[trackerb] and elevs[trackerb]<elevs[trackera]+10000)or(elevs[trackerb]-10000<elevs[trackera] and elevs[trackera]<elevs[trackerb]+10000):
                                   lose()
                    trackerb+=1
               trackera+=1
               
               
          counter=0
          writeColor(0, 0, 20, 0, str(score), (0,255,0))
          
     try:
          selected = planes[num]
     except:
          selected = planes[0]
          
     pygame.draw.circle(gameDisplay, (0,250,0), (selected.x, selected.y), 5)
     
     writeColor(selected.x+5, selected.y+10, 13, 0, 'Heading: '+str(selected.heading), (255,200,200))
     writeColor(selected.x+5, selected.y+20, 13, 0,'Speed: '+str(selected.speed), (255,200,200))
     writeColor(selected.x+5, selected.y+30, 13, 0,'FL: '+str(int(selected.elevation/100)), (255,200,200))
     writeColor(selected.x+5, selected.y+40, 13, 0,'Destination: '+str(selected.destination+1), (255,200,200))
     pygame.display.update()


pygame.quit()
